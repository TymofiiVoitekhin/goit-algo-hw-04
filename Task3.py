import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def timsort(arr):
    return arr.sort()


def benchmark():
    sizes = [1_000, 5_000, 10_000]
    results = []

    for size in sizes:
        arr = [random.randint(0, 100_000) for _ in range(size)]
        insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
        merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
        timsort_time = timeit.timeit(lambda: timsort(arr.copy()), number=1)
        results.append((size, insertion_time, merge_time, timsort_time))

    # Вивід у форматі Markdown
    print("| Розмір масиву | Insertion Sort (сек) | Merge Sort (сек) | Timsort (сек) |")
    print("|---------------|----------------------|------------------|---------------|")
    for size, ins, mer, tim in results:
        print(f"| {size: <10} | {ins: <15} | {mer: <15} | {tim: <15} |")


if __name__ == "__main__":
    benchmark()
