import itertools

def rotate_array(arr, k):
    i = 0
    new_list = arr.copy()

    while i < len(arr):

        next_index = (i + k) % len(arr)

        new_list[next_index] = arr[i]

        i += 1

    return new_list


def rotate_array_no_auxiliary_space(arr, k):
    i = 0
    j = 0
    temp = arr[j]

    while i <= len(arr):

        next_position_index = (j + k) % len(arr)

        next_position_value = arr[next_position_index]

        arr[next_position_index] = temp

        temp = next_position_value

        j = next_position_index

        i = i + 1

    return arr


array_for_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(rotate_array(array_for_test, 3))
# print(rotate_array_no_auxiliary_space(array_for_test, 4))


def perez_rotation(arr, k):
    return arr[len(arr)-k:] + arr[:len(arr)-k]

def rotateKSteps(arr, k):
    currentTempIndex = 0
    i = 0
    while (i < len(arr)):
        nextIndex = (currentTempIndex + k) % len(arr)
        while(currentTempIndex != nextIndex):
            valueToPlace = arr[currentTempIndex]
            temp = arr[nextIndex]
            arr[nextIndex] = valueToPlace
            arr[currentTempIndex] = temp
            nextIndex = (nextIndex + k) % len(arr)
            i += 1
        currentTempIndex += 1
        i += 1
    return arr

def permitate(arr):
    return list(itertools.permutations([1, 2, 3]))


print(perez_rotation(array_for_test, 3))
# print(permitate(array_for_test))

print(rotateKSteps(array_for_test, 3))



