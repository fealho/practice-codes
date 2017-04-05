import operator
from collections import Counter

#Solving problem: https://www.urionlinejudge.com.br/judge/en/problems/view/1737

#param: line: a string
#return: a Counter tuple([(digram, its absolute frequency)], total number of digrams)
def digramFrequencyLine(line):
	digrams = Counter([ line[i-1] + line[i] for i in range(1, len(line) ) ])
	return (digrams, len(line) - 1)


#param: lines: a list of strings
#return: (Counter dictionary {digram: its absolute frequency}, number of diagrams)
def digramFrequency(lines):
	total_digram_dict, total_num_digrams = digramFrequencyLine(lines[0])
	
	for i in range(1, len(lines)):
		digram_dict, num_digrams = digramFrequencyLine(lines[i-1][-1] + lines[i]) 
		total_num_digrams += num_digrams
		total_digram_dict.update(digram_dict)
	
	return (total_digram_dict, total_num_digrams)


#param: lines: a list of stirngs
#		numFrequencies: num of most frequent digrams to be shown
#return: list of most frequent digrams, sorted lexicograficaly in case of draw,
#		 with their absolute and relative frequencies
def topFrequencies(lines, numFrequencies):
	all_frequencies, num_diagrams = digramFrequency(lines)
	top_frequencies = all_frequencies.most_common()
	top_frequencies = sorted( [(-count, digram) for digram, count in top_frequencies])
	top_frequencies = [(digram, -count) for count, digram in top_frequencies]
	return [ ( digram, count, float(count)/num_diagrams ) for digram, count in top_frequencies ] 


#-------------------------MAIN------------------------------------

if __name__ == "__main__":
	lines = input()
	while lines != 0:
		all_lines = [raw_input() for line in range(lines)]
		freq = topFrequencies(all_lines, 5)
		for i in range(5):
			print "%s %i %.6f" % (freq[i][0], freq[i][1], freq[i][2]) 
		lines = input()
		print ""
