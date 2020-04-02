import random
dataIn = open("data.txt", 'r').read().casefold().split()
#dataOut= open("Stored.txt",'w')
def mergeA(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
learnDict = {}
dataLen = len(dataIn)
index = 0
j = 0
length = 30
sentance = ""
succsess = False
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
    print("Error handled.")
  index = index + 1

while succsess == False:
  try:
    word1 = random.choice(dataIn)
    try:
      word2 = random.choice(learnDict[word1+"¶"].split())
    except:
      word2 = learnDict[word1+"¶"]
    try:
      word3 = random.choice(mergeA(learnDict[word2+"¶"].split(),
      learnDict[word1+"¶¶"].split()))
    except:
      word3 = learnDict[word1+"¶"]
    try:
      word4 = random.choice(mergeA(learnDict[word3+"¶"].split(),
      mergeA(learnDict[word2+"¶¶"].split(),
      learnDict[word1+"¶¶¶"].split())))
    except:
      word4 = learnDict[word1+"¶"]
    try:
      word5 = random.choice(mergeA(learnDict[word4+"¶"].split(),
      mergeA(learnDict[word3+"¶¶"].split(),
      mergeA(learnDict[word2+"¶¶¶"].split(),
      learnDict[word1+"¶¶¶¶"].split()))))
    except:
      word5 = learnDict[word1+"¶"]

    while j < length:

      word1 = random.choice(mergeA(learnDict[word5+"¶"].split(),
      mergeA(learnDict[word4+"¶¶"].split(),
      mergeA(learnDict[word3+"¶¶¶"].split(),
      mergeA(learnDict[word2+"¶¶¶¶"].split(),
      learnDict[word1+"¶¶¶¶¶"].split())))))

      word2 = random.choice(mergeA(learnDict[word5+"¶¶"].split(),
      mergeA(learnDict[word4+"¶¶¶"].split(),
      mergeA(learnDict[word3+"¶¶¶¶"].split(),
      mergeA(learnDict[word2+"¶¶¶¶¶"].split(),
      learnDict[word1+"¶"].split())))))

      word3 = random.choice(mergeA(learnDict[word5+"¶¶¶"].split(),
      mergeA(learnDict[word4+"¶¶¶¶"].split(),
      mergeA(learnDict[word3+"¶¶¶¶¶"].split(),
      mergeA(learnDict[word2+"¶"].split(),
      learnDict[word1+"¶¶"].split())))))

      word4 = random.choice(mergeA(learnDict[word5+"¶¶¶¶"].split(),
      mergeA(learnDict[word4+"¶¶¶¶¶"].split(),
      mergeA(learnDict[word3+"¶"].split(),
      mergeA(learnDict[word2+"¶¶"].split(),
      learnDict[word1+"¶¶¶"].split())))))

      word5 = random.choice(mergeA(learnDict[word5+"¶¶¶¶¶"].split(),
      mergeA(learnDict[word4+"¶"].split(),
      mergeA(learnDict[word3+"¶¶"].split(),
      mergeA(learnDict[word2+"¶¶¶"].split(),
      learnDict[word1+"¶¶¶¶"].split())))))

      sentance = sentance+ word1+" "+word2+" "+word3+" "+word4+" "+word5+" "
      j = j + 1
    succsess = True
  except:
    print("Error handled.")
    succsess = False

print("Data Size: ", dataLen/1000, "KB")
print(sentance)
