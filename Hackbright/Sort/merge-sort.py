def mergesorted(a, b):
    """Merge 2 already sorted lists"""

    ia = 0  # index into list a
    ib = 0  # index into list b

    while ia < len(a) and ib < len(b):
        # Check current items in both lists:
        #  - if a < b, add a and increase ia
        #  - else      add b and increase ib

        if a[ia] < b[ib]:
            out.append(a[ia])
            ia += 1

        else:
            out.append(b[ib])
            ib += 1

    # One list could have things remaining; add any remaining items
    out.extend(a[ia:])
    out.extend(b[ib:])

    return out