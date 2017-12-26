from Christmas import FunWithSnow
from List2 import remove_adjacent, linear_merge

clase = FunWithSnow()


def testRemoveAdjacement():
    assert (remove_adjacent([1, 2, 2, 3]) == [1, 2, 3])
    assert (remove_adjacent([2, 2, 3, 3, 3]) == [2, 3])
    assert remove_adjacent([]) == []


def testLinearMerge():
    assert (linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']) ==
            ['aa', 'bb', 'cc', 'xx', 'zz'])
    assert (linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']) ==
            ['aa', 'bb', 'cc', 'xx', 'zz'])
    assert (linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) ==
            ['aa', 'aa', 'aa', 'bb', 'bb'])
