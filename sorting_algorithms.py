from random import shuffle
from visualize import Visualize


def bubble_sort(d, num_of_points):
    vis = Visualize(num_of_points, None)
    vis.bubble_sort(d, -1, -1, -1, -1, -1)

    passes = 0
    while passes < num_of_points:
        for i in range(num_of_points - passes - 1):
            vis.bubble_sort(d, i, i+1, num_of_points - passes, -1, -1)

            if i+1 < num_of_points and d[i] > d[i+1]:
                temp = d[i]
                d[i] = d[i+1]
                d[i+1] = temp

        passes += 1
    vis.bubble_sort(d, -1, -1, -1, -1, -1)
    vis.create_gif('bubble_sort')


def quick_sort(d, num_of_points):
    vis = Visualize(num_of_points, None)
    vis.bubble_sort(d, -1, -1, -1, -1, -1)
    re_quick_sort(d, 0, num_of_points - 1, vis)
    vis.bubble_sort(d, -1, -1, -1, -1, -1)
    vis.create_gif('quick_sort')


def re_quick_sort(d, lo, hi, vis):
    if lo < hi:
        p = qs_partition(d, lo, hi, vis)
        re_quick_sort(d, lo, p - 1, vis)
        re_quick_sort(d, p + 1, hi, vis)


def qs_partition(d, lo, hi, vis):
    pivot = d[hi]
    i = lo - 1
    for j in range(lo, hi):
        if d[j] < pivot:
            i += 1
            vis.bubble_sort(d, j, i, hi, lo, hi - 1)
            temp = d[i]
            d[i] = d[j]
            d[j] = temp
        else:
            vis.bubble_sort(d, j, -1, hi, lo, hi - 1)

    vis.bubble_sort(d, hi, i + 1, hi, lo, hi - 1)
    temp = d[i + 1]
    d[i + 1] = d[hi]
    d[hi] = temp

    return i + 1


def start_merge_sort(d, num_of_points):
    vis = Visualize(num_of_points, tuple(d))
    vis.merge_sort(-1, -1, -1, -1, -1)
    print(merge_sort(d, vis, 0, num_of_points - 1))
    vis.merge_sort(-1, -1, -1, -1, -1)
    vis.create_gif('merge_sort')


def merge_sort(d, vis, start, end):
    if len(d) <= 1:
        return d

    mid = len(d)//2
    left = d[:mid]
    right = d[mid:]

    left = merge_sort(left, vis, start, mid - 1)
    right = merge_sort(right, vis, start+mid, end)

    return merge(left, right, vis, start, mid - 1, start+mid, end)


def merge(left, right, vis, l0, l1, r0, r1):
    result = []
    k = l0
    while left and right:
        if left[0] <= right[0]:
            vis.merge_sort(l0, l1, r0, r1, k)
            l0 += 1
            result.append(left.pop(0))
        else:
            vis.merge_sort(l0, l1, r0, r1, k)
            r0 += 1
            l0 += 1
            result.append(right.pop(0))
        k += 1

    while left:
        # vis.merge_sort(l0, l1, r0, r1, k)
        result.append(left.pop(0))
        k += 1

    while right:
        # vis.merge_sort(l0, l1, r0, r1, k)
        result.append(right.pop(0))
        k += 1

    return result


if __name__ == '__main__':
    data_points = 32
    data = [i for i in range(1, data_points + 1)]
    shuffle(data)

    # data = [8, 7, 6, 5, 4, 3, 2, 1]
    # bubble_sort(data, data_points)
    # quick_sort(data, data_points)
    start_merge_sort(data, data_points)