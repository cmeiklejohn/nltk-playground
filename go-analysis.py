from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize

# Read in the Go corupus.
raw = ""

with open("go-corpus.txt", 'r') as fh:
    for line in fh:
        raw = raw + line

# Tokenize words
tokens = word_tokenize(raw)

print "Number of tokens: "
print len(tokens)
print

print "First 10 tokens: "
print tokens[:10]
print

fdist1 = nltk.FreqDist(tokens)

print "Frequency distribution: "
print fdist1
print

print "10 most common: " 
print fdist1.most_common(10)
print

trigrams = nltk.ngrams(tokens, 3)

print "Number of trigrams: "
print len(list(trigrams))
print 

fdist2 = nltk.FreqDist(trigrams)

print "Number of trigrams: "
print len(fdist2.items())
print

print "Frequency distribution: "
print fdist2
print

print "10 most common: " 
print fdist2.most_common(10)
print