def is_anagram(first_string, second_string):
    first_string_lower = list(first_string.lower())
    second_string_lower = list(second_string.lower())

    if first_string == '' and second_string == '':
        return (first_string, second_string, False)

    merge_sort(first_string_lower)
    merge_sort(second_string_lower)

    first_string_lower = "".join(first_string_lower)
    second_string_lower = "".join(second_string_lower)

    result = first_string_lower == second_string_lower

    return (first_string_lower, second_string_lower, result)


def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (end + start) // 2
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        merge(word, start, mid, end)


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index += 1
        else:
            word[general_index] = right[right_index]
            right_index += 1
