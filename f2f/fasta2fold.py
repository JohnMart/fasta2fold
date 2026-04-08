import click
import datetime
import os
from f2f.util import pdbtools
from datetime import datetime

__version__ = "0.1.0"

@click.command()
@click.version_option(__version__, prog_name="fasta2tm")
@click.option('--input-dir', '-idir', required='true', help='Folder containing PDB files or FASTA files.')
@click.option('--output-dir', '-odir', default=None, help='Folder to place the results.')
def fasta2fold(input_dir, output_dir):
    SUCCESS_MESSAGE = '\033[92m' + "f2f: " + '\033[0m'
    
    # Set the output directory to the current directory with timestamp if no user input
    if not output_dir:
        output_dir = os.curdir + "/" + "fasta2fold_results_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    input_files = []
    
    # Retrieve all the artifacts in the directory
    artifacts = os.listdir(input_dir)
    
    # Loop through each artifacts to collect all files
    for artifact in artifacts:
        path = os.path.join(input_dir, artifact)
        if os.path.isfile(path):
            input_files.append(path)
    
    # Convert each PDB file into a FASTA file
    for file in input_files:
        pdbtools.pdb2fasta(file, output_dir)
    
    # Build the Mega FASTA file
    pdbtools.fasta2megafasta(output_dir)
    
    print(SUCCESS_MESSAGE + str(len(input_files)) + " PDB files successfully converted to FASTA files.")