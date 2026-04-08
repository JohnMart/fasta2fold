import sys
import os
import warnings
from pathlib import Path
from Bio import SeqIO

warnings.simplefilter('ignore')

def pdb2fasta(pdb_file, output_directory):
        
    # Retrieve the PDB File as an object via Path
    pdb_file_path = Path(pdb_file)
    
    # Convert the output directory string into a Path
    output_directory_path = Path(output_directory)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory_path, exist_ok=True)
    
    # Build the name and object value of the FASTA file
    pdb_file_name = pdb_file_path.name.replace('.pdb', '')
    fasta_file = os.path.join(output_directory_path, pdb_file_name + ".fasta")
    
    # Loop through each PDB file and convert to FASTA format
    with open(pdb_file, "r") as file:
        records = list(SeqIO.parse(file, "pdb-atom"))

    # Write to a FASTA file
    with open(fasta_file, "w") as fasta:
        SeqIO.write(records, fasta, "fasta")


def fasta2megafasta(input_directory):
    
    # Convert the input directory string into a Path
    input_directory_path = Path(input_directory)
    
    # Build the name and object value of the Mega FASTA file
    mega_fasta_file = os.path.join(input_directory_path, "_mega_fasta.fasta")
    
    fasta_files = []
    
    # Retrieve all artifacts in the directory
    artifacts = os.listdir(input_directory)
    
    # Loop through each artifacts to verify it is a file
    for artifact in artifacts:
        path = os.path.join(input_directory, artifact)
        if os.path.isfile(path):
            fasta_files.append(path)
    
    # Build the Mega FASTA file with the contents of each FASTA file in the directory
    with open(mega_fasta_file, "w") as mega_fasta:
        for file in fasta_files:
            with open(file, "r") as fasta_file:
                fasta_file_path = Path(file)

                fasta_contents = fasta_file.read()
                
                mega_fasta.write('----------------------------------------' + '\n')
                mega_fasta.write(fasta_file_path.name + ' START' + '\n')
                mega_fasta.write('----------------------------------------' + '\n')
                mega_fasta.write(fasta_contents)
                mega_fasta.write('----------------------------------------' + '\n')
                mega_fasta.write(fasta_file_path.name + ' END' + '\n')
                mega_fasta.write('----------------------------------------' + '\n')