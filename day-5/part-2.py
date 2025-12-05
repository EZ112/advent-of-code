import sys

def main():
    ranges = []
    with open(sys.argv[1]) as r:
        section = r.read().replace('\n','x').split('xx')
        ranges = section[0].split('x')

    ranges = list(map(lambda i: list(map(lambda x: int(x),i.split('-'))), ranges))
    ranges.sort(key=lambda x: x[0])

    curr = 0
    while curr<len(ranges)-1:
        left, right = ranges[curr]
        next_left, next_right = ranges[curr+1]
        if(right>=next_left):
            ranges[curr] = [min(left, next_left), max(right, next_right)]
            del ranges[curr+1]
        else:
            ranges[curr] = [left, right]
            curr+=1
        print(ranges)
    
    total = 0
    for left, right in ranges:
        total+=right-left+1
    print(total)



if __name__ == "__main__":
    main()
