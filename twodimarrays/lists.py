



mylist = [1,2,3,4,5,6,7,8,9]
print(mylist)
mylist[3] = 99
print(mylist)


target = 88

if target in mylist:
    print(f"{target} is in list")
else:
    print(f"{target} is not in list")


newlist = [item*2 for item in mylist if item%2 == 0] 

print(mylist)
print(newlist)


arr = [1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1] = arr[i]

print(arr)
