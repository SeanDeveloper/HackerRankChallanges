from typing import List


def socketMatch(arr: List[int], k: int) -> List[int]:
    # arr reprents the array entered
    # k represents the number of pairs

    # initializing variables
    output = {}
    total_pairs = 0
    temp_value = 0

    # dictionary contianing all the values inside of the arr with no duplicates
    for y in set(arr):
        output.update({y: 0})
    for x in arr:
        output.update({x: output[x] + 1})
    
    for key, items in output.items():
        if items % k == 1:
            items = (items + 1) / 2 - 1
            if items % k == 1:
                total_pairs += 1
                temp_value += items
        if items % k == 0:
            total_pairs += 1
            temp_value += items / 2

    # print(f"Total Pairs: {temp_value}")
    return temp_value

socketMatch(arr=[10, 20, 20, 10, 10, 30, 50, 10, 20], k=2)
