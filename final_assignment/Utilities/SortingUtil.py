# Handler Method for Heap Sort
def sortMarketCapAscending_UsingHeapSort(dataFrameInput):

    dataFrame = dataFrameInput

    heapSort(dataFrame)

    return dataFrame

# Handler Method for Quick Sort
def sortMarketCapAscending_UsingQuickSort(dataFrameInput):

    dataFrame = dataFrameInput
    dataFrameSize = len(dataFrame)

    quickSort(dataFrame, 0, dataFrameSize - 1)

    return dataFrame

# Handler Method for Shell Sort
def sortMarketCapAscending_UsingShellSort(dataFrameInput):

    dataFrame = dataFrameInput

    shellSort(dataFrame)

    return dataFrame

# Partion Method used by Quick Sort
def partition(dataFrame, startingIndex, endingIndex):

    a_index = (startingIndex - 1)
    pivotPoint = dataFrame[endingIndex]

    for b_index in range(startingIndex, endingIndex):

        if dataFrame[b_index] <= pivotPoint:

            a_index = a_index + 1
            dataFrame[a_index], dataFrame[b_index] = dataFrame[b_index], dataFrame[a_index]

    dataFrame[a_index + 1], dataFrame[endingIndex] = dataFrame[endingIndex], dataFrame[a_index + 1]

    return (a_index + 1)

# Method utilizes the Quick Sort Algorithm
def quickSort(dataFrame, startingIndex, endingIndex):

    if len(dataFrame) == 1: 
        
        return dataFrame

    if startingIndex < endingIndex:

        partitionResponse = partition(dataFrame, startingIndex, endingIndex)

        quickSort(dataFrame, startingIndex, partitionResponse - 1)
        quickSort(dataFrame, partitionResponse + 1, endingIndex)

# Heapify Method uses by Heap Sort
def heapify(dataFrame, size, index):

    largest = index
    left_heap = 2 * index + 1     
    right_heap = 2 * index + 2     

    if left_heap < size and dataFrame[index] < dataFrame[left_heap]:

        largest = left_heap

    if right_heap < size and dataFrame[largest] < dataFrame[right_heap]:

        largest = right_heap

    if largest != index:

        dataFrame[index], dataFrame[largest] = dataFrame[largest], dataFrame[index]
        heapify(dataFrame, size, largest)

# Method utilizes the Heap Sort Algorithm
def heapSort(dataFrame):

    size = len(dataFrame)

    for index in range(size // 2 - 1, -1, -1):

        heapify(dataFrame, size, index)

    for index in range(size - 1, 0, -1):

        dataFrame[index], dataFrame[0] = dataFrame[0], dataFrame[index]
        heapify(dataFrame, index, 0)

# Method utilizes the Shell Sort Algorithm
def shellSort(dataFrame):

    size = len(dataFrame)
    gap = int(size / 2)

    while gap > 0:

        for a_index in range(gap, size):

            temp = dataFrame[a_index]
            b_index = a_index

            while b_index >= gap and dataFrame[b_index - gap] > temp:

                dataFrame[b_index] = dataFrame[b_index - gap]
                b_index -= gap

            dataFrame[b_index] = temp

        gap = int(gap / 2)