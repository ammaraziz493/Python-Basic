def greet(fx):
    def mfx(*args, **kwargs):  # *args is for all argument for tuple, **kwargs is for all arguments in dictonary

        print("Good Morning")  # print before the actual fuction
        fx(*args, **kwargs)
        print("Thank for using this function")  # Print after the actual function

    return mfx


@greet
def hello():
    print("Hello World")


@greet
def add(a, b):
    print(a + b)


hello()
(add(1, 2))

