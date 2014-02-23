import Util
import sys
import re

def baseLineTranslations(fileName):
	corpus_file = open("../corpus/"+fileName, 'r')
	dictionary = Util.readDict()
	for line in corpus_file:
		translation = []
		wordTypes = []
		for word in line.split():
			matches = re.findall("(\W*)(\w+)(\W*)",word)
			if matches[0][0] == "\'":
				trans = dictionary[matches[0][0]+matches[0][1]]
				translation.append(trans[0]+matches[0][2])
				wordTypes.append(trans[1])
			else:
				trans = dictionary[matches[0][1]]
				translation.append(matches[0][0]+trans[0]+matches[0][2])
				wordTypes.append(trans[1])
		print " "
		print line
		print "Translation: "+" ".join(translation)
		print "Word Types:"+" ".join(wordTypes)
		print "---------------------------------------------------------"

if __name__ == "__main__":
	if len(sys.argv) < 2: baseLineTranslations("dev_set.txt")
	else: baseLineTranslations(str(sys.argv[1]))