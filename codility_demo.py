my_list = [ -1,-3]
print(type(my_list))
print(dir(my_list))

def min_elm_list(my_list):
    my_list=list(set(my_list))
    print(my_list)
    my_list.sort()  # type: object
    print(my_list)
    if my_list[0] >= 0:
        minimum = my_list[0]+1
    else:
        minimum = 1
        print(minimum)
    for i in my_list[1:]:
        if i == minimum:
            minimum = minimum+1
        else:
            break
    print(minimum)
    pass
min_elm_list(my_list)
