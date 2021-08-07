list_with_script = [55, 36, 59, 129, 59]
total_weight = 0
for element in list_with_script:
###Check through list_with_script	
	total_weight = total_weight + element
	print(total_weight)
	if total_weight > 200:
		print("Elevator is full")
		break