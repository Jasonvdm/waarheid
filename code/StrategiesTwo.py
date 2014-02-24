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