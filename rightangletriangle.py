print('half pyramyd Pattern of star(*):')
n=int(input('enter the the number of rows:'))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()    