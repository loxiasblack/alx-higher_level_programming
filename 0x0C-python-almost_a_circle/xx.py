#!/usr/bin/python3
class A:
    """Hello this is just for a test"""
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello" + self.name)

class B(A):
    pass

if __name__ == "__main__":
    x = A("PX-0")
    Y = B("PX-5")

    Y.say_hi()
