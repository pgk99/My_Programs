from array import *

if __name__ == "__main__":
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Example usage
    sample_array = array('i', [])
    n = int(input('Enter number of elements : '))
    for i in range(n):
        x = int(input(f'Enter element {i + 1} : '))
        sample_array.append(x)
    #To check whether the array is sorted or not

    k = int(input('Please enter the target value to search for : '))

    result = binary_search(sample_array, k)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")
