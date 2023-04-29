#!.venv/bin/python3
"""Module which handles permutations and combintations"""

from itertools import permutations
from typing import List, Union


def permutation(
        objects: Union[int, List], sample: int = None) -> Union[int, List]:
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
    return len(result), result


test_list = ["a", "w", "s", "d", "f"]

rez, rez_list = permutation(5, 2)
print(rez)
print(rez_list)

print(f"{'='*80}")

rez, rez_list = permutation(test_list, 2)
print(rez)
print(rez_list)
