def frequency_sort(items):
    return sorted(items,
                  key=lambda i: items.count(i)*10000 - items.index(i),
                  reverse=True)
