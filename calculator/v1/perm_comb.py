#!.venv/bin/python3
"""Module which handles permutations and combintations"""

from itertools import permutations
from typing import List, Union


def permutation(objects: Union[int, List], sample: int = None) -> List:
    """Get all permutations of lists"""
    if not isinstance(objects, int) and not sample:
        sample = len(objects)
    elif not sample:
        sample = objects
    if isinstance(objects, int):
        objects = range(objects)
    perm = permutations(objects, sample)
    result = []
    for i in list(perm):
        result.append(i)
        # print (i)
    return len(result)


def permutation_visuals(objects: Union[int, List], sample: int = None) -> List:
    """See all permutations of lists"""
    if not isinstance(objects, int) and not sample:
        sample = len(objects)
    elif not sample:
        sample = objects
    if isinstance(objects, int):
        objects = range(objects)
    perm = permutations(objects, sample)
    result = []
    for i in list(perm):
        result.append(i)
    return result


# test_list = ["a", "w", "s", "d", "f"]

# rez = permutation_visuals(5, 2)
# print(rez)

# rez = permutation(5, 2)
# print(rez)

# print(f"{'='*80}")

# rez = permutation_visuals(test_list, 2)
# print(rez)

# rez = permutation(test_list, 2)
# print(rez)
