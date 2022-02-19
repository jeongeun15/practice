T =int(input())

for i in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))
    n_list = list(set(num_list))
    
    max_count = 0 
    max_num = 0
    
    for n in n_list:
        if num_list.count(n) > max_count:
            max_count = num_list.count(n) 
            max_num = n
        elif num_list.count(n) == max_count:
            if n > max_num:
                max_num = n
            
    print(f'#{i} {max_num} {max_count}')    
            