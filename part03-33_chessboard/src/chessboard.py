# Write your solution here
def chessboard(x):
    ROW=1
    i=1
    while ROW<=x:
        if i<=x:
            print ("1", end="")
            i+=1
        if i<=x:
            print ("0", end="")
            i+=1
        else:
            ROW+=1
            print()
            i=1
            while ROW<=x:
                if i<=x:
                    print ("0", end="")
                    i+=1
                if i<=x:
                    print ("1", end="")
                    i+=1  
                else:
                    print()
                    i=1
                    ROW+=1
                    break
                

# Testing the function
if __name__ == "__main__":
    chessboard(3)
