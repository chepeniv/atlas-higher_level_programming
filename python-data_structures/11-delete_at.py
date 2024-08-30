#!/usr/bin/python3

def delete_at(items=[], i=0):
    if len(items) > 0:
        first = items[:i]
        second = items[i+1:]
        items.clear()
        items.extend(first + second)
    return items
