# author: Jiangyi Lin
import random


def bubble_sort(sort_list):
    """This is func implement bubble sort algorithm.
    first loop make sure the n->i part is in sort.
    second loop compare number one by one.

    T(n)=O(n^2)
    S(n)=O(1)

    Args:
        sort_list (list) : The list to be sorted.
    """
    length = len(sort_list)
    for i in range(length - 1, -1, -1):
        for j in range(i):
            if sort_list[j] > sort_list[j + 1]:
                tmp = sort_list[j]
                sort_list[j] = sort_list[j + 1]
                sort_list[j + 1] = tmp


def counting_sort(sort_list):
    """\This is func implementing counting sort.
    First count #number for every element
    Second count #number not lager than each element
    Finally place element into right space.

    k is the range of the number
    T(n)=O(n+k)
    S(n)=O(n+k)

    Args:
        sort_list (list) : The list to be sorted, where element number is no less than 0
            and all int.

    Returns:
         sorted list: The sorted list of the input
    """
    k = max(sort_list)
    k_list = [0] * (k + 1)
    for i in sort_list:
        k_list[i] += 1

    for i in range(1, k + 1):
        k_list[i] += k_list[i - 1]

    result = [0] * len(sort_list)
    for i in sort_list:
        result[k_list[i] - 1] = i
        k_list[i] -= 1

    return result


# noinspection PyUnusedLocal
def radix_sort(sort_list):
    """
    This is function implementing radix sort.

    d is how many digits
    k is constant number now(0-9 or alphabetic)

    T(n)=O(d*(n+k))=O(d*n)
    S(n)=O(d*n)

    :param sort_list:
    :return:
    """
    pass


def merge_sort(sort_list):
    """
    This is function implementing merge sort.

    T(n)=O(nlogn)
    S(n)=O(n)

    :param sort_list: The list we need to sort
    :return: the sorted list
    :rtype: list
    """

    def sort(low, high):
        if high - low < 1:
            return
        split = int((low + high) / 2)
        sort(low, split)
        sort(split + 1, high)
        merge(low, split, high)

    def merge(low, split, high):
        tmp = [i for i in result]
        i = low
        j = split + 1
        k = low
        while i <= split and j <= high:
            if tmp[i] < tmp[j]:
                result[k] = tmp[i]
                k += 1
                i += 1
            else:
                result[k] = tmp[j]
                k += 1
                j += 1
        while i <= split:
            result[k] = tmp[i]
            i += 1
            k += 1
        while j <= high:
            result[k] = tmp[j]
            j += 1
            k += 1

    result = [i for i in sort_list]
    sort(0, len(sort_list) - 1)

    return result


def quick_sort(sort_list):
    """
    This is function implementing quick sort.

    worst
    T(n)=O(n^2)
    average
    T(n)=O(nlogn)

    S(n)=O(1)

    :param sort_list: The list we need to sort
    :return: sorted list
    :rtype: list
    """

    # ! 3 number switch
    def sort(low, high):
        if low >= high:
            return
        i = low
        j = high
        pivot = result[i]
        while i < j:
            while i < j and result[j] >= pivot:
                j -= 1
            result[i] = result[j]
            while i < j and result[i] <= pivot:
                i += 1
            result[j] = result[i]
            result[i] = pivot

        sort(low, i - 1)
        sort(i + 1, high)

    result = [i for i in sort_list]
    sort(0, len(result) - 1)
    return result


def randomized_quick_sort(sort_list):
    """
    This is function implementing randomized quick sort.
    The pivot is chosen randomly.

    worst
    T(n)=O(n^2)
    average
    T(n)=O(nlogn)

    S(n)=O(1)

    :param sort_list: The list we need to sort
    :return: sorted list
    :rtype: list
    """

    # ! 3 number switch
    def sort(low, high):
        if low >= high:
            return

        # random pivot
        r = random.choice(range(low, high + 1))
        tmp = result[low]
        result[low] = result[r]
        result[r] = tmp

        i = low
        j = high
        pivot = result[i]
        while i < j:
            while i < j and result[j] >= pivot:
                j -= 1
            result[i] = result[j]
            while i < j and result[i] <= pivot:
                i += 1
            result[j] = result[i]
            result[i] = pivot

        sort(low, i - 1)
        sort(i + 1, high)

    result = [i for i in sort_list]
    sort(0, len(result) - 1)
    return result
