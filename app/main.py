import sys
import pdftotext
from textblob import TextBlob
import operator
import pickle

input_folder_path = "input/"
pickle_store_path = "cache/store.pickle"
if len(sys.argv) < 2:
  raise Exception('ERROR: you need to input the filename as the first argument for this script.')

filename = sys.argv[1]
filename_without_extension = filename.split('.')[0]

try:
    with open(pickle_store_path,"rb") as pickle_in:
      store = pickle.load(pickle_in)
except FileNotFoundError:
    print("File not accessible")

with open(input_folder_path + filename, "rb") as f:
    pdf = pdftotext.PDF(f)
raw_text = "".join(pdf)

blob = TextBlob(raw_text)

np_counts = blob.np_counts
np_counts_sorted = sorted(np_counts.items(),key=operator.itemgetter(1),reverse=True)
np_counts_filtered = np_counts_sorted[:20]

this_text_analysis = {}
this_text_analysis['raw_text'] = raw_text
this_text_analysis['np_counts'] = np_counts_sorted
this_text_analysis['np_counts_sorted'] = np_counts_sorted
this_text_analysis['np_counts_filtered'] = np_counts_filtered

try:
  store[filename_without_extension] = this_text_analysis
except NameError:
  with open(pickle_store_path,"wb") as pickle_out:
    store = {}
    store[filename_without_extension] = this_text_analysis
    pickle.dump(store, pickle_out)
    pickle_out.close()
# for item in np_counts_filtered:
#   print(item)
