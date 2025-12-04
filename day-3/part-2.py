import sys

def main():
    banks = []
    with open(sys.argv[1]) as r:
        banks = r.read().split('\n')
        banks.pop()

    banks = map(lambda x: list(x), banks)
    max_bat = 12
    total_jolts = 0
    for bat in banks:
        next_idx = 0
        max_jolts = [0 for _ in range(max_bat)]
        max_jolts_idx = 0
        print('Battery: ',''.join(bat))
        print('next_idx', end=': ')
        while max_jolts_idx<max_bat:
            curr_idx = next_idx
            while curr_idx<len(bat):
                jolt = int(bat[curr_idx], base=10)
                if(len(bat)-curr_idx+max_jolts_idx>=12 and max_jolts[max_jolts_idx]<jolt):
                    max_jolts[max_jolts_idx] = jolt
                    next_idx = curr_idx+1
                curr_idx+=1
            print(next_idx, end=',')
            max_jolts_idx+=1
        print()
        print('max_jolts',max_jolts)
        total_jolts+=int(''.join(map(lambda x:str(x),max_jolts)), base=10)
    print(total_jolts)

if __name__ == "__main__":
    main()
