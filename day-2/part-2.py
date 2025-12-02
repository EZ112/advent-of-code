import sys

def main():
    ranges = []
    with open(sys.argv[1]) as r:
        ls = r.read().split(',')
        for i in ls:
            ranges.append(map(lambda x: int(x), i.split('-')))

    invalid_ids = []
    for start, end in ranges:
        print(f'range: {start}-{end}')
        for i in range(start, end+1):
            num_str = str(i)
            num_len = len(num_str)

            step = 1
            while step<num_len:
                total=0
                for j in range(0, num_len-step, step):
                    curr_num = int(num_str[j:j+step], base=10)
                    next_num = int(num_str[j+step:j+step+step], base=10)
                    total += curr_num+next_num if curr_num == 0 or next_num == 0 else abs(curr_num-next_num)
                    print(f'{curr_num}, {next_num}-> {total}')

                if(total==0):
                    invalid_ids.append(i)
                    break
                step+=1

    invalid_ids.sort()
    print(invalid_ids)
    print('sum:', sum(invalid_ids))

if __name__ == "__main__":
    main()
