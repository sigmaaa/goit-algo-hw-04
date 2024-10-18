import random
import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
            # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def timsort(arr):
    return sorted(arr)


def measure_time(func, data):
    return timeit.timeit(lambda: func(data.copy()), number=100)


small_dataset = [random.randint(0, 100) for _ in range(100)]
medium_dataset = [random.randint(0, 1000) for _ in range(1000)]
large_dataset = [random.randint(0, 10000) for _ in range(10000)]

datasets = [("Small", small_dataset),
            ("Medium", medium_dataset),
            ("Large", large_dataset)]

for name, dataset in datasets:
    print(f"\n{name} dataset:")
    for sort_func in [merge_sort, insertion_sort, timsort]:
        time_taken = measure_time(sort_func, dataset)
        print(f"{sort_func.__name__}: {time_taken:.5f} seconds")
