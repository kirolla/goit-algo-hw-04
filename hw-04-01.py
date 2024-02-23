import timeit
import random

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

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Генеруємо різні набори даних для сортування
    small_data = random.sample(range(1000), 10)
    medium_data = random.sample(range(10000), 100)
    large_data = random.sample(range(100000), 1000)

    # Сортуємо дані та вимірюємо час для кожного алгоритму
    print("Час сортування за допомогою сортування злиттям:")
    print("Кількість елементів для вимірювання:", len(small_data))
    print(timeit.timeit(lambda: merge_sort(small_data), number=1000))
    print(timeit.timeit(lambda: merge_sort(medium_data), number=1000))
    print(timeit.timeit(lambda: merge_sort(large_data), number=1000))

    print("\nЧас сортування за допомогою сортування вставками:")
    print("Кількість елементів для вимірювання:", len(small_data))
    print(timeit.timeit(lambda: insertion_sort(small_data), number=1000))
    print(timeit.timeit(lambda: insertion_sort(medium_data), number=1000))
    print(timeit.timeit(lambda: insertion_sort(large_data), number=1000))

    print("\nЧас сортування за допомогою вбудованого алгоритму Python (Timsort):")
    print("Кількість елементів для вимірювання:", len(small_data))
    print(timeit.timeit(lambda: sorted(small_data), number=1000))
    print(timeit.timeit(lambda: sorted(medium_data), number=1000))
    print(timeit.timeit(lambda: sorted(large_data), number=1000))

if __name__ == "__main__":
    main()
