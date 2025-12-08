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
 
    indices = {0:{manifolds[0].index('S')}}
    idx = 0
    count = 0
    for i in range(len(manifolds)):
        for j in indices[idx]:
            if(manifolds[i][j]=='^'):
                count+=1
                if(i not in indices):
                    indices[i] = set(indices[idx])
                indices[i].add(j-1)
                indices[i].add(j+1)
                indices[i].remove(j)

                manifolds[i][j-1] = '|'
                manifolds[i][j+1] = '|'
                idx=i
            elif manifolds[i][j]!='S':
                manifolds[i][j] = '|'
        print(indices[idx])

    for i in range(len(manifolds)):
        for j in range(len(manifolds[i])):
            print(manifolds[i][j], end='')
        print()

    print(indices)
    print(count)

if __name__ == "__main__":
    main()
