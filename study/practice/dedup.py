def no_dup(items):
    no_dup_items=[]
    seen=set()
    for item in items:
        if item not in seen:
            no_dup_items.append(item)
            seen.add(item)
    return no_dup_items()




