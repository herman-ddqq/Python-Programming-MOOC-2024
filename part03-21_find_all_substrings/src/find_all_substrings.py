# Write your solution here
word = input ("Please type in a word: ")
character = input ("Please type in a character: ")
while True:
    index = word.find(character)
    if index <= len(word)-3 and index != -1:
        print(word[index:index+3])
        word = word[index+1:]
    else:
        break
        