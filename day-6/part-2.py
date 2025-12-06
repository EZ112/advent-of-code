import sys

def main():
    numbers = []
    operation = []
    with open(sys.argv[1]) as r:
        rows = r.read().split('\n')
        rows.pop()

        numbers = rows[:-1]
        operation = list(filter(lambda x:x!='',rows[-1].split(' ')))
        operation.reverse()

    print(numbers)
    print(operation)

    numbers_ordered_str = ['' for _ in range(len(numbers[0]))]
    for r_idx, row in enumerate(numbers):
        for c_idx, col in enumerate(row):
            numbers_ordered_str[c_idx]+=row[len(row)-1-c_idx]

    numbers_ordered = list(map(lambda x: int(x.strip(), base=10) if x.strip()!='' else 0, numbers_ordered_str))
    print(numbers_ordered)

    totals = list(map(lambda x: 1 if x == '*' else 0, operation))
    curr_idx = 0
    op_idx = 0
    while curr_idx<len(numbers_ordered):
        if(numbers_ordered[curr_idx]==0):
            op_idx+=1
        else:
            print(totals[op_idx], numbers_ordered[curr_idx], operation[op_idx])
            totals[op_idx] = totals[op_idx]*numbers_ordered[curr_idx] if operation[op_idx]=='*' else totals[op_idx]+numbers_ordered[curr_idx]
        curr_idx+=1
    print(totals)
    print(sum(totals))

        

    
if __name__ == "__main__":
    main()
