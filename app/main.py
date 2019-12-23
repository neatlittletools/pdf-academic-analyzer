import sys
import pdftotext
from textblob import TextBlob
import operator

input_folder_path = "input/"
if len(sys.argv) < 2:
  raise Exception('ERROR: you need to input the filename as the first argument for this script.')

filename = sys.argv[1]
filename_without_extension = filename.split('.')[0]

with open(input_folder_path + filename, "rb") as f:
    pdf = pdftotext.PDF(f)
# merge everything into one string
raw_text = "".join(pdf)
# prepare TextBlob
blob = TextBlob(raw_text)
# access noun phrases counts
np_counts = blob.np_counts
# sort noun phrases by frequency in reverse order
np_counts_sorted = sorted(np_counts.items(),key=operator.itemgetter(1),reverse=True)

filtered = np_counts_sorted[:20]

for item in filtered:
  print(item)
