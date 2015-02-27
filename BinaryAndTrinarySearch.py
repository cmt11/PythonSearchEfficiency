import random
import time


"""
This is a testing module which runs several experiments comparing the
efficiency of binary search and trinary search algorithms.
"""
def main():
    sizes = [500, 1000, 5000, 10000, 25000, 50000]

    # Loop through different array sizes
    for size in sizes:
        nums = generateArray(size)

        # Loop through different sized lists of numbers to search for
        # The numbers being searched for are present in the list
        for n in [50, 100, 250]:
            testNums = random.sample(nums, n)
            start = time.clock()
            
            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses binary search
            for search in testNums:
                binSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Binary search time for list size", size, "and", \
                n, "search values (milliseconds):", totalTime * 1000

            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses trinary search
            start = time.clock()
            for search in testNums:
                trinSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Trinary search time for list size", size, "and", \
                n, "search values (milliseconds):", totalTime * 1000
            print "----------"

        # Loop through different sized lists of numbers to search for
        # The numbers being searched for are NOT present in the list
        for n in [50, 100, 250]:
            testNums = generateAbsentTest(nums, size, n)
            start = time.clock()

            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses binary search
            for search in testNums:
                binSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Binary search time for list size", size, "and", n, \
                  "ABSENT search values (nanoseconds):", totalTime * 1000

            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses trinary search
            start = time.clock()
            for search in testNums:
                trinSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Trinary search time for list size", size, "and", n, \
                  "ABSENT search values (nanoseconds):", totalTime * 1000
            print "----------"



"""
Generates a sorted list of with random numbers.
Takes the size of the list.
Returns the sorted list.
"""
def generateArray(size):
    array = []
    for i in range(0, size - 1):
        # Append a random integer to the array
        array.append((random.randint(0, size * 10)) * 2)
    mergeSort(array)
    return array



"""
Generates a list of random numbers, none of which are present in the original
array being searched.
Takes the original list, the original list's size, and the size of the new
testing list to be generated.
Returns the list of random numbers.
"""
def generateAbsentTest(nums, originalSize, testSize):
    counter = 0
    array = []
    while counter < testSize:
        testNum = random.randint(0, originalSize * 10)
        # If the test number is not in the original list, append it to the new one
        if binSearch(nums, 0, originalSize - 1, testNum) == -1:
            array.append(testNum)
            counter+=1
    return array
    


"""
Binary search algorithm.
Takes an array to search, lowest and highest search indeces to consider,
and a target value as parameters.
Returns index of target if found, or -1 if target is not in the list.
"""
def binSearch(array, low, high, target):
    if low > high:
        # The target is not in the list
        return -1
    else:
        # Calculate middle index
        mid = ((high + low) / 2)
        if array[mid] == target:
            # The target value has been found
            return mid
        elif array[mid] > target:
            # Search the "lower" half of the array
            return binSearch(array, low, mid -1, target)
        else:
            # Search the "upper" half of the array
            return binSearch(array, mid+1, high, target)



"""
Trinary search algorithm.
Takes an array to search, lowest and highest search indeces to consider,
and a target value as parameters.
Returns index of target if found, or -1 if target is not in the list.
"""
def trinSearch(array, low, high, target):
    if low > high:
        # The target is not in the list
        return -1
    else:
        # Calculate one-third and two-thirds indeces
        oneThird = low + ((high - low) / 3)
        twoThirds = low + (2 * ((high - low) / 3))
        if array[oneThird] == target:
            # The target value has been found
            return oneThird
        elif array[twoThirds] == target:
            # The target value has been found
            return twoThirds
        elif array[twoThirds] < target:
            # Search the "upper" third of the array
            return trinSearch(array, twoThirds+1, high, target)
        elif array[oneThird] < target:
            # Search the "middle" third of the array
            return trinSearch(array, oneThird+1, twoThirds-1, target)
        else:
            # Search the "lower" third of the array
            return trinSearch(array, low, oneThird-1, target)



"""
Merge sort algorithm.
Takes an array and sorts its elements in non-decreasing order.
"""
def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) / 2
        lower = nums[:mid]
        upper = nums[mid:]
        mergeSort(lower)
        mergeSort(upper)
        i=0
        j=0
        k=0
        while (i < len(lower) and j < len(upper)):
            if lower[i] < upper[j]:
                nums[k] = lower[i]
                i+=1
            else:
                nums[k] = upper[j]
                j+=1
            k+=1
        while (i < len(lower)):
            nums[k] = lower[i]
            i+=1
            k+=1
        while (j < len(upper)):
            nums[k] = upper[j]
            j+=1
            k+=1
12cmt@queensu.ca

