import argparse
import re
from typing import Any, Dict, List, Optional

from jinja2 import BaseLoader, Environment, FileSystemLoader, Template


class MarkdownRules:
    @staticmethod
    def header(content: str, header_text: str) -> str:
        """
        Extract content from a markdown section starting with the specified header
        until the next header of same or higher level is encountered.
        """
        # Find the header level by counting the leading '#' characters
        header_level = len(re.match(r"^#+", header_text).group())

        # Create a pattern to match the exact header
        header_pattern = re.escape(header_text)

        # Find the start position of our target header
        match = re.search(header_pattern, content, re.MULTILINE)
        if not match:
            return ""

        start_pos = match.start()

        # Split the remaining content into lines
        remaining_content = content[start_pos:].split("\n")

        # Collect lines until we hit a header of same or higher level
        result_lines = []
        for line in remaining_content:
            # Check if line is a header
            header_match = re.match(r"^(#+)\s", line)
            if (
                header_match
                and len(header_match.group(1)) <= header_level
                and line != header_text
            ):
                # Found a header of same or higher level (fewer or equal #s)
                break
            result_lines.append(line)

        return "\n".join(result_lines).strip()


class MarkdownTemplateProcessor:
    def __init__(self):
        self.rules = MarkdownRules()

        # Create Jinja environment
        self.env = Environment(loader=BaseLoader())

        # Register custom filters
        self.env.filters["header"] = self.rules.header

    def process_template(self, template_path: str, markdown_path: str) -> str:
        """
        Process the template file using the markdown input file.
        """
        # Read the markdown content
        with open(markdown_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        # Read the template
        with open(template_path, "r", encoding="utf-8") as f:
            template_content = f.read()

        # Create template object
        template = self.env.from_string(template_content)

        # Render template with markdown content as input
        return template.render(content=markdown_content)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Process markdown file using a template"
    )
    parser.add_argument("--input", "-i", required=True, help="Input markdown file")
    parser.add_argument("--template", "-t", required=True, help="Template file")
    parser.add_argument("--output", "-o", required=True, help="Output file")

    args = parser.parse_args()

    # Create processor instance
    processor = MarkdownTemplateProcessor()

    # Process the template
    result = processor.process_template(args.template, args.input)

    # Write the output
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(result)


if __name__ == "__main__":
    main()
