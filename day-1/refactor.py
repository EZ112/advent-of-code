import sys

def main():
    instruction = []
    with open(sys.argv[1]) as r:
        for text in r:
            instruction.append(text.replace('\n',''))

    curr = 50
    zeros = 0
    calc = lambda curr, rotation, direction: (
                max((curr-rotation if direction =='L' else curr+rotation) % 100, 0)
            )
    for rotate in instruction:
        curr = calc(curr, int(rotate[1:], base=10), rotate[0]) 

        if(curr==0):
            zeros+=1
        print(f'{rotate} -> {curr}')
    print('zeros:',zeros)

if __name__ == '__main__':
    main()
