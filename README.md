# revSee
A tool to generate the reverse complement of a DNA sequence

## Requirements
* Python 3+
* BioPython


## Usage
As input, revSee.py requires a DNA sequence in FASTA format. The FASTA file can contain multiple sequences. The reverse complement of all sequences in the FASTA will be generated and exported to a single output file. 
```
# Basic usage
python revSee.py -f file.fasta
```

revSee.py will export the sequences to a directory called reverse_complement/. To change the name of this directory use the -o or --output_directory flag. By default, revSee.py will create this directory in the current working directory. To change the path to the output directory, use the -p or --output_path flag. The exported FASTA file will be named filename_revC.fasta where filename is the name of the input file. For example, if the input fasta file is called my_sample.fasta, then revSee.py will create a file named my_sample_revC.fasta. The name of the exported file can be changed using the -s or --savename flag. 

```
# Extensive usage
python revSee.py -f file.fasta -p /different/path -o output -s my_new_seqs
```
