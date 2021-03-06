s1="Morning"
s2="Bring"
s1=list(s1)
s2=list(s2)
i=0
cnt=0
while(i!=len(s1)):
	if(s1[i] not in s2):
		cnt+=1
	elif(s1.count(s1[i])!=s2.count(s1[i])):
		cnt+=abs((s1.count(s1[i])-s2.count(s1[i])))
		s1.remove(s1[i])
	i+=1

