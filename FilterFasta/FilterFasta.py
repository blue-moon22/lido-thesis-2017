#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    A copy of the GNU General Public License is available at
#    http://www.gnu.org/licenses/gpl-3.0.html

"""Filter the contigs depending on their length."""

from __future__ import print_function
import os
import sys
from argparse import ArgumentParser


__author__ = "Mathieu Almeida, Amine Ghozlane"
__copyright__ = "Copyright 2014, INRA"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Mathieu Almeida, Amine Ghozlane"
__email__ = "mathieu.almeida77@jouy.inra.fr, amine.ghozlane@jouy.inra.fr"
__status__ = "Developpement"


def isfile(path):
    """Check if path is an existing file.
      :Parameters:
          path: Path to the file
    """
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = "{0} is a directory".format(path)
        else:
            msg = "{0} does not exist.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path


#===================
#parameters
#===================    
def config_parameters():
    """Extract program options
    """
    parser = ArgumentParser(description=__doc__,
                            usage="{0} -h [options] [arg]".format(sys.argv[0]))
    parser.add_argument('-f', '--readFasta', dest='fastafile', type=isfile,
                        help='Input fasta file. Warning : only *.fasta') 
    parser.add_argument('-t', '--trim', dest='trimsize', type=int, default=800,
                        help='Keep the contigs with trimSize or '
                        'more nucleotides.')
    parser.add_argument('-s', '--sample', dest='samplename', type=str,
                        default='', help='Define a sample name')
    parser.add_argument('-o', '--outfile', dest='outfile', type=str,
                        default=None, help='Define a sample name')
    return parser.parse_args()


#===========================================
#remove contigs or scaffolds shorter than trimSize
#===========================================    
def parse_fasta_file(FastaFileName, TrimSize, SampleName, OutFileName):
    """Parse the fasta file and remove contigs or scaffolds shorter than
    trimsize
    """
    NbContig = 0
    NbContigInOutput = 0    
    fragment=''
    header=''
    if not OutFileName:
        OutFileName = ('.'.join(FastaFileName.split('.')[0:-1]) + '.' +
                       str(TrimSize) + '.fasta')
    try:
        with open(FastaFileName, "rt") as FastaFile:
            with open(OutFileName, "wt") as OutFile:
                for line in FastaFile:
                    if line[0]=='>':
                        if header!='':
                            if len(fragment) >= TrimSize:
                                if SampleName == '':
                                    OutFile.write("{1}{0}{2}{0}".format(
                                        os.linesep, header, fragment))
                                else:
                                    OutFile.write("{1}.{2}{0}{3}{0}".format(
                                        os.linesep, header, SampleName,
                                        fragment))
                                NbContigInOutput = NbContigInOutput + 1
                            NbContig = NbContig + 1
                        fragment = ''
                        header = line.strip()
                    else:
                        fragment = fragment + line.strip()
                #last fragment
                if len(fragment) >= TrimSize:
                    if SampleName == '':
                        OutFile.write("{1}{0}{2}{0}".format(
                                        os.linesep, header, fragment))
                    else:
                        OutFile.write("{1}.{2}{0}{3}{0}".format(
                                        os.linesep, header, SampleName,
                                        fragment))
                    NbContigInOutput = NbContigInOutput + 1
    except IOError:
        sys.exit("Error cannot {0} or {1}".format(FastaFileName, OutFileName))
    print('Number of fragment in the input: {0}'.format(NbContig))
    print('Number of fragment in the output: {0}'.format(NbContigInOutput))


#===================
#MAIN
#===================
def main():
    """Main function
    """
    args = config_parameters()
    parse_fasta_file(args.fastafile, args.trimsize,
                     args.samplename, args.outfile)


if __name__=="__main__":
    main()
