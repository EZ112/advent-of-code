import sys

def main():
    banks = []
    with open(sys.argv[1]) as r:
        banks = r.read().split('\n')
        banks.pop()

    max_jolts = []
    for bat in banks:
        jolt = 0
        left = 0
        right = left+1
        while left<right:
            while right<len(bat):
                jolt = max(jolt, int(bat[left]+bat[right], base=10))
                right+=1

            left+=1
            if(left<len(bat)):
                right = left+1
        max_jolts.append(jolt)
    print(max_jolts) 
    print(sum(max_jolts))


if __name__ == "__main__":
    main()
