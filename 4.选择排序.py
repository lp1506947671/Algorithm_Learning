#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select_sort(arr):
    n = len(arr)
    for i in range(n):
        mix_index = i
        for j in range(i + 1, n):
            if arr[mix_index] > arr[j]:
                mix_index = j
        arr[i], arr[mix_index] = arr[mix_index], arr[i]


if __name__ == "__main__":
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    select_sort(arr1)
    print(f"排序后的数组:{arr1}")
