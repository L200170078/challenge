data=[4,4,6,7,9,10,12,20,40,42]

def hasPairWithSum(result, data):
	low=0
	hi=len(data)-1	

	while low < hi:
		if (data[low] + data[hi]) is result:
			return (str(True)+" : "+str(data[low]) + " + " + str(data[hi]) + " is " + str(result))
		elif (data[low]+data[hi]) < result:
			low+=1
		elif (data[low]+data[hi]) > result:
			hi-=1

	return False

print(data)
print(hasPairWithSum(47, data))