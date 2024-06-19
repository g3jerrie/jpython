from One import First
from One.Two import Second

# This if condition is required only for reviewer perspective. Not mandatory for compiler.
if(__name__ == '__main__'):
    print("Started from Main...")
    First.doOne()
    print("Executed doOne...")
    Second.doTwo()
    print("Executed doTwo...")
