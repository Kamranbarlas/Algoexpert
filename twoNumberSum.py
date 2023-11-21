def twoNumberSum(array, targetSum):
    print("input  +++++++++++ ",array)
    for i in range(len(array) - 1):
        # print("i=========>",array[i])
        for j in range(i+1,len(array)):
            if array[i] + array[j] == targetSum:
                return(array[i] , array[j])
    return []
