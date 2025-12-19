import sys

def main():
    manifolds = []
    with open(sys.argv[1]) as r:
        rows = r.read().split('\n')
        rows.pop()
        for i in rows:
            data = []
            for j in i:
                data.append(j)
            manifolds.append(data)

    row_len = len(manifolds)
    col_len = len(manifolds[0])

    count = 0
    for i in range(row_len):
        for j in range(col_len):
            if manifolds[i][j] != '^':
                if i>0 and (manifolds[i-1][j] == 'S' or manifolds[i-1][j] == '|'):
                    manifolds[i][j] = '|'
            else:
                manifolds[i][j-1] = '|'
                manifolds[i][j+1] = '|'
            if i>0 and manifolds[i-1][j] == '|' and manifolds[i][j] == '^':
                count+=1

    for i in range(row_len):
        for j in range(col_len):
            print(manifolds[i][j], end='')
        print()
    print(count)


if __name__ == "__main__":
    main()
