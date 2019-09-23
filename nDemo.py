def getPairsCount(i_List, listLenght, i_Sum):
    dct={'key':'Value'}

    for i in range(0, listLenght):
        for j in range(i + 1, listLenght):
            if i_List[i] + i_List[j] == i_Sum:
                dct.add(1,'i_List[i],i_List[j]')
                print(dct)
                return "Found Pair"

if __name__ == "__main__":
    i_List=[1,2,4,5,67,7]
    listLenght=len(i_List)
    i_Sum=68

    o_result=getPairsCount(i_List, listLenght, i_Sum)
    print(o_result)
