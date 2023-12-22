#!/usr/bin/python3
<<<<<<< HEAD
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
=======
""" Check """
from models.square import Square

s = Square(5)

try:
    s.size = "12"
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    s.size = [13]
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    s.size = 13.12
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    s.size = { 'id': 12 }
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

print("OK", end="")
>>>>>>> 09fe79ff10070d04a64fa0508d49d426766b683f
