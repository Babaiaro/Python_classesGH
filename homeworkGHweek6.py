# Project:
#  Simple Word Counter. Write a program that asks the user for a sentence.
#  The program should then count the occurrences of each word in the sentence
#  and display the result as a dictionary.

# word_counter = input("Can you write there your sentence. \n:")
#
# x = len(word_counter)
# print(x)
#
# z=word_counter.count("z")
# print(z)

# sentences = []
# sentences = input("write here you sentence: ")
# for i, sentence in enumerate(sentences, 1):
#     print(i, sentence)
# # s = len(sentences)
# # print(s)

def countWord(input_string):
    d = {}
    for word in input_string:
        try:
            d[word] += 1
        except:
            d[word] = 1

    for k in d.keys():
        print ("%s: %d" % (k, d[k]))
print (countWord("Hello I am going to I with Hello am"))

