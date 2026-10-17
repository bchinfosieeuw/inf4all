def compact(lst: list[object]) -> None:
    """
    Remove falsy items such as False, 0 or ''.
    newlist = []
    for i in range(len(lst)):
        if lst[i]!=False and lst[i]!=0 and lst[i]!='':
            newlist.append(lst[i])
    #print(newlist)
    
#compact([0])
#compact([1, 2, 3, 4, 5])
#compact([0, 1, 2, 3, 4, 5])