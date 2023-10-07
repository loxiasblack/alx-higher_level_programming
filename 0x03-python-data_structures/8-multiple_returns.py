#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    for i in range(len(sentence)):
        i += 1
    return (i, sentence[0])
