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

print "Go Corpus"
print

# Question 1.
print "Question 1: Number of tokens"
print len(tokens)

tdist = nltk.FreqDist(tokens)

# Question 2.
print "Question 2: Most popular tokens"
print tdist.most_common(10)

trigrams = list(nltk.trigrams(tokens))

# Question 3.
print "Question 3: Number of trigrams"
print len(trigrams)

g3_dist = nltk.FreqDist(trigrams)

# Question 4.
print "Question 4: Most popular trigrams"
print g3_dist.most_common(10)

g3_cfdist = nltk.ConditionalFreqDist()
for trigram in list(trigrams):
    condition = trigram[0] == 'for'
    g3_cfdist[condition][trigram] += 1

# Question 5.
print "Question 5: Most popular trigrams starting with 'for'"
print g3_cfdist[True].most_common(10)

g3_cfdist1 = nltk.ConditionalFreqDist()
for trigram in list(trigrams):
    condition = trigram[0] == 'for'
    g3_cfdist1[condition][(trigram[0], trigram[1])] += 1

g3_cpdist1 = nltk.ConditionalProbDist(g3_cfdist1, nltk.ELEProbDist, g3_cfdist[True].B() + g3_cfdist[False].B())

# Question 6.
print "Question 6: Probability of i coming after 'for'"
print g3_cpdist1[True].prob(('for', 'i'))

# Question 7.
print "Question 7: Probability of e coming after 'for'"
print g3_cpdist1[True].prob(('for', 'e'))

# Question 8.
print "Question 8: Most probable 10 tokens that come after 'for' with probabilities"
items = []

for sample in g3_cpdist1[True].samples():
    items = items + [(sample, g3_cpdist1[True].prob(sample))]

items.sort(key=lambda tup: tup[1])
items.reverse()

i = 0

for item in items:
    if i == 10:
        break
    print "{0}: {1}".format(item[0], item[1])
    i = i + 1

# Question 9.
print "Question 9: Generate random code starting from the token 'for' up to 50 tokens"
for _ in range(50):
    print g3_cpdist1[True].generate()