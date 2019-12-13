# Story-gan
An experiment in which you supply a code some text, and it will spit out it's own original text.

Place training data in the `data.txt` file. Training data can be anything that is readable by the Python Shell, like essays
and news articles. It can even be other Python codes, or any programming language and math calculations.

Some training data has been placed in the `data.txt` file already.

The ammount of training data that you put in the `data.txt` file will increase the legibility of the outputted text,
but new text file is created for every unique string of letters, using up more space. The text files of stored words are 
found in `stored`.

I recomend deleting all the text files in the `stored` folder before editing the `data.txt` file and running the
program again.

To run the program, run `Story Gan.py`.
