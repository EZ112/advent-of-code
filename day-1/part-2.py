import sys

def main():
    instruction = []
    with open(sys.argv[1]) as r:
        for text in r:
            instruction.append(text.replace('\n',''))

    curr = 50
    zeros = 0
    for rotate in instruction:
        prev=curr
        if(rotate[0]=='L'):
            left_rotate = int(rotate[1:], base=10)
            if(left_rotate>100):
                zeros+=left_rotate//100
                left_rotate%=100
            
            curr-=left_rotate
        else:
            right_rotate = int(rotate[1:], base=10)
            if(right_rotate>100):
                zeros+=right_rotate//100
                right_rotate%=100

            curr+=right_rotate

        if(prev!=0 and (curr<0 or curr>100 or curr%100==0)):
            zeros+=1
        raw_curr = curr
        curr%=100

        print(f'curr zeros {rotate} -> {curr}({raw_curr}) : {zeros}')
    print('zeros:',zeros)

if __name__ == '__main__':
    main()
