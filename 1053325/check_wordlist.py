f = open("wordlist.txt", "r")
wordlist = [line.strip() for line in f]
f.close()
candidate_list = list()

for candidate in wordlist:
	#print(candidate)
	sort_candidate = [c for c in candidate]
	sort_candidate.sort()
	candidate_list.append(sort_candidate)
for i in range(len(candidate_list)):
	word = candidate_list[i]
	compare = list()
	if i == 0:
		compare = candidate_list[i+1:]
	elif i == len(candidate_list)-1:
		compare = candidate_list[0:i]
	else:
		compare = candidate_list[0:i]+candidate_list[i+1:]
	if word in compare:
		print("have same sort_word")
		print(i)