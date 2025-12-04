import sys

def main():
    shelve = []
    with open(sys.argv[1]) as r:
        for row in r:
            shelve.append(row.replace('\n', ''))

    shelve = list(map(lambda x: list(x), shelve))
    picked = 0
    picked_idx = []
    while True:
        pickable = 0
        for row_idx, row in enumerate(shelve):
            for col_idx, col in enumerate(row):
                adjecent = [[row_idx-1,col_idx-1], [row_idx-1, col_idx], [row_idx-1, col_idx+1],
                            [row_idx, col_idx-1], [row_idx, col_idx+1],
                            [row_idx+1, col_idx-1], [row_idx+1, col_idx], [row_idx+1, col_idx+1]]

                if(shelve[row_idx][col_idx]!='@'):
                    continue

                count=0
                for i,j in adjecent:
                    if(i<0 or j<0 or i>=len(shelve) or j>=len(row)):
                        continue
                    if(shelve[i][j] == '@'):
                        count+=1
                if(count<4):
                    picked_idx.append([row_idx, col_idx])
                    pickable+=1

        if(len(picked_idx)<1):
            break

        print('pickable: ',pickable)
        for i,j in picked_idx:
            shelve[i][j] = 'x'
            picked+=1
        picked_idx = []

        for row in (list(map(lambda x: ''.join(x),shelve))):
            print(row)

    print(picked)

if __name__ == "__main__":
    main()
