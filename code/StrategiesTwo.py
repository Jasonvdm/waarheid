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
		if currTup[1] == 'V' and nextTup[1] in ['N','PN'] and currTup[0] != 'is':
			translation[i] = nextTup
			translation[i+1] = currTup
	return translation

def applyQuoteTenseRule(translation):
	startQuote = -1
	endQuote = -1
	pastTense = Util.readDict("english_tenses")
	for i in xrange(len(translation)):
		if '\"' in translation[i][0]:
			if startQuote == -1:
				startQuote = i
			else:
				endQuote = i
	if startQuote == -1:
		return translation
	for i in xrange(len(translation)):
		if i in xrange(startQuote,endQuote+1):
			continue
		if translation[i][1] == 'V':
			translation[i] = pastTense[translation[i][0]]
	return translation