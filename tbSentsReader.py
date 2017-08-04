from nltk.corpus import ptb

fo = open("ptb.plainSents.txt", "w")

allSents = ptb.sents()

for sent in allSents:
    joined = " ".join(sent)
    fo.write(joined + "\n")

print ptb.sents()[:10]


