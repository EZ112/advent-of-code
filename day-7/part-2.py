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
    for i in range(row_len):
        for j in range(col_len):
            if manifolds[i][j] != '^':
                if i>0 and (manifolds[i-1][j] == 'S' or manifolds[i-1][j] == '|'):
                    manifolds[i][j] = '|'
            else:
                manifolds[i][j-1] = '|'
                manifolds[i][j+1] = '|'
        
    paths_count = [0 for _ in range(col_len)]
    for i in range(row_len-1, -1, -1):
        for j in range(col_len-1, -1, -1):
            print(manifolds[i][j], end='')
            if i==row_len-1 and manifolds[i][j]=='|':
                paths_count[j]=1
            if(manifolds[i][j]=='^'):
                paths_count[j] = paths_count[j-1] + paths_count[j+1]
        print()
    print(max(paths_count))
    
    

if __name__ == "__main__":
    main()
