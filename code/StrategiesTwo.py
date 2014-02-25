import Util
import string

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

def applySecondVerbRule(translation):
	if Util.countVerbs(translation) > 1 and len(translation)>6:
		firstVerb = -1
		secondVerb = -1
		for i in xrange(len(translation)):
			if translation[i][1] == 'V':
				if firstVerb == -1:
					firstVerb = i
				else:
					secondVerb = i
		insertIndex = 0
		startIndex = secondVerb
		if translation[secondVerb-1][1] in ['N','PN']:
			startIndex = secondVerb-1
		for i in reversed(xrange(startIndex)):
			if '\"' in translation[i][0] or ',' in translation[i][0] or ':' in translation[i][0]:
				print translation[i][0]
				insertIndex = secondVerb
			if translation[i][1] in ['V','N','PN'] and insertIndex == 0:
				insertIndex = i + 1
		newTranslation = []
		for i in xrange(len(translation)):
			if i == insertIndex:
				newTranslation.append(translation[secondVerb])
			if i == secondVerb: continue
			newTranslation.append(translation[i])
		return newTranslation
	return translation

def applyStillContextRule(translation):
	iIndex = -1
	word = ""
	for i in xrange(len(translation)):
		if translation[i][0] == "still" and translation[i-1][0] not in ['is','are'] and translation[i+1][1] != 'V':
			iIndex = i
			word = "is"
			if translation[i-1][0][-1] == 's':
				word = "are"
	newTranslation = []
	for i in xrange(len(translation)):
		if i == iIndex:
			newTranslation.append((word,'V'))
		newTranslation.append(translation[i])
	return newTranslation

def applyCapitalizationPeriodRule(translation):
	firstWord = translation[0][0]
	if firstWord[0] not in string.ascii_letters:
		newWord = firstWord[0] + firstWord[1].upper()
		if len(firstWord)> 2:
			newWord += firstWord[2:]
		firstWord = newWord
	else:
		firstWord = firstWord[0].upper() + firstWord[1:]
	translation[0] = (firstWord,translation[0][1])
	lastWord = translation[-1][0]
	if lastWord[-1] not in ['.','?','!']:
		lastWord += '.'
	translation[-1] = (lastWord,translation[-1][0])
	return translation