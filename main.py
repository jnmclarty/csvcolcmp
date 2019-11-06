

from argparse import ArgumentParser
from csv import DictReader

parser = ArgumentParser(description='Compare two columns in two csv files.')

parser.add_argument('left', help='The first file.')
parser.add_argument('l_col', help='The first file\'s column, either 0-indexed int or a str.')
parser.add_argument('--l_skip', type=int, default=0, help='Number of rows to skip, in the left file.')

parser.add_argument('right', help='The second file.')
parser.add_argument('r_col', help='The scond file\'s column, either 0-indexed int or a str.')
parser.add_argument('--r_skip', type=int, default=0, help='Number of rows to skip, in the right file.')

args = parser.parse_args()

def csv_parser(fname, col, skip, ReaderCls, **kwargs):
    contents = []

    try:
        slc = int(col)
    except:
        slc = col

    with open(fname) as f:
        rdr = ReaderCls(f, **kwargs)
        for i, row in enumerate(rdr):
            if i >= skip:
                contents.append(row[slc].lower().strip())
    return contents

l_file = csv_parser(args.left, args.l_col, args.l_skip, DictReader, delimiter=',', quotechar='"')
r_file = csv_parser(args.right, args.r_col, args.r_skip, DictReader, delimiter=',', quotechar='"')

out = []
for cell_value in l_file:
    if not(cell_value in r_file):
        out.extend([cell_value])

out = list(set(out))
out.sort()

for o in out:
    print(o)
