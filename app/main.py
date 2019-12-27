import sys
import pdftotext
from textblob import TextBlob
import operator
from utils import print_list

max_subjectivity = 0.6
input_folder_path = "input/"
if len(sys.argv) < 2:
  raise Exception('ERROR: you need to input the filename as the first argument for this script.')

filename = sys.argv[1]
filename_without_extension = filename.split('.')[0]

with open(input_folder_path + filename, "rb") as f:
    pdf = pdftotext.PDF(f)
raw_text = "".join(pdf)

def analyse_string(string):
  blob = TextBlob(raw_text)
  np_counts = blob.np_counts
  np_counts_sorted = sorted(np_counts.items(),key=operator.itemgetter(1),reverse=True)
  np_counts_filtered = np_counts_sorted[:20]
  sentences = string_to_sentences(blob)
  sentences_sentiments = build_sentences_sentiments_list(sentences)

  filtered_sentences_sentiments = filter_sentences_sentiments(sentences_sentiments)
  sorted_sentences_sentiments = sort_sentences_sentiments(filtered_sentences_sentiments)
  
  five_most_positive=sorted_sentences_sentiments[-5:]
  five_most_negative=sorted_sentences_sentiments[:4]
  print_list(five_most_positive)
  result = {}
  result['raw_text'] = raw_text
  result['np_counts'] = np_counts_sorted
  result['np_counts_sorted'] = np_counts_sorted
  result['np_counts_filtered'] = np_counts_filtered
  result['sentences_sentiments'] = sentences_sentiments
  result['sorted_sentences_sentiments'] = sorted_sentences_sentiments
  return result

def string_to_sentences(blob):
  return blob.sentences

def build_sentences_sentiments_list(sentences):
  result = []
  for index, sentence in enumerate(sentences):
    result.append({ 'position': index, 'sentence': sentence, 'sentiment': sentence.sentiment })
  return result

# very naive, taking into account only the polarity
def sort_sentences_sentiments(sentences_sentiments):
  return sorted(sentences_sentiments, key=lambda x: getattr(x['sentiment'],'polarity'))

def filter_sentences_sentiments(sentences_sentiments):
  return filter(lambda x: (getattr(x['sentiment'],'subjectivity') < max_subjectivity), sentences_sentiments)

this_text_analysis = analyse_string(raw_text)