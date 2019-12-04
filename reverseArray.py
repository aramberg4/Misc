# script reverses an array in place

def main(array):
	if len(array)/2 %2 != 0:
		#odd
		midpoint = len(array) // 2 #floor
		i=1
		while i <= midpoint:
			tmp = array[midpoint+i]
			array[midpoint+i] = array[midpoint-i]
			array[midpoint-i] = tmp
			i+=1
	else:
		#even
		runner1 = len(array) // 2 - 1#floor
		runner2 = len(array) // 2 #floor
		while runner2 < len(array):
			tmp = array[runner2]
			array[runner2] = array[runner1]
			array[runner1] = tmp
			runner1 -= 1
			runner2 += 1

	return array

if __name__ == "__main__":
	arrayOdd = [0,1,2,3,4]
	arrayEven = [0,1,2,3]
	print("testing odd array...")
	newArray1 = main(arrayOdd)
	for elem in newArray1:
		print(str(elem))
	print("testing even array...")
	newArray2 = main(arrayEven)
	for elem in newArray2:
		print(str(elem))
