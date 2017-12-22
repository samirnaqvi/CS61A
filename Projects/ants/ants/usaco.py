b=[6, 10, 23, 19, 2401, 506]

max=0;
count=0;


def count_paths(a)
for i in range(len(a)-1):
	if(can_add(a[i],a[i+1])):
		b=[a[i]+a[i+1]]
		b.extend(a[i+2:])
		return 1+count_paths(b)
	count_paths(a[i],a[i+1:])

	count =0;
	for x in b[1:]:

def can_add(a,b):
	while(a!=0 or b!=0):
		if(a%10+b%10>=9):
			return False
		a=a//10
		b=b//10
	return true

1 2 3 4 5

3 4 5