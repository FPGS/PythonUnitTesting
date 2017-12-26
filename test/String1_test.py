
from String1 import mix_up, donuts, both_ends, fix_start


def testDonuts():
    assert (donuts(4)== "Number of donuts: 4")
    assert (donuts(9)== 'Number of donuts: 9')
    assert (donuts(10)== 'Number of donuts: many')
    assert (donuts(99)== 'Number of donuts: many')

def testBothEnds():
    assert (both_ends('spring')== 'spng')
    assert (both_ends('Hello')== 'Helo')
    assert (both_ends('a')== '')
    assert (both_ends('xyz')== 'xyyz')

def testFixStart():
    assert fix_start('babble')== 'ba**le'
    assert (fix_start('aardvark')== 'a*rdv*rk')
    assert (fix_start('google')== 'goo*le')
    assert (fix_start('donut')== 'donut')

def testMixUp():
    assert (mix_up('mix', 'pod')== 'pox mid')
    assert (mix_up('dog', 'dinner')== 'dig donner')
    assert (mix_up('gnash', 'sport')== 'spash gnort')
    assert (mix_up('pezzy', 'firm')== 'fizzy perm')
