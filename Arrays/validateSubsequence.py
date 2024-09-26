def isValidSubsequence(array, sequence):
    print(array,sequence)
    sub = 0
    for i in range(len(array)):
        print("first loop i-->", i)
        if array[i] == sequence[sub]:
            print("array[i] == sequence[j] ", array[i] , sequence[sub])
            sub+=1
        if sub == len(sequence):
            return True

    return False
