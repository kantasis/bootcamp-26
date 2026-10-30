array = [13,15,100,25,90,0,9, 11]

for i in range(0,len(array),2):
    print('Normal:', array[i])
    #print('Reversed:',array[-(i+1)])
    print(10*'-')

print(10*'#')
for i in range(len(array),0,-2):
    print('Reversed:',array[i-1])
    print(10*'-')

