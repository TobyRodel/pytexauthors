from pandas import read_excel
from argparse import ArgumentParser
from pyauthor import mnras_auth_list as authlist

parser = ArgumentParser(prog='PyTeXAuthors')
parser.add_argument('--tablepath', '-i', help='Path to author list spreadsheet.')
parser.add_argument('--outpath', '-o', help='Path to output author list TeX file.')
args = parser.parse_args()

authors = read_excel(args.tablepath)
affls = read_excel(args.tablepath, 1)

authlist(args.outpath, authors, affls)