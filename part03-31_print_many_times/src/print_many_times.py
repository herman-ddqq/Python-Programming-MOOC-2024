# Write your solution here
def print_many_times(text, times):
    i = 1
    while i<=times:
        print(text)
        print()
        i +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("Roger", 3)