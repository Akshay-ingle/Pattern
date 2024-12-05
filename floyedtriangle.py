rw=int(input('please enter amount of rows:'))
nb=1
print('floyeds triangle')
for i in range(1,rw+1):
    for j in range(1,i+1):
        print(nb,end='')
        nb=nb+1
    print()    