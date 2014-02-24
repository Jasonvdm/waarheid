def readDict():
    dictionary = dict()
    dict_file = open("../corpus/dictionary.txt", 'r')
    for line in dict_file:
        endWord = line.find(":")
        dictionary[line[:endWord]] = (line[endWord + 2:line.find(",")],line[line.find(",")+1:line.find(")")])
    dict_file.close()
    return dictionary

def isNegative(word):
	neg_words = ['no', 'not', 'none', 'nobody', 'nothing', 'neither', 'nowhere', 'never']
	word = word.lower()
	if word in neg_words: return True
	return False

def countVerbs(sentence):
	count = 0
	for word in sentence:
		if word[0] == 'V': count += 1
	return count

def countNouns(sentence):
	count = 0
	for word in sentence:
		if word[0] == 'N': count += 1
	return count