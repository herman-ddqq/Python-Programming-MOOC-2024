# Write your solution here
WORDS = ""
prev_word = False

while True:
    word = input("Please type in a word:  ")

    if word == "end":
        break

    if word == prev_word:
        break
    
    WORDS += word + " "
    prev_word = word

print (WORDS)

