def ds(a=1,b="default"):
    print(" 1)Normal\n 2)List \n 3)Tuple\n 4)Set\n 5)Dictionary")
    i=int(input("Enter type 0f datastructure"))
    if i==1:
        return a,b
    elif i==2:    
        list=[a,b]
        return list
    elif i==3:
        tuple=(a,b)
        return tuple
    elif i==4:
        set={a,b}
        return set
    elif i==5:
        dictionary={
            "roll no":a,
            "name":b
            }
        return dictionary
    else:
        print("choose correct option")
        
    if i==1:
        del (a,b)
    elif i==2:    
       del(list)
    elif i==3:
       del(tuple)
    elif i==4:
       del(set)
    elif i==5:
       del(dictionary)
    print("data structure deleted")
print(ds(83,"mangal"))
