def hello(to="world"):
    print("hello,", to)


hello()  # Calling the hello function without any arguments, so it will use the default value "world"
name = input("What's your name? ")
hello(name)