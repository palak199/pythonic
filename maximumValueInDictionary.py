#get key with maximum value in dictionary
import operator
dictionary={"ram":34,"alice":80}
list_of_values=dictionary.values()
print(max(dictionary.items(),key=operator.itemgetter(1))[0])