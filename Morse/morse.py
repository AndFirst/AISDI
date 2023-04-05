import sys
from functions import encode_file

def main(argv):
    path = sys.argv[1]
    print(encode_file(path))

if __name__ == '__main__':
    main(sys.argv)