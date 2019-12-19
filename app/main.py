import pdftotext
import sys

input_folder_path = "input/"
filename = sys.argv[1]

with open(input_folder_path + filename, "rb") as f:
    pdf = pdftotext.PDF(f)

text = "".join(pdf)
