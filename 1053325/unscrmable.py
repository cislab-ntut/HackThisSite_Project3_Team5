
f = open("wordlist.txt", "r")
wordlist = [line.strip() for line in f]
f.close()
candidate_list = list()

for candidate in wordlist:
	#print(candidate)
	sort_candidate = [c for c in candidate]
	sort_candidate.sort()
	candidate_list.append((sort_candidate, candidate))
print("enter the scrmable words")
input_str = list()
for i in range(10):
	string = input()
	sort_string = [c for c in string]
	sort_string.sort()
	input_str.append(sort_string)
result = list()
for i in input_str:
	for j in candidate_list:
		if i == j[0]:
			result.append(j[1])
print (','.join(result))