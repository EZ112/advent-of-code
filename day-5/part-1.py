import sys

def main():
    ranges = []
    avail_ids = []
    with open(sys.argv[1]) as r:
        section = r.read().replace('\n','x').split('xx')
        ranges = section[0].split('x')
        avail_ids = section[1].split('x')
        avail_ids.pop()

    ranges = list(map(lambda i: list(map(lambda x: int(x),i.split('-'))), ranges))
    avail_ids= list(map(lambda i: int(i), avail_ids))

    count = 0
    for i in avail_ids:
        for left, right in ranges:
            if(i>=left and i<=right):
                count+=1
                break
    print(count)


if __name__ == "__main__":
    main()
