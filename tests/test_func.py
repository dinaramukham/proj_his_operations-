import json

import pytest

from utils import func


@pytest.fixture
def coll():
    return "Visa Gold 27248529432547658655"


def test_info_from(coll):
    assert func.info_from(coll) == "Visa Gold"


def test_hide_str(coll):
    assert func.hide_str(coll[-20:]) == "2724 85** **** **** 8655"
    assert func.hide_str(coll[-16:]) == "8529 43** **** 8655"


def test_hide_check(coll):
    assert func.hide_check(coll) == "**8655"


@pytest.fixture
def empty():
    with open('/Users/dinara/PycharmProjects/proj_his_operations-/utils/operations.json') as f:
        list_ = json.load(f)
        return list_


def test_sort_operat(empty):
    assert func.sort_operat(empty)[0]['id'] == 863064926
def test_print_info(empty):
    assert func.print_info(func.sort_operat(empty))[:11]  =="\n08.12.2019"
