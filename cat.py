# documentation: https://docs.python.org/3/library/argparse.html

import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="a simple python implementation of the UNIX cat command",
    epilog="built by GDSC Ashesi. \
            You are welcome to modify and reuse this code as needed"
)

parser.add_argument('filename', help="the file to be displayed")  # use this for test-allow multiple files to be read, you'll need to know about Python's kwargs and args
parser.add_argument('-n', '--number', help="the number of bytes to read from the file", type=int)
parser.add_argument('-l', '--lines', help="the number of lines you want to read from the file.", type=int)



# -n and -l are mutually exclusive groups, i.e. you shouldn't be able to specify both AT THE SAME TIME
# so we'll ad them as mutually exclusive groups

# group = parser.add_mutually_exclusive_group()
# group.add_argument()  # copy the parser.add argument here and modify it to group.


# parsing the created arguments for use:
args = parser.parse_args()


if args.number:
    with open(args.filename, 'r') as fp:
        print(fp.read(args.number))  # if type is not specified in argument, you'll have to convert the number to an int first before using it in read
elif args.lines:
    # we can also do fp.readlines(args.lines), but it returns a list, and we will 
    # still need to loop
    with open(args.filename, 'r') as fp:
        for i in range(args.lines):
            print(fp.readline())
else:
    with open(args.filename, 'r') as fp:
        print(fp.read())



# if __name__ == '__main__':
#     # call function we will refactor into