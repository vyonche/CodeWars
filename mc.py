#!/usr/bin/python
def get_middle(s):
    if(len(s) % 2 == 0):
        return "" + s[(int(len(s) / 2) - 1)] + s[(int(len(s) / 2))]
    else:
        return s[(int(len(s)/2))]
        
def main():
    print('Enter string: ')
    s = raw_input()
    print('Middle character is', get_middle(s))
    
main()
