
# List Comprehension

## Nested For loop + if 문


case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

result = [i+j for i in case_1 for j in case_2 if not (i==j)]

# print(result)

# >>> ['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']

result.sort()
print(result)

# >>> ['AD', 'AE', 'BA', 'BD', 'BE', 'CA', 'CD', 'CE']


## split + list Comprehension

# words = 'The quick brown fox jumps over the lazy dog'.split()  # 이렇게 쓰는게 코드 길이가 짧아지네 
words = 'The quick brown fox jumps over the lazy dog'
# print(words)

words = words.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

for i in stuff:
    print(i)