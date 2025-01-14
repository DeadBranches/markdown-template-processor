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