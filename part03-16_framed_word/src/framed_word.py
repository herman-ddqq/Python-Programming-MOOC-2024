# Write your solution here
string = input ("Word: ")
line1 = "*" * 30
line3 = line1

if len(string)%2==0:
    space_num = int((30-(len(string)+2))/2)
    space1 = space2 = " " * space_num
else:
    space_num = int((30-(len(string)+3))/2)
    space1 = " " * space_num
    space2 = " " * space_num + " "


print (line1)
print (f"*{space1}{string}{space2}*")
print (line3)

