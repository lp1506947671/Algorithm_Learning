#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def binarySearch(arr, l, r, x):
    """返回 x 在 arr 中的索引，如果不存在返回 -1"""
    # 基本判断
    if r < l:
        return -1
    mid = int(l + (r - l) / 2)
    # 元素整好的中间位置
    if arr[mid] == x:
        return mid
        # 元素小于中间位置的元素，只需要再比较左边的元素
    elif arr[mid] > x:
        return binarySearch(arr, l, mid - 1, x)
        # 元素大于中间位置的元素，只需要再比较右边的元素
    else:
        return binarySearch(arr, mid + 1, r, x)


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binarySearch(arr, 0, len(arr) - 1, x)
    tips = f"元素在数组中的索引为{result}" if result != -1 else "元素不在数组中"
    print(tips)