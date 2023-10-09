def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Рекурсивно сортируем левую и правую части
        merge_sort(left)
        merge_sort(right)

        # Слияние отсортированных частей
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Обработка оставшихся элементов в левой части
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        # Обработка оставшихся элементов в правой части
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

# Пример использования
nums = [7, 8, 1, 10, 5, 0, 5]
merge_sort(nums)
print(nums)

