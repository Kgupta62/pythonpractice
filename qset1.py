input = [
    [1,2,2,4,3,6],
    [5,1,3,4],
    [9,5,7,1],
    [2,4,1,3]]
result =set(input[0])
for array in input[1:]:
    result.update(array)
print(result)