I confirm that this submission is my own work and is consistent
with the Queen's regulations on Academic Integrity.

This is a testing module which runs several experiments comparing the
efficiency of binary search and trinary search algorithms.
"""
def main():
    sizes = [500, 1000, 5000, 10000, 25000, 50000]

    # Loop through different array sizes
    for size in sizes:
        nums = generateArray(size)

        # Loop through different sized lists of numbers to search for
        # The numbers being searched for are present in the list
        for n in [50, 100, 250]:
            testNums = random.sample(nums, n)
            start = time.clock()
            
            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses binary search
            for search in testNums:
                binSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Binary search time for list size", size, "and", \
                n, "search values (milliseconds):", totalTime * 1000

            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses trinary search
            start = time.clock()
            for search in testNums:
                trinSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Trinary search time for list size", size, "and", \
                n, "search values (milliseconds):", totalTime * 1000
            print "----------"

        # Loop through different sized lists of numbers to search for
        # The numbers being searched for are NOT present in the list
        for n in [50, 100, 250]:
            testNums = generateAbsentTest(nums, size, n)
            start = time.clock()

            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses binary search
            for search in testNums:
                binSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Binary search time for list size", size, "and", n, \
                  "ABSENT search values (nanoseconds):", totalTime * 1000

            # Loop through the list of "search" numbers and time how long it takes
            # This part of the test uses trinary search
            start = time.clock()
            for search in testNums:
                trinSearch(nums, 0, size - 1, search)
            totalTime = time.clock() - start
            print "Trinary search time for list size", size, "and", n, \
                  "ABSENT search values (nanoseconds):", totalTime * 1000
            print "----------"



"""
Generates a sorted list of with random numbers.
Takes the size of the list.
Returns the sorted list.
"""
def generateArray(size):
    array = []
    for i in range(0, size - 1):
        # Append a random integer to the array
        array.append((random.randint(0, size * 10)) * 2)
    mergeSort(array)
    return array



"""
Generates a list of random numbers, none of which are present in the original
array being searched.
Takes the original list, the original list's size, and the size of the new
testing list to be generated.
Returns the list of random numbers.
"""
def generateAbsentTest(nums, originalSize, testSize):
    counter = 0
    array = []
    while counter < testSize:
        testNum = random.randint(0, originalSize * 10)
        # If the test number is not in the original list, append it to the new one
        if binSearch(nums, 0, originalSize - 1, testNum) == -1:
            array.append(testNum)
            counter+=1
    return array
    


"""
Binary search algorithm.
Takes an array to search, lowest and highest search indeces to consider,
and a target value as parameters.
Returns index of target if found, or -1 if target is not in the list.
"""
def binSearch(array, low, high, target):
    if low > high:
        # The target is not in the list
        return -1
    else:
        # Calculate middle index
        mid = ((high + low) / 2)
        if array[mid] == target:
            # The target value has been found
            return mid
        elif array[mid] > target:
            # Search the "lower" half of the array
            return binSearch(array, low, mid -1, target)
        else:
            # Search the "upper" half of the array
            return binSearch(array, mid+1, high, target)



"""
Trinary search algorithm.
Takes an array to search, lowest and highest search indeces to consider,
and a target value as parameters.
Returns index of target if found, or -1 if target is not in the list.
"""
def trinSearch(array, low, high, target):
    if low > high:
        # The target is not in the list
        return -1
    else:
        # Calculate one-third and two-thirds indeces
        oneThird = low + ((high - low) / 3)
        twoThirds = low + (2 * ((high - low) / 3))
        if array[oneThird] == target:
            # The target value has been found
            return oneThird
        elif array[twoThirds] == target:
            # The target value has been found
            return twoThirds
        elif array[twoThirds] < target:
            # Search the "upper" third of the array
            return trinSearch(array, twoThirds+1, high, target)
        elif array[oneThird] < target:
            # Search the "middle" third of the array
            return trinSearch(array, oneThird+1, twoThirds-1, target)
        else:
            # Search the "lower" third of the array
            return trinSearch(array, low, oneThird-1, target)



"""
Merge sort algorithm.
Takes an array and sorts its elements in non-decreasing order.
"""
def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) / 2
        lower = nums[:mid]
        upper = nums[mid:]
        mergeSort(lower)
        mergeSort(upper)
        i=0
        j=0
        k=0
        while (i < len(lower) and j < len(upper)):
            if lower[i] < upper[j]:
                nums[k] = lower[i]
                i+=1
            else:
                nums[k] = upper[j]
                j+=1
            k+=1
        while (i < len(lower)):
            nums[k] = lower[i]
            i+=1
            k+=1
        while (j < len(upper)):
            nums[k] = upper[j]
            j+=1
            k+=1
