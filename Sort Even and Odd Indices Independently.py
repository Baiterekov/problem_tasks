nums = [36,45,32,31,15,41,9,46,36,6,15,16,33,26,27,31,44,34]
odd_arr = []
even_arr = []
result_arr = []
n=0
for i in nums:
	if i%2==0:
		even_arr.append(i)
	else:
		odd_arr.append(i)
even_arr.sort()
odd_arr.sort()
if len(odd_arr)>len(even_arr):
	n = len(odd_arr)
else:
	n = len(even_arr)
for i in range(0, n):
	try:
		result_arr.append(even_arr[i])
	except:
		continue
	try:
		result_arr.append(odd_arr[i])
	except:
		continue
print(even_arr)
print(odd_arr)
print(result_arr)
		