# Write your solution here
students_on_course = int(input("How many students on the course? "))
desired_size = int(input("Desired group size? "))
INTgroups_number = int(students_on_course // desired_size)
left = int(students_on_course % desired_size)
if left>0:
    print (f"Number of groups formed: {INTgroups_number+1}")

if left==0:
    print (f"Number of groups formed: {INTgroups_number}")