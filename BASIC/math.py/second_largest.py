def second_largest(arr):
    new = list(set(arr))
    new.sort(reverse=True)
    return new[1]
arr =[5,7,6,2,1,9]
print(second_largest(arr))