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

# range_mix_number 리스트 총 길이 정하고 random_number개의 출력 리스트 길이 
def random_num_all(range_mix_number,random_number):
    
    import random 
    range_mix_number = int(range_mix_number)
    tmp = list(range(1,range_mix_number))
    random.shuffle( tmp )
    # print('log1')
    random_number = int(random_number)
    cnt = 0
    number = list()
    
    for num in tmp:
        cnt += 1 
        # print('log2')
        if cnt <= random_number : 
            # print(num)
            number.append(num)
            pass

    # print('Count : %s' % len(number), number)
    print('Count : %s' % len(number))
    return number


def step_num():
    pass


# 1부터 100까지 x개의 출력 리스트 길이 
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
