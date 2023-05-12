arr=[5,4,4,2,2,1,8]
result=[]
while(True):
    re = [x for x in arr if x>0]

    if (len(re) != 0):
        result.append(len(re))
    else:
        break
    for x in range(len(arr)):

        arr[x]=arr[x]-int(min(re))

print(result)



