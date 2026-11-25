def ft_count_harvest_recursive(day=1, last=None):
    if last is None:
        last = int(input("Days until harvest: "))

    if day > last:                 # base case: past the last day?
        print("Harvest time!")
        return
    print("Day", day)
    ft_count_harvest_recursive(day + 1, last)
