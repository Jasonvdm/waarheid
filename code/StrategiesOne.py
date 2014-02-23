import Util


# Replace "full" with "full of."
def applyFullContext(sentence):
	# Minus one indexing for lookahead.
	for i in xrange(len(sentence) - 1):
		word = sentence[i][0]
		next_word = sentence[i + 1][0]
		# If "full" is in the sentence, and it's not already "full of."
		if word == 'full' and next_word != 'of':
			sentence = sentence[:i] + ('of', 'P') + sentence[i:]
	return sentence

# Replace "from is" with "from this is." Afrikaans doesn't always include "this."
def applyFromContext(sentence):
	# Minus one indexing for lookahead.
	for i in xrange(len(sentence) - 1):
		word = sentence[i][0]
		next_word = sentence[i + 1][0]
		# If we have "from is", change it to "from this is."
		if word == 'from' and next_word == 'is':
			sentence = sentence[:i] + ('this', 'ADJ') + sentence[i:]
	return sentence

