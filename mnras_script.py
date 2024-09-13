import pandas as pd
import sys
from pyauthor import mnras_auth_list as authlist

tablepath = sys.argv[1]
outpath = sys.argv[2]

authors = pd.read_excel(tablepath)
affls = pd.read_excel(tablepath, 1)

authlist(outpath, authors, affls)