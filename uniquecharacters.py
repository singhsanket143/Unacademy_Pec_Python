def getUniqueCharacters(string):
	freq_map = {}
	for i in range(0, len(string)):
		if(freq_map.get(string[i]) == None):
			freq_map[string[i]] = 1
		else:
			freq_map[string[i]] += 1

	result = []
	for k in freq_map.keys():
		if(freq_map[k] == 1):
			result.append(k)

	return tuple(result)


string = "codechef"
result = getUniqueCharacters(string)
print(result)