# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
data = open('birth_places_train.tsv').read()
data = list(data.encode('utf-8').decode('ascii', errors='ignore').split('\n'))
ys = [d.split('\t') for d in data]
ys = ys[:-1]
num_london = sum([1 if s[1] == 'London' else 0 for s in ys])
accuracy = num_london / len(ys)
print("London baseline: {}%".format(accuracy*100))
