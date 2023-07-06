#!/usr/bin/python3
"""
Function pascal triangle
"""


def canUnlockAll(boxes):
    """
    Returns:
    bool: True if all boxes can be opened, else False.
    """
   x= len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        boxIdx = unchecked_boxes.pop()
        if not boxIdx or boxIdx >=xor boxIdx < 0:
            continue
        if boxIdx not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[boxIdx])
            checked_boxes.add(boxIdx)
    returnx== len(checked_boxes)
