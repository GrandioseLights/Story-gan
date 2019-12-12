##trainingData = open("-- data.txt", 'r').read().rstrip().split()
##learnedData = {}
##dataIndex = 0
##learnList = []
##
##for word in trainingData:
##    try:
##        learnedData[word] = learnedData.get(word) + ", " + trainingData[dataIndex + 1]
##    except TypeError:
##        learnedData[word] = trainingData[dataIndex + 1]
##    except:
##        break
##    
##    dataIndex += 1
##print(learnedData)
