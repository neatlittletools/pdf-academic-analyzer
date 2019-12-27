from textblob import TextBlob
import operator
from utils import print_list

def analyse_string(string,max_subjectivity):
  blob = TextBlob(string)
  np_counts = blob.np_counts
  np_counts_sorted = sorted(np_counts.items(),key=operator.itemgetter(1),reverse=True)
  np_counts_filtered = np_counts_sorted[:20]
  sentences = string_to_sentences(blob)
  sentences_sentiments = build_sentences_sentiments_list(sentences)

  filtered_sentences_sentiments = filter_sentences_sentiments(sentences_sentiments,max_subjectivity)
  sorted_sentences_sentiments = sort_sentences_sentiments(filtered_sentences_sentiments)
  
  five_most_positive=sorted_sentences_sentiments[-5:]
  five_most_negative=sorted_sentences_sentiments[:4]
  print_list(five_most_positive)
  result = {}
  result['raw_text'] = string
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

def filter_sentences_sentiments(sentences_sentiments,max_subjectivity):
  return filter(lambda x: (getattr(x['sentiment'],'subjectivity') < max_subjectivity), sentences_sentiments)