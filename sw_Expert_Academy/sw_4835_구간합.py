T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    sum_min = 3000
    sum_max = 3
    nums = list(map(int, input().split()))
    for i in range(N-2):
        nums_sum = nums[i] + nums[i+1] + nums[i+2]
        if nums_sum >sum_max:
            sum_max = nums_sum
        if nums_sum < sum_min:
            sum_min = nums_sum
            
    answer = sum_max - sum_min
    print(f'#{tc} {answer}')
            
    