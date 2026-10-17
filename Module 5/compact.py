def compact(lst: list[object]) -> list[objects]:
    """
    Remove falsy items such as False, 0 or ''.
    
    >>> compact([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    
    >>> compact([1, 0, 3, 4, 5])
    [1, 3, 4, 5]
    
    >>> compact([1, 0, 0, 4, 5])
    [1, 4, 5]
    
    >>> compact([0])
    []
    """
    newlist = []
    for i in range(len(lst)):
        if lst[i]!=False and lst[i]!=0 and lst[i]!='' and lst[i]!=[]:
            newlist.append(lst[i])
    #print(newlist)
    return newlist
    
if __name__ == '__main__':
    print(compact([0]))
    print(compact([1, 2, 3, 4, 5]))
    print(compact([0, 1, 2, 3, 4, 5]))