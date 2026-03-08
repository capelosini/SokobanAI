numbersTable = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def isNumber(x):
    return x in numbersTable


def swap(arr, ia, ib):
    temp = arr[ia]
    arr[ia] = arr[ib]
    arr[ib] = temp
