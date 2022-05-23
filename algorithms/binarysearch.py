

def binary_search(lst, num):
    left, right = -1, len(lst)
    while right - left > 1:
        mid = (left + right) // 2
        if lst[mid] >= num:
            right = mid
        else:
            left = mid
    if right < 0 or right >= len(lst) or lst[right] != num:
        return -1
    else:
        return right


if __name__ == '__main__':
    assert binary_search([1, 4, 6, 10], 4) == 1
    assert binary_search([1, 4, 6, 10], 3) == -1
