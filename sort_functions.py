def bubble_sort_peminjaman(items, kriteria, order='ASC'):
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if kriteria == "Nama Barang":
                if (order == 'ASC' and items[j][0] > items[j+1][0]) or (order == 'DESC' and items[j][0] < items[j+1][0]):
                    items[j], items[j+1] = items[j+1], items[j]
            elif kriteria == "Nama Peminjam":
                if (order == 'ASC' and items[j][1] > items[j+1][1]) or (order == 'DESC' and items[j][1] < items[j+1][1]):
                    items[j], items[j+1] = items[j+1], items[j]
            elif kriteria == "Tanggal Pinjam":
                if (order == 'ASC' and items[j][2] > items[j+1][2]) or (order == 'DESC' and items[j][2] < items[j+1][2]):
                    items[j], items[j+1] = items[j+1], items[j]
            elif kriteria == "Tanggal Kembali":
                if (order == 'ASC' and items[j][3] > items[j+1][3]) or (order == 'DESC' and items[j][3] < items[j+1][3]):
                    items[j], items[j+1] = items[j+1], items[j]
    return items

def merge_sort_peminjaman(items, kriteria, order='ASC'):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left_half = merge_sort_peminjaman(items[:mid], kriteria, order)
    right_half = merge_sort_peminjaman(items[mid:], kriteria, order)

    return merge(left_half, right_half, kriteria, order)

def merge(left, right, kriteria, order):
    sorted_list = []
    while left and right:
        if kriteria == "Nama Barang":
            if (order == 'ASC' and left[0][0] < right[0][0]) or (order == 'DESC' and left[0][0] > right[0][0]):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif kriteria == "Nama Peminjam":
            if (order == 'ASC' and left[0][1] < right[0][1]) or (order == 'DESC' and left[0][1] > right[0][1]):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif kriteria == "Tanggal Pinjam":
            if (order == 'ASC' and left[0][2] < right[0][2]) or (order == 'DESC' and left[0][2] > right[0][2]):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif kriteria == "Tanggal Kembali":
            if (order == 'ASC' and left[0][3] < right[0][3]) or (order == 'DESC' and left[0][3] > right[0][3]):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))

    sorted_list.extend(left if left else right)
    return sorted_list


# algoritma sorting sebelum menambahkan fungsi asc dan desc
# def bubble_sort_peminjaman(items, kriteria):
#     n = len(items)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if kriteria == "Nama Barang":
#                 if items[j][0] > items[j+1][0]:
#                     items[j], items[j+1] = items[j+1], items[j]
#             elif kriteria == "Nama Peminjam":
#                 if items[j][1] > items[j+1][1]:
#                     items[j], items[j+1] = items[j+1], items[j]
#             elif kriteria == "Tanggal Pinjam":
#                 if items[j][2] > items[j+1][2]:
#                     items[j], items[j+1] = items[j+1], items[j]
#             elif kriteria == "Tanggal Kembali":
#                 if items[j][3] > items[j+1][3]:
#                     items[j], items[j+1] = items[j+1], items[j]
#     return items

# def merge_sort_peminjaman(items, kriteria):
#     if len(items) <= 1:
#         return items

#     mid = len(items) // 2
#     left_half = merge_sort_peminjaman(items[:mid], kriteria)
#     right_half = merge_sort_peminjaman(items[mid:], kriteria)

#     return merge(left_half, right_half, kriteria)

# def merge(left, right, kriteria):
    sorted_list = []
    while left and right:
        if kriteria == "Nama Barang":
            if left[0][0] < right[0][0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif kriteria == "Nama Peminjam":
            if left[0][1] < right[0][1]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif kriteria == "Tanggal Pinjam":
            if left[0][2] < right[0][2]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif kriteria == "Tanggal Kembali":
            if left[0][3] < right[0][3]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))

    sorted_list.extend(left if left else right)
    return sorted_list
