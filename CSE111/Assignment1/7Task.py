def sum_list(user_list):
    global max_sum, max_lst
    lst_sum = sum(user_list)

    if lst_sum > max_sum:
        max_sum = lst_sum
        max_lst = user_list


times = int(input())
max_sum = 0
max_lst = []
for time in range(times):
    user_list = [int(num) for num in input().split()]
    sum_list(user_list)

print(max_sum)
print(max_lst)
