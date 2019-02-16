__all__ = ["STRUCTURES"]

import pkg_resources
import collections

from hg_conway.structures import base

STRUCTURES_ENTRY_POINT = "hg_conway.structures"


def get_structures(base_structures: dict = None):
    # initialize structure dict with base files (no install with entry_points needed)
    structures = collections.OrderedDict({"base": base_structures})

    # get dicts of structures from entry_points
    for entry_point in pkg_resources.iter_entry_points(STRUCTURES_ENTRY_POINT):
        structures[entry_point.name].update(**entry_point.load())

    # flatten dicts
    flatten_structures = collections.OrderedDict([(k2, v2) for k, v in structures.items() for k2, v2 in v.items()])
    return flatten_structures


STRUCTURES = get_structures(base.BASE_STRUCTURES)
