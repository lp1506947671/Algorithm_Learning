#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr1)
    print(f"排序后的数组:{arr1}")
