file = open('text.txt','a')
for x in range(100, 1000):
    for y in range(100, 1000):
        print(x,'x',y,',', end =' ', sep = '', file=file)