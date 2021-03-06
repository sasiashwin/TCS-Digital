arr=[6,3,2,5,1,2,9]
sum_list=[]
i=1
sum=arr[0]
while(i!=len(arr)):
	if(arr[i]>sum):
		sum+=arr[i]
	else:
		sum_list.append(sum)
		sum=0
		sum+=arr[i]
	i+=1
sum_list.append(sum)
print(max(sum_list))

