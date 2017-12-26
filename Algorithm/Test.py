# author: Jiangyi Lin
import unittest

from Algorithm.Sort import counting_sort, bubble_sort, merge_sort, quick_sort, randomized_quick_sort


class TestSort(unittest.TestCase):
    list1 = [6, 5, 4, 3, 2, 1]
    list2 = [1, 2, 3, 4, 5, 6]
    result_1_2 = [1, 2, 3, 4, 5, 6]
    list3 = [1, 2, 1, 5, 3]
    result_3 = [1, 1, 2, 3, 5]

    def setUp(self):
        TestSort.list1 = [6, 5, 4, 3, 2, 1]
        TestSort.list2 = [1, 2, 3, 4, 5, 6]
        TestSort.list3 = [1, 2, 1, 5, 3]

    def test_bubble(self):
        bubble_sort(TestSort.list1)
        bubble_sort(TestSort.list2)
        bubble_sort(TestSort.list3)
        self.assertEqual(TestSort.list1, TestSort.result_1_2)
        self.assertEqual(TestSort.list2, TestSort.result_1_2)
        self.assertEqual(TestSort.list3, TestSort.result_3)

    def test_counting(self):
        r1 = counting_sort(TestSort.list1)
        r2 = counting_sort(TestSort.list2)
        r3 = counting_sort(TestSort.list3)
        self.assertEqual(r1, TestSort.result_1_2)
        self.assertEqual(r2, TestSort.result_1_2)
        self.assertEqual(r3, TestSort.result_3)

    def test_merge(self):
        r1 = merge_sort(TestSort.list1)
        r2 = merge_sort(TestSort.list2)
        r3 = merge_sort(TestSort.list3)
        self.assertEqual(r1, TestSort.result_1_2)
        self.assertEqual(r2, TestSort.result_1_2)
        self.assertEqual(r3, TestSort.result_3)

    def test_quick(self):
        r1 = quick_sort(TestSort.list1)
        r2 = quick_sort(TestSort.list2)
        r3 = quick_sort(TestSort.list3)
        self.assertEqual(r1, TestSort.result_1_2)
        self.assertEqual(r2, TestSort.result_1_2)
        self.assertEqual(r3, TestSort.result_3)

    def test_randomized_quick(self):
        r1 = randomized_quick_sort(TestSort.list1)
        r2 = randomized_quick_sort(TestSort.list2)
        r3 = randomized_quick_sort(TestSort.list3)
        self.assertEqual(r1, TestSort.result_1_2)
        self.assertEqual(r2, TestSort.result_1_2)
        self.assertEqual(r3, TestSort.result_3)


if __name__ == '__main__':
    unittest.main()
