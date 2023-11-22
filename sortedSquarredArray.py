def sortedSquaredArray(array):
    # Write your code here.
    squarred = [element**2 for element in array]
    return sorted(squarred)


#chatgpt answer

def sortedSquaredArray(array):
    # The final sorted squared array
    squaredArray = [0 for _ in array]

    # Pointers for the smallest and largest values
    left = 0
    right = len(array) - 1

    # Iterate from the end of the squaredArray to fill it with the highest squares
    for i in range(len(array) - 1, -1, -1):
        smallerValue = array[left]
        largerValue = array[right]

        if abs(smallerValue) > abs(largerValue):
            squaredArray[i] = smallerValue ** 2
            left += 1
        else:
            squaredArray[i] = largerValue ** 2
            right -= 1

    return squaredArray

# Example usage
array = [-4, -1, 0, 3, 10]
print(sortedSquaredArray(array))  # Output: [0, 1, 9, 16, 100]
