import sys
import pdftotext
from analyser import analyse_string

max_subjectivity = 0.6
input_folder_path = "input/"
if len(sys.argv) < 2:
  raise Exception('ERROR: you need to input the filename as the first argument for this script.')

filename = sys.argv[1]
filename_without_extension = filename.split('.')[0]

with open(input_folder_path + filename, "rb") as f:
    pdf = pdftotext.PDF(f)
raw_text = "".join(pdf)



this_text_analysis = analyse_string(string=raw_text, max_subjectivity=max_subjectivity)