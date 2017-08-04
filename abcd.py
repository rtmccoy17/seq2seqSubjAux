from random import randint
import random
import numpy as np

fo1 = open("abcd.train", "w")
fo2 = open("abcd.test", "w")
letters = ['A', 'B', 'C', 'D']


inputs1 = []
inputs2 = []
inputs3 = []
inputs4 = []
inputs5 = []
inputs6 = []
inputs7 = []
inputs8 = []

allInputs = [inputs1, inputs2, inputs3, inputs4, inputs5, inputs6, inputs7, inputs8]

prevInputs = ['']
for member in allInputs:
    for string in prevInputs:
        for letter in letters:
            member.append((string + " " + letter).strip())
    prevInputs = member

for member in allInputs:
    random.shuffle(member)


testOptions = [[], [], [], inputs4[:1], inputs5[:604], inputs6[:1000], inputs7[:7870], inputs8[:8599]]

trainOptions = [inputs1, inputs2, inputs3, inputs4[1:], inputs5[604:], inputs6[1000:], inputs7[7870:], inputs8[8599:]]

trainSet = []
for length in trainOptions:
    trainSet += list(np.random.choice(length, 9000))

print len(trainSet)

trainSetRandom = []

for trainItem in trainSet:
    words = trainItem.split()
    trainItemRev = " ".join(list(reversed(words)))
    trainSetRandom.append(trainItem + " FWD" + "\t" + trainItem + " FWD" + "\n")
    trainSetRandom.append(trainItem + " REV" + "\t" + trainItemRev + " REV" + "\n")

random.shuffle(trainSetRandom)
for item in trainSetRandom:
    fo1.write(item)

testSet = []
for length in testOptions:
    testSet += length

testSet = sorted(testSet)
for testItem in testSet:
    words = testItem.split()
    testItemRev = " ".join(list(reversed(words)))
    fo2.write(testItem + " FWD" + "\t" + testItem + " FWD" + "\n")
    fo2.write(testItem + " REV" + "\t" + testItemRev + " REV" + "\n")

#print inputs2

#inputs = []

#for length in range(8):
 #   for count in range(9000):
  #      sent = []
   #     for num in range(length + 1):
    #        sent.append(letters[randint(0,3)])
#
 #       string = " ".join(sent)
  #      stringRev = " ".join(list(reversed(sent)))
   #     inputs.append(string + " FWD" + "\t" + string + " FWD" + "\n")
    #    inputs.append(string + " REV" + "\t" + stringRev + " REV" + "\n")
#
#random.shuffle(inputs)
#for inputSent in inputs:
#    fo.write(inputSent)
#
