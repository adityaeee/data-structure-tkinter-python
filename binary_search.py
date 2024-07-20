def binary_search_peminjaman(items, nama_peminjam):
    items.sort(key=lambda x: x[1])
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        if items[mid][1] == nama_peminjam:
            return items[mid]
        elif items[mid][1] < nama_peminjam:
            low = mid + 1
        else:
            high = mid - 1
    return -1
