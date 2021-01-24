#Outputs are word for word: Output paragraphs will be more random after every few merges.

### Stuff you can change ###
writeOutput  = False
length       = 20  #This is not the number of words, it is the number of merges.
############################

import random
import math
import warnings
dataIn = open("data.txt", 'r').read().casefold().split()
dataOut= open("Stored.txt",'w')
dataWarn1 = "Small ammounts of traning will result in less than desireable results!"

lst1 = ""
def mergeA(b, lst1, lst2 = lst1):
  c = round(b*math.ceil(b/1))
  a = random.randint(1,c)
  lst3 = [value for value in lst1 if value in lst2]
  if a != b:
    lst3 = lst1 + lst2
  return lst3
learnDict = {}
dataLen = len(dataIn)
index = 0
j = 0
g = ""
sentance = ""
succsess = False
storyDone = False
errorNum = 0


if 500 > len(dataIn):
  warnings.warn(dataWarn1)

print("Leaning Basics! Just a moment...")
while index < len(dataIn):
  word = dataIn[index]
  try:
    try:
      learnDict[str(word + "¶")] = learnDict[word + "¶"]+" "+str(dataIn[index+1])
    except:
      learnDict[str(word + "¶")] = str(dataIn[index+1])
    try:
      learnDict[str(word + "¶¶")] = learnDict[word + "¶¶"]+" "+str(dataIn[index+2])
    except:
      learnDict[str(word + "¶¶")] = str(dataIn[index+2])
    try:
      learnDict[str(word + "¶¶¶")] = learnDict[word + "¶¶¶"]+" "+str(dataIn[index+3])
    except:
      learnDict[str(word + "¶¶¶")] = str(dataIn[index+3])
    try:
      learnDict[str(word + "¶¶¶¶")] = learnDict[word + "¶¶¶¶"]+" "+str(dataIn[index+4])
    except:
      learnDict[str(word + "¶¶¶¶")] = str(dataIn[index+4])
    try:
      learnDict[str(word + "¶¶¶¶¶")] = learnDict[word + "¶¶¶¶¶"]+" "+str(dataIn[index+5])
    except:
      learnDict[str(word + "¶¶¶¶¶")] = str(dataIn[index+5])
  except:
    pass
  index = index + 1

print("Time to write...")

while storyDone == False:
  while succsess == False:
    try:
      word1 = random.choice(dataIn)
      word2 = random.choice(learnDict[word1+"¶"].split())
      try:
        word3 = random.choice(mergeA(learnDict[word2+"¶"].split(),
        learnDict[word1+"¶¶"].split()))
      except:
        word3 = random.choice(learnDict[word2+"¶"].split())
      try:
        word4 = random.choice(mergeA(learnDict[word3+"¶"].split(),
        mergeA(learnDict[word2+"¶¶"].split(),
        learnDict[word1+"¶¶¶"].split())))
      except:
        word4 = random.choice(learnDict[word3+"¶"].split())
      try:
        word5 = random.choice(mergeA(learnDict[word4+"¶"].split(),
        mergeA(learnDict[word3+"¶¶"].split(),
        mergeA(learnDict[word2+"¶¶¶"].split(),
        learnDict[word1+"¶¶¶¶"].split()))))
      except:
        word5 = random.choice(learnDict[word4+"¶"].split())
      succsess = True
    except:
      succsess = False
  
  try:
    while j < length:
      word1 = random.choice(
      mergeA(1,learnDict[word5+"¶"].split(),
      mergeA(1,learnDict[word4+"¶¶"].split(),
      mergeA(1,learnDict[word3+"¶¶¶"].split(),
      mergeA(1,learnDict[word2+"¶¶¶¶"].split(),
      learnDict[word1+"¶¶¶¶¶"].split())))))

      word2 = random.choice(
      mergeA(1,learnDict[word5+"¶¶"].split(),
      mergeA(1,learnDict[word4+"¶¶¶"].split(),
      mergeA(1,learnDict[word3+"¶¶¶¶"].split(),
      mergeA(1,learnDict[word2+"¶¶¶¶¶"].split(),
      learnDict[word1+"¶"].split())))))

      word3 = random.choice(
      mergeA(1,learnDict[word5+"¶¶¶"].split(),
      mergeA(1,learnDict[word4+"¶¶¶¶"].split(),
      mergeA(1,learnDict[word3+"¶¶¶¶¶"].split(),
      mergeA(1,learnDict[word2+"¶"].split(),
      learnDict[word1+"¶¶"].split())))))

      word4 = random.choice(
      mergeA(1,learnDict[word5+"¶¶¶¶"].split(),
      mergeA(1,learnDict[word4+"¶¶¶¶¶"].split(),
      mergeA(1,learnDict[word3+"¶"].split(),
      mergeA(1,learnDict[word2+"¶¶"].split(),
      learnDict[word1+"¶¶¶"].split())))))

      word5 = random.choice(
      mergeA(2,learnDict[word5+"¶¶¶¶¶"].split(),
      mergeA(1,learnDict[word4+"¶"].split(),
      mergeA(1,learnDict[word3+"¶¶"].split(),
      mergeA(1,learnDict[word2+"¶¶¶"].split(),
      learnDict[word1+"¶¶¶¶"].split())))))

      sentance = sentance+ word1+" "+word2+" "+word3+" "+word4+" "+word5+" "
      #print("Merge generated successfully.")
      j = j + 1
    storyDone = True
  except:
    succsess = False

print("Finished!! Data Size: ", dataLen/1000, "KB")
print(sentance)
i = ""
for x, y in learnDict.items():
  i = i + x + " : " + y + "\n"
if writeOutput == True:
  dataOut.write(i)
