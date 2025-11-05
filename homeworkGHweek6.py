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


# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase and split into words
words = sentence.lower().split()

# Create an empty dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the result
print("Word count:", word_count)



