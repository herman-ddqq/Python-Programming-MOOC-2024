# Write your solution here
word = input ("Please type in a word: ")
character = input ("Please type in a character: ")
index = word.find(character)
if index < len(word)-2 and index != -1:
    print(word[index:index+3])
else:
    print("")