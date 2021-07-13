import os

def hello():
    x = 'Hello World from learnall/{}'.format(os.path.basename(__file__))
    return x
