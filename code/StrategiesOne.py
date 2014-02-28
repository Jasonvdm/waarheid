import Util


# Replace "full" with "full of."
def applyFullContextRule(sentence):
	new_sentence = []
	new_sentence.append(sentence[0])
	# Minus one indexing for lookahead.
	for i in xrange(1,len(sentence)-1):
		new_sentence.append(sentence[i])
		word = sentence[i][0]
		prev_word = sentence[i - 1]
		next_word = sentence[i+1]
		if word == 'full' and next_word[1] == 'N' and prev_word[1] == 'V':
			new_sentence.append(('of', 'P'))
	new_sentence.append(sentence[-1])
	return new_sentence

# Replace "from is" with "from this is." Afrikaans doesn't always include "this."
def applyFromContextRule(sentence):
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

def applyQuestionContextRule(sentence):
	new_sentence = []
	# Minus one indexing for lookahead.
	for i in xrange(len(sentence) - 1):
		new_sentence.append(sentence[i])
		word = sentence[i][0]
		next_word = sentence[i + 1][0]
		# Add do or does between question word and pronoun."
		if sentence[i][1] == 'Q':
			if next_word in ['you','I','we']:
				new_sentence.append(('do', 'V'))
			else:
				new_sentence.append(('does', 'V'))
	new_sentence.append(sentence[-1])
	return new_sentence
