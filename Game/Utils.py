from enum import Enum

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


class Directions(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3
    Unknown = 4


def isNumber(x):
    return x in numbersTable


def swap(arr, ia, ib):
    temp = arr[ia]
    arr[ia] = arr[ib]
    arr[ib] = temp
