reverse = ""
sentence = input("give me a sentence")
for i in range(len(sentence)):
    reverse += sentence[len(sentence)- 1-i]
print(reverse)