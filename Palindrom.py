def swap(data, i,k):
	temp=data[i]
	data[i]=data[k]
	data[k]=temp
	return data

def cekProses(angka):
	if angka%2 is not 0:
		return (angka//2)+1
	else:
		return angka//2
	return None

def balik(data):
	lenKata=len(data)
	kanan=lenKata-1
	batas=cekProses(lenKata)
	kiri=0

	while kanan > 0:
		if kiri is batas:
				break
		for i in range(0,batas):
			swap(data, kanan, kiri)
			# print(x)
			# print(data)	
			kiri+=1
			kanan-=1
	return data

kata="IRAS"
listKata=list(kata)

data=balik(listKata)
final=""
for i in data:
	# final+""+str(i)
	final=final+""+i

if kata==final:
	print(kata)
	print("Setelah di Proses :", final)
	print("Kata Palindrom")
else:
	print(kata)
	print("Setelah di Proses : ",final)
	print(kata, " Bukan Kata Palindrom")
