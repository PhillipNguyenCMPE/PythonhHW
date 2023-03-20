def sort_dictionary(d1):
	reversed=[]
	sorted_d1=sorted(d1.keys(), key=lambda key:d1[key][1])
	for key in sorted_d1:
		temp=(key,d1[key][0])
		reversed.append(temp)
	return reversed
