# Markdown Template Processor Script
# 
# This NuShell script automates the execution of the Markdown Template Processor Python script
# using predefined file paths for the input Markdown document, Jinja2 template, and output file.
# It also supports optional activation of a Conda environment.
#
# Usage:
#     source examples/generate.nu
#
# Prerequisites:
# - Python installed with required dependencies (see README.md).
# - Optional: Conda installed if using a virtual environment.
#
# Input:
# - A Markdown document containing structured content.
# - A Jinja2 template defining how the content is processed and formatted.
#
# Output:
# - A formatted Markdown file in the specified output directory.
#
# Logs:
# The script logs status messages to provide feedback on file processing and Conda environment activation.

use std log

# leave blank for no conda environment
let conda_environment: string = 'side-projects'

let python_file: path = '..\src\main.py' | path expand

let input_filepath: path = '.\input-documents\DSM-V-TR - Autism Spectrum Disorder.md' | path expand
let output_filepath: path = '.\outputs\DSM-V-TR - Autism Spectrum Disorder.md' | path expand
let template_filepath: path = '.\templates\template.md' | path expand

if (($output_filepath | path exists) == true) {
    log info "Output file already exists. Removing."    
    rm $output_filepath
}

if ($conda_environment | is-not-empty) {
    conda activate $conda_environment
}

with-env { PYTHON_UTF8:1 } {
    python $python_file -i $input_filepath -t $template_filepath -o $output_filepath
    log info "[markdown-template-processor] Finished."
}