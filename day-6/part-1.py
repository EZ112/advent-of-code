import sys

def main():
    numbers = []
    operation = []
    with open(sys.argv[1]) as r:
        rows = r.read().split('\n')
        rows = list(map(lambda x: x.strip().split(' '), rows))
        rows.pop()

        for row in rows:
            data = list(filter(lambda x: x!='', row))
            if(data[0] in ['+', '*']):
                operation = data
            else:
                numbers.append(list(map(lambda x: int(x, base=10),data)))

    print(numbers)
    print(operation)
    totals = [0 for _ in range(len(numbers[0]))]
    for r_idx, row in enumerate(numbers):
        for c_idx,col in enumerate(row):
            if(r_idx==0):
                totals[c_idx] = 1 if operation[c_idx]=='*' else 0
            totals[c_idx] = totals[c_idx]*col if operation[c_idx]=='*' else totals[c_idx]+col
            print(f'({c_idx},{col})', end=',')
        print()
        print(totals)

    print(sum(totals))
        

    
if __name__ == "__main__":
    main()
