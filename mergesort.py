def merge_two_lists(a, b):
    List = []
    a_max_index = len(a) - 1
    b_max_index = len(b) - 1
    current_a = 0
    current_b = 0


    while current_a <= a_max_index and current_b <= b_max_index:
        if a[current_a] < b[current_b]:
            List.append(a[current_a])
            current_a += 1
        else:
            List.append(b[current_b])
            current_b += 1

    while current_a <= a_max_index:
        List.append(a[current_a])
        current_a += 1


    while current_b <= b_max_index:
        List.append(b[current_b])
        current_b += 1

    return List

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    middle = len(arr)//2

    return merge_two_lists(merge_sort(arr[:middle]),merge_sort(arr[middle:]))

def main():
    # Test case 1: Regular unsorted array
    a = [1, 7, 3, 8, 11, 90]
    print("Original:", a)
    print("Sorted:  ", merge_sort(a))

    # Test case 2: Already sorted array
    b = [1, 2, 3, 4, 5]
    print("\nOriginal:", b)
    print("Sorted:  ", merge_sort(b))

    # Test case 3: Reverse sorted array
    c = [5, 4, 3, 2, 1]
    print("\nOriginal:", c)
    print("Sorted:  ", merge_sort(c))

    # Test case 4: Array with duplicates
    d = [4, 2, 7, 3, 3, 7, 1, 4]
    print("\nOriginal:", d)
    print("Sorted:  ", merge_sort(d))

    # Test case 5: Single element array
    e = [42]
    print("\nOriginal:", e)
    print("Sorted:  ", merge_sort(e))

    # Test case 6: Empty array
    f = []
    print("\nOriginal:", f)
    print("Sorted:  ", merge_sort(f))

    # Test case 7: Array with negative numbers
    g = [-3, -1, -7, -5, 0, 2, 1]
    print("\nOriginal:", g)
    print("Sorted:  ", merge_sort(g))

    # Test case 8: Array with all identical elements
    h = [5, 5, 5, 5, 5]
    print("\nOriginal:", h)
    print("Sorted:  ", merge_sort(h))

    

if __name__ == "__main__":
    main()
