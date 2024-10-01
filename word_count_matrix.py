import re
import nltk
from nltk.tokenize import word_tokenize
from tqdm import tqdm
#nltk.download('punkt')
======================================================
def clean_text(text):
  return re.sub(r'[^a-z\s]','',text)
======================================================
def word_matrix(dict_words,sample_size):
  matrix = {}
  for key,value in tqdm(dict_words.items()):
    matrix[key]=[]
    for i in range(sample_size):
      matrix[key].append(value.count(i))
  return matrix
=======================================================
dict_words = {}
for i in tqdm(range(X.shape[0])):
  words = word_tokenize(clean_text(X.values[i][0]))
  for word in words:
    if (word not in dict_words.keys()):
      dict_words[word] = []
      dict_words[word].append(i)
    else:
      dict_words[word].append(i)
word_count = word_matrix(dict_words ,X.shape[0])
