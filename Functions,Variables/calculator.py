#Implementing a function that returns a value that was passed into it
def main():
    x=int(input("What's x?"))
    print("x squared is", square(x))

#Defining a function that returns the square of a number
def square(n):
    return n * n

main()