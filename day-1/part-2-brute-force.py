import sys

def main():
    instruction = []
    with open(sys.argv[1]) as r:
        for text in r:
            instruction.append(text.replace('\n',''))

    curr = 50
    zeros = 0
    for rotate in instruction:
        num = int(rotate[1:], base=10)
        if(rotate[0]=='L'):
            for _ in range(num):
                curr-=1
                if(curr<0):
                    curr+=100
                if(curr == 0):
                    zeros+=1
        else:
            for _ in range(num):
                curr+=1
                if(curr>=100):
                    curr-=100
                if(curr == 0):
                    zeros+=1
                
        print(f'{rotate} -> {curr}: {zeros}')
    print('zeros: ', zeros)

if __name__ == "__main__":
    main()
