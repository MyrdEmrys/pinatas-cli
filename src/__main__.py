import sys
from .classmodule import Pinatas

def main():
    args = sys.argv[1:]
    pinatas =  Pinatas()
    pinatas.candies = args

    print(pinatas.get_max_amount())

if __name__ == '__main__':
    main()
