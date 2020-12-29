MyList = [318, 3, 2, 1, 0, 1]
print(MyList)

def BubSort(MyList):
    n = len(MyList)
    for i in range(n-1):
        for j in range(i + n - 1):
            if MyList[j]> MyList[j+1]:
                tmp = MyList[j]
                MyList[j]= MyList[j+1]
                MyList[j+1]= tmp
BubSort(MyList);
print(MyList)