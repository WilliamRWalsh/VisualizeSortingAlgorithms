from random import shuffle
from visualize import Visualize
from collections import deque
from itertools import islice

# Bubble sort O(N^2) time on average
def bubble_sort(d):
    vis = Visualize(d)
    vis.bubble_sort()  # Starting frame

    length = len(d)
    for p in range(length):
        for i in range(length - p - 1):
            vis.bubble_sort(highlight_0=i, highlight_1=i+1)
            if d[i] > d[i+1]:
                d[i], d[i+1] = d[i+1], d[i]

    vis.bubble_sort()  # Finished frame
    vis.create_gif('bubble_sort')


def quick_sort(d):
    vis = Visualize(d)
    vis.quick_sort(d, -1, -1, -1, -1, -1)
    re_quick_sort(d, 0, len(d) - 1, vis)
    vis.quick_sort(d, -1, -1, -1, -1, -1)
    vis.create_gif('quick_sort')


def re_quick_sort(d, lo, hi, vis):
    if lo < hi:
        p = qs_partition(d, lo, hi, vis)
        re_quick_sort(d, lo, p - 1, vis)
        re_quick_sort(d, p + 1, hi, vis)


def qs_partition(d, lo, hi, vis):
    pivot = d[hi]
    swap_loc = lo

    for j in range(lo, hi):
        if d[j] < pivot:
            vis.quick_sort(d, j, swap_loc, hi, lo, hi - 1)
            d[swap_loc], d[j] = d[j], d[swap_loc]
            swap_loc += 1
        else:
            vis.quick_sort(d, j, -1, hi, lo, hi - 1)

    vis.quick_sort(d, hi, swap_loc, hi, lo, hi - 1)
    d[swap_loc], d[hi] = d[hi], d[swap_loc]

    return swap_loc


def start_merge_sort(d):
    vis = Visualize(d)
    vis.merge_sort()
    print(*merge_sort(d, vis))
    vis.merge_sort()
    vis.create_gif('merge_sort')


def merge_sort(d, vis, start, end):
    if len(d) <= 1:
        return d

    mid = len(d)//2
    left = deque(islice(d, 0, mid))
    right = deque(islice(d, mid, None))

    left = merge_sort(left, vis)
    right = merge_sort(right, vis)

    return merge(left, right, vis)


def merge(left, right, vis):
    result = deque()

    while left and right:
        if left[0] <= right[0]:
            # vis.merge_sort()
            result.append(left.popleft())
        else:
            # vis.merge_sort()
            result.append(right.popleft())

    while left:
        result.append(left.popleft())

    while right:
        result.append(right.popleft())

    return result


if __name__ == '__main__':
    data_points = 8
    data = [i for i in range(1, data_points + 1)]
    shuffle(data)
    # data = [20, 14, 13, 5, 19, 23, 18, 16, 10, 15, 8, 12, 3, 4, 1, 24, 6, 9, 2, 17, 22, 21, 11, 7]

    bubble_sort(data)
    # quick_sort(data)
    # start_merge_sort(data)
