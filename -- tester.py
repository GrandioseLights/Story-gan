import random
training_data = open("-- READ ME.txt", 'r').read().casefold().split()
data_position = 0
first_word = ""
sentance = ""
sentance_length = 100
word_count = 0
unique_words = []
thrid_list = []
fourth_list = []

def inter(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

while data_position < len(training_data):
    try:
        trained_word = training_data[data_position]
        word_data = open(trained_word+".txt", 'a')
        word_data.write(training_data[data_position+1] + '\n')
        
        word_data = open(trained_word+"2.txt", 'a')
        word_data.write(training_data[data_position+2] + '\n')
        
        word_data = open(trained_word+"3.txt", 'a')
        word_data.write(training_data[data_position+3] + '\n')
        data_position += 1
    except IndexError:
        print("IndexError Error handled")
        break
    i = 0
    for i in unique_words:
        if i in unique_words:
            pass
        else:
            unique_words.append(trained_word)

data_position = 0

for file_name in unique_words:
    file_name = file_name.rstrip() #remove the trailing \n from the word in "english_words.txt".
    try: #try to open file "x.txt"
        opened_file = open(file_name+".txt", 'r')
    except:
        pass #if no txt for the word was found
    
    try: #try to open file "x2.txt"
        opened_file = open(file_name+"2.txt", 'r')
    except:
       pass #if no txt for the word was found

    try: #try to open file "x2.txt"
        opened_file = open(file_name+"3.txt", 'r')
    except:
        pass #if no txt for the word was found

while word_count < sentance_length:
    try:
        first_word = jump_word
    except:
        first_word = random.choice(training_data)
    try:
        second_word = random.choice(open(first_word+".txt", 'r').read().casefold().split())
                                          
        third_word = random.choice(inter(open(first_word+"2.txt", 'r').read().casefold().split(),open(second_word+".txt", 'r').read().casefold().split()))

        jump_word = random.choice(inter(open(first_word+"3.txt", 'r').read().casefold().split(),inter(open(second_word+"2.txt", 'r').read().casefold().split(),open(third_word+".txt", 'r').read().casefold().split())))
    except:
        print("Error handled")


    sentance = sentance + first_word + " " + second_word + " " + third_word + " "
    
    word_count = word_count + 3

print(sentance)
