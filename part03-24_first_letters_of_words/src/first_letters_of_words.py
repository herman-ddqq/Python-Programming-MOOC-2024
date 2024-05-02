# Write your solution here
sentence = input ("Please type in a sentence: ")
#sentence = "Cat loves milk "
space = " "
while True:
    index = sentence.find(space)
    if index != -1:
        print(sentence[0])
        sentence = (sentence[index+1:])
        continue
    if index == -1:
        print(sentence[0])
        break