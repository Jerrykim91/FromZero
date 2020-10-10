# Enumerate & Zip


## list comprehension + zip

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)


# outut
# (1, 10, 100) (2, 20, 200) (3, 30, 300)

print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])


# outut
# [111, 222, 333]




## enumerate + zip

a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']


for i,(a,b) in enumerate(zip(a_list,b_list)):
    print(i,":" , a, b)



# outut
# 0 : a1 b1
# 1 : a2 b2
# 2 : a3 b3