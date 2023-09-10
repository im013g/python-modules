def compare_nested_dicts(left, right):
    """
    Returns `changed`, items that are in `left` and `right`
    Returns `unique_left`, items are present only in `left`
    Returns `unique_right`, items are present only in `right`
    """
    changed = []
    unique_left = []
    unique_right = []

    def comapre_a_b(a_item, b_item, a_unique, ab_changed):
        for i in a_item:
            if i in b_item:
                if a_item[i] != b_item[i]:
                    changed.append(i)
            else:
                a_unique.append(i)
        return ab_changed, a_unique

    changed, unique_left = comapre_a_b(left, right, unique_left, changed)
    changed, unique_right = comapre_a_b(right, left, unique_right, changed)
    changed = list(set(changed))
    return changed, unique_left, unique_right