#Non Preemptive Priority Scheduling
process=[]
n=input("Enter no of process: ")
ct=[0]*n
tat=[]
wt=[]
for i in range(n):
	process.append([])
	process[i].append(raw_input("Enter process id: "))
	process[i].append(input("Enter arrival time: "))
	process[i].append(input("Enter burst time: "))
	process[i].append(input("Enter priority: "))
	print ''

for i in range(n):
	process[i].append(i)

process.sort(key = lambda process:process[1])


c=process[0][1]
for i in range(n):
	p=list(filter(lambda pr:pr[1]<=c and len(pr)==5,process))
	if p!=[]:
		p.sort(key = lambda p:p[3],reverse=True)
		c+=p[0][2]
		index=p[0][4]
		ct[index]=c
		process[index].append(1)

for i in range(n):
	tat.append(ct[i]-process[i][1])
	wt.append(tat[i]-process[i][2])


print "PID\tAT\tBT\t  priority\tCT\tTAT\tWt"
for i in range(n):
	print process[i][0],'\t',process[i][1],'\t',process[i][2],'\t\t',process[i][3],'\t',ct[i],'\t',tat[i],'\t',wt[i]

