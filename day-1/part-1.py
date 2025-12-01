import sys

def main():
    instruction = []
    with open(sys.argv[1]) as r:
        for text in r:
            instruction.append(text.replace('\n',''))

    curr = 50
    zeros = 0
    for rotate in instruction:
        if(rotate[0]=='L'):
            left_rotate = int(rotate[1:], base=10)
            curr-=left_rotate
        else:
            right_rotate = int(rotate[1:], base=10)
            curr+=right_rotate
        curr%=100

        if(curr==0):
            zeros+=1
        print(f'{rotate} -> {curr}')
    print('zeros:',zeros)

if __name__ == '__main__':
    main()
