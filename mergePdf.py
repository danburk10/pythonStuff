#!/usr/bin/env python

from pypdf import PdfMerger
import sys

for line in sys.argv[1:]:
    print("*",line,"*")

pdfs = sys.argv[1:]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

