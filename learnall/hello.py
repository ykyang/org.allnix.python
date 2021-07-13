# Basic package loading and using
import os

import learnall
import learnall.util

print('Hello World from {}'.format(os.path.basename(__file__)))

print(learnall.hello())
print(learnall.util.hello())