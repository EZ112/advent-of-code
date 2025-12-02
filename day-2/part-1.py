import sys

def main():
    ranges = []
    with open(sys.argv[1]) as r:
        ls = r.read().split(',')
        for i in ls:
            ranges.append(map(lambda x: int(x), i.split('-')))

    invalid_ids = []
    for start, end in ranges:
        for i in range(start, end+1):
            num_str = str(i)
            num_len = len(num_str)
            mid = num_len//2

            left=0
            right=mid
            is_invalid = True
            while(right<num_len):
                if(num_str[left]!=num_str[right]):
                    is_invalid = False
                left+=1
                right+=1

            if(is_invalid and num_len%2==0):
                print(i)
                invalid_ids.append(i)
    
    print('sum:', sum(invalid_ids))

if __name__ == "__main__":
    main()
