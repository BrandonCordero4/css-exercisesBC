def recursive_list_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return recursive_list_sum(lst[1:]) + lst[0] 

print(recursive_list_sum([1,2,3,4]))