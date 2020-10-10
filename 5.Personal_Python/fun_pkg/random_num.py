# random_num 함수 
history_log = """
# 진행과정 

# tmp = list()
# print(tmp)

tmp = list(range(1,100))
# print(random.shuffle( tmp ))
random.shuffle( tmp )
# print(tmp)


number = [] 
x = 50
cnt = 0
for num in tmp:
    cnt += 1 
    if cnt <= x : 
        # print(num)
        number.append(num)
        pass 
print('Count : %s' % len(number), number)
"""
# print(history_log)



def step_num():
    pass

def random_num(x):
    
    import random 
    tmp = list(range(1,100))
    random.shuffle( tmp )
    # print('log1')
    x = int(x)
    cnt = 0
    number = list()
    
    for num in tmp:
        cnt += 1 
        # print('log2')
        if cnt <= x : 
            # print(num)
            number.append(num)
            pass

    # print('Count : %s' % len(number), number)
    print('Count : %s' % len(number))
    return number

# a = random_num(20)

# print( a )