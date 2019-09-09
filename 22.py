def name_score(name):
        letters = list(name)
        letters = [ord(x) - 64 for x in letters]
        return sum(letters)

f = open('names.txt')

list_of_names = f.read()
list_of_names = list_of_names .split(',')
list_of_names = [x[1 :-1] for x in list_of_names]
list_of_names.sort()

scores = 0

for i in range(len(list_of_names)):
	scores += name_score(list_of_names[i]) * (i + 1)
print (scores)
