import Util


# Replace "full" with "full of."
def applyFullContext(sentence):
	new_sentence = []
	# Minus one indexing for lookahead.
	for i in xrange(len(sentence) - 1):
		new_sentence.append(sentence[i])
		word = sentence[i][0]
		next_word = sentence[i + 1][0]
		# If "full" is in the sentence, and it's not already "full of."
		if word == 'full' and next_word != 'of':
			new_sentence.append(('of', 'P'))
	new_sentence.append(sentence[-1])
	return new_sentence

# Replace "from is" with "from this is." Afrikaans doesn't always include "this."
def applyFromContext(sentence):
	new_sentence = []
	# Minus one indexing for lookahead.
	for i in xrange(len(sentence) - 1):
		new_sentence.append(sentence[i])
		word = sentence[i][0]
		next_word = sentence[i + 1][0]
		# If we have "from is", change it to "from this is."
		if word == 'from' and next_word == 'is':
			new_sentence.append(('this', 'ADJ'))
	new_sentence.append(sentence[-1])
	return new_sentence

