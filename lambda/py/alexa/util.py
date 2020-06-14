# -*- coding: utf-8 -*-
import random
import six
# from ask_sdk_core.handler_input import HandlerInput
# from ask_sdk_core.utils import is_request_type

from . import data
from typing import Dict

def load_locale_specific_recipe(locale):
    """Return the recipe dictionary specific to the locale.
    Checks for a recipe dictionary with name 'RECIPE_<locale>' in data
    module and return it. Returns None if there is no dictionary
    specific to the locale.
    eg: load_locale_specific_recipe('en-US') -> data.RECIPE_EN_US
    """
    # type: (str) -> Dict[str, str]
    return getattr(
        data, "RECIPE_{}".format(locale).upper().replace("-", "_"), None)


def get_random_item(locale):
    """Return a random item from the locale specific dict."""
    # type: (str) -> str
    return random.choice(list(load_locale_specific_recipe(locale).keys()))


def get_item(slots, states_list):
    """Get matching data object from slot value."""
    item = []
    resolved_slot = None
    for _, slot in six.iteritems(slots):
        if slot.value is not None:
            resolved_slot = slot.value
            for state in states_list:
                for _, v in six.iteritems(state):
                    if v.lower() == slot.value.lower():
                        item.append(state)
            if len(item) > 0:
                return item[0], True
    else:
        return resolved_slot, False