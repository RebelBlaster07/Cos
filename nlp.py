import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from collections import Counter

# Download required NLTK data (only once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Input text
text = "Natural Language Processing helps computers understand human language."

# a. Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# b. Word Frequency
freq = Counter(tokens)
print("Word Frequency:", freq)

# c. Remove Stop Words
stop_words = set(stopwords.words('english'))
filtered = [w for w in tokens if w.lower() not in stop_words]
print("After Removing Stop Words:", filtered)

# d. POS Tagging
pos_tags = pos_tag(filtered)
print("POS Tags:", pos_tags)

========================================================================================================
import re
from collections import Counter

text = "Natural Language Processing helps computers understand human language."

# Tokenize
tokens = re.findall(r'\w+', text)

# Word frequency
print("Word Frequency:", Counter(tokens))

# Remove stopwords
stop_words = {'a', 'an', 'the', 'and', 'in', 'on', 'of', 'for', 'to', 'is', 'are', 'was', 'be', 'by'}
filtered = [w for w in tokens if w.lower() not in stop_words]
print("Filtered:", filtered)

# Simple POS tagging
tags = [(w, 'VBG' if w.endswith('ing') else 'NN') for w in filtered]
print("POS Tags:", tags)
