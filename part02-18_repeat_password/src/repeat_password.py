# Write your solution here
code = input("Password: ")
while True:
  repeat = input("Repeat password: ")
  if repeat==code:
    print("User account created! ")
    break
  print ("They do not match!")
