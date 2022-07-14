
def histo(data, bins=3):
    hist = {}
    element_count = {}
    minval = data[0]
    maxval = data[0]
    for i in data:
        if i < minval:
            minval = i
        elif i > maxval:
            maxval = i
        if i not in element_count:
            element_count[i] = 1
        else:
            element_count[i] = element_count[i] + 1

    bucket_size = (maxval - minval) // bins
    print(f'bucket size={bucket_size}')

    for i in range(minval, maxval + 1, bucket_size):
        if i < maxval - bucket_size:
            hist[f'{i}-{i+bucket_size-1}'] = sum(element_count.get(j, 0) for j in range(i, i+bucket_size))
        else:
            hist[f'{i}-{maxval}'] = sum(element_count.get(j, 0) for j in range(i, maxval + 1 ))

    return hist


if __name__ == '__main__':
    args = [
        ([2,3,4,5], 2),
        ([1,2,3,3,3,5,6,9,9,10], 3),
        ([3,3,3,3,3,3,3,3,3,3,3,3,3], 4),
        ([1,1,22,4,6,7,2,1,4], 4)
    ]
    for arg in args:
        print(f'Input {arg[0]}, buckets={arg[1]}')
        h = histo(arg[0], arg[1])
        print(h)




