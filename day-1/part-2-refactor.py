import sys

def calc(curr, rotation, direction, zeros):
    prev = curr
    if(rotation>100):
        zeros+=rotation//100
        rotation%=100

    curr = curr-rotation if direction =='L' else curr+rotation 

    if(prev!=0 and (curr<0 or curr>100 or curr%100==0)):
        zeros+=1
    curr%=100

    return curr, zeros


def main():
    instruction = []
    with open(sys.argv[1]) as r:
        for text in r:
            instruction.append(text.replace('\n',''))

    curr = 50
    zeros = 0
    for rotate in instruction:
        curr, zeros = calc(curr, int(rotate[1:], base=10), rotate[0], zeros) 
        print(f'{rotate} -> {curr} : {zeros}')

    print('zeros:',zeros)

if __name__ == '__main__':
    main()
