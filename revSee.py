'''
FILE:	revSee.py
AUTHOR:	J.R. Hendrix
URL: 	http://stronglab.org
DESC:	This script imports a FASTA file
		and exports the reverse complement sequence
'''


# IMPORT FROM PYTHON STANDARD LIBRARY
import argparse
import operator
import os
import sys
import time

from Bio import SeqIO	# Source: https://biopython.org/wiki/SeqIO
from Bio.SeqRecord import SeqRecord


def reverseC(args):

	# CREATE OUTPUT FILE
	try:
		outdir = '/'.join((args.output_path, args.output_directory))
		if not os.path.exists(outdir):
			os.mkdir(outdir)
		prefix = '/'.join((outdir, args.savename))
		outf = ".".join((prefix, 'fasta'))
		f = open(outf, 'w')
		
	except:
		print('ERROR: Could not configure output GFA file. Skipping...')
		return

	for record in SeqIO.parse(args.fasta, 'fasta'):
		s = record.seq.reverse_complement()

		newID = '_'.join((record.id, 'reverse_complement'))
		newRecord = SeqRecord(
			s,
			id=newID
			)

		SeqIO.write(newRecord, f, 'fasta')

	f.close()




def main(program):
	cwd = os.getcwd()

	# PARSER : ROOT
	# NOTE: optional arguments must preceed positional arguments on the command line
	parent_parser = argparse.ArgumentParser(prog='revSee', add_help=False)
	parent_parser.add_argument('-f', '--fasta', help='FASTA file of sequence (required)', required=True)
	parent_parser.add_argument('-o', '--output_directory', default='reverse_complement', help='Prefix of output directory', type=str)
	parent_parser.add_argument('-p', '--output_path', default=cwd, help='Path to output', type=str)
	parent_parser.add_argument('-s', '--savename', default='extract', help='Prefix for output.')
	subparsers = parent_parser.add_subparsers(help='sub-command help')

	args = parent_parser.parse_args()

	# GET REVERSE COMPLEMENT
	reverseC(args)


if __name__ == "__main__":
	main(sys.argv[1])










