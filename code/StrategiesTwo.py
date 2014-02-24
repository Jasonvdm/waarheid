import Util

def applyDoubleNegativeRule(translation):
	if Util.isNegative(translation[-1][0]):
		return translation[:-1]
	return translation

def applyQuestionRule(translation):
	if translation[0][1] == "Q":
		word = translation[-1][0]
		translation[-1] = (word+"?",translation[-1][1])
	return translation

def applyNounVerbRule(translation):
	for i in xrange(len(translation)-1):
		currTup = translation[i]
		nextTup = translation[i+1]
		if currTup[1] == 'V' and nextTup[1] in ['N','PN']:
			translation[i] = nextTup
			translation[i+1] = currTup
	return translation