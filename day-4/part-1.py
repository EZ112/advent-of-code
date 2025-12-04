import sys

def main():
    shelve = []
    with open(sys.argv[1]) as r:
        for row in r:
            shelve.append(row.replace('\n', ''))

    pickable = 0
    for row_idx, row in enumerate(shelve):
        for col_idx, col in enumerate(row):
            adjecent = [[row_idx-1,col_idx-1], [row_idx-1, col_idx], [row_idx-1, col_idx+1],
                        [row_idx, col_idx-1], [row_idx, col_idx+1],
                        [row_idx+1, col_idx-1], [row_idx+1, col_idx], [row_idx+1, col_idx+1]]

            if(shelve[row_idx][col_idx]!='@'):
                continue

            print('check:', row_idx, col_idx)
            count=0
            for i,j in adjecent:
                if(i<0 or j<0 or i>=len(shelve) or j>=len(row)):
                    continue
                if(shelve[i][j] == '@'):
                    count+=1
                print(f'{i,j}', end=',')
            print(' count:', count)
            if(count<4):
                pickable+=1

    print(pickable)
if __name__ == "__main__":
    main()
