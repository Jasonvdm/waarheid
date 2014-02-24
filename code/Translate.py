import Util
import sys
import re
import StrategiesOne
import StrategiesTwo

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
				translation.append((trans[0]+matches[0][2],trans[1]))
			else:
				trans = dictionary[matches[0][1]]
				translation.append((matches[0][0]+trans[0]+matches[0][2],trans[1]))
		translation = StrategiesOne.applyFullContext(translation)
		translation = StrategiesOne.applyFromContext(translation)
		translation = StrategiesTwo.applyDoubleNegativeRule(translation)
		translation = StrategiesTwo.applyQuestionRule(translation)
		translation = StrategiesTwo.applyNounVerbRule(translation)
		print ""
		print line
		transWords = ""
		for i in xrange(len(translation)):
			transWords += translation[i][0] + " "
		print transWords
		transTypes = ""
		for i in xrange(len(translation)):
			transTypes += translation[i][1] + " "
		print transTypes
		print "---------------------------------------------------------"

if __name__ == "__main__":
	if len(sys.argv) < 2: baseLineTranslations("dev_set.txt")
	else: baseLineTranslations(str(sys.argv[1]))