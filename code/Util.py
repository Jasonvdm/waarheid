def readDict():
    dictionary = dict()
    dict_file = open("../corpus/dictionary.txt", 'r')
    for line in dict_file:
        endWord = line.find(":")
        dictionary[line[:endWord]] = (line[endWord + 2:line.find(",")],line[line.find(",")+1:line.find(")")])
    dict_file.close()
    return dictionary