def count_sort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = max(arr)

    # create and initialize cntArr
    cntArr = [0] * (maxval + 1)

    # count frequency of each element
    for v in arr:
        cntArr[v] += 1

    # compute prefix sums
    for i in range(1, maxval + 1):
        cntArr[i] += cntArr[i - 1]

    # build output array
    ans = [0] * n
    # iterate in reverse to keep it stable
    for i in range(n - 1, -1, -1):
        v = arr[i]
        ans[cntArr[v] - 1] = v
        cntArr[v] -= 1

    return ans


if __name__ == "__main__":
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    ans = count_sort(arr)
    print(ans)
