def mergeArr(arr1,arr2):
    result = []
    for i in range(len(arr1) + len(arr2)):
        result.append(i)

    idx_one = 0
    idx_two = 0
    result_idx = 0

    while (idx_one < len(arr1)) and (idx_two < len(arr2)):
        if arr1[idx_one] < arr2[idx_two]:
            result[result_idx] = arr1[idx_one]
            idx_one +=1
            result_idx +=1

        else:
            result[result_idx] = arr2[idx_two]
            idx_two += 1
            result_idx += 1


    while (idx_one < len(arr1)):
        result[result_idx] = arr1[idx_one]
        idx_one += 1
        result_idx += 1

    while (idx_two < len(arr2)):
        result[result_idx] = arr2[idx_two]
        idx_two += 1
        result_idx += 1

    return result

print(mergeArr([3,4,5],[-2,5,29]))