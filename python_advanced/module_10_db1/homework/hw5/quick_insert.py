from typing import Union, List

Number = Union[int, float, complex]


def find_insert_position(array: List[Number], number: Number) -> int:
    low = 0
    high = len(A)

    if x > A[-1]:
        return high
    if x < A[0]:
        return low

    while low < high:
        mid = low + (high - low) // 2
        if x < A[mid]:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == '__main__':
    A: List[Number] = [1, 2, 3, 3, 3, 5]
    x: Number = 4
    insert_position: int = find_insert_position(A, x)
    assert insert_position == 5

    A: List[Number] = [1, 2, 3, 3, 3, 5]
    x: Number = 4
    A.insert(insert_position, x)
    assert A == sorted(A)


