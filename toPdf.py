#!/usr/bin/env python3

'''ImageToPdf.
Convert an image or a set of image to a pdf file.
In case of directory, images must be numeric-ordered

Usage:
    toPdf.py PATH [-o OUTPUT]

Options:
    -h --help
    --version
    -o output file
'''

from docopt import docopt
from path import Path
import img2pdf


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')

    output_file = 'output.pdf'
    if (args['-o']):
        output_file = args['-o']

    output_file = Path(output_file)
    if not output_file.ext:
        output_file = output_file + '.pdf'

    if (args['PATH']):
        p = Path(args['PATH'])
        listfile = list()
        if p.isfile():
            listfile.append(p)
        if p.isdir():
            listfile.extend(p.files('*.jpg'))

        listfile.sort(key=lambda f: int(f.stem))
        # with open("output.pdf", "wb") as f:
        #     f.write(img2pdf.convert([i for i in listfile]))
        print("{} generated".format(output_file))
