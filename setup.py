from setuptools import setup, find_packages

setup(
    name='fasta2fold',
    version='0.1.0',
    description='v0.1.0 - Converts PDB files to FASTA files',
    author='John M',
    url='',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fasta2fold=f2f.fasta2tm:fasta2fold',
            'f2f=f2f.fasta2fold:fasta2fold'
        ],
    },
    install_requires=[
        'click',
        'biopython'
    ]
)