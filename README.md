<a name="readme-top"></a>

<div align="center">
  <h3 align="center">Markdown Template Processor</h3>
  <p align="center">
    A tool to dynamically extract and format sections of Markdown documents using Jinja2 templates.
  </p>
</div>

---

## About The Project

The **Markdown Template Processor** simplifies the extraction and formatting of structured Markdown content using Jinja2 templates. This is ideal for processing documents like technical specifications, diagnostic criteria, or structured reports into a reusable format.

### Features

- Dynamically extracts sections from Markdown based on headers.
- Formats extracted sections using Jinja2 templates.
- Outputs formatted content as a new Markdown file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

To use the Markdown Template Processor locally, follow these steps:

### Prerequisites

1. **Python**: Install Python 3.8 or higher.
   ```sh
   sudo apt install python3
   ```
2. **Dependencies**: Install required Python packages:
   ```sh
   pip install jinja2
   ```
3. **Optional**: Conda for virtual environment management.

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/deadbranch-forks/markdown-template-processor.git
   ```
2. Navigate to the project directory:
   ```sh
   cd markdown-template-processor
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

### Running the Python Script

Run the processor directly with:
```sh
python src/main.py -i <input_markdown> -t <template_file> -o <output_file>
```

Example:
```sh
python src/main.py -i examples/input-documents/input-file.md \
                   -t examples/templates/template.md \
                   -o examples/outputs/output-file.md
```

### Using the NuShell Script

Automate the process with the `generate.nu` script:
```sh
nushell examples/generate.nu
```

Ensure you configure the file paths within the NuShell script to match your environment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the GNU Affero General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
