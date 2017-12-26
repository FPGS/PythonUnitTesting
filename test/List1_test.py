from List1 import match_ends, front_x, sort_last


    
def test_MatchEnds():
    assert (match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])== 3)
    assert (match_ends(['', 'x', 'xy', 'xyx', 'xx'])== 2)
    assert (match_ends(['aaa', 'be', 'abc', 'hello'])== 1)

def test_Front():
    assert (front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])==
                    ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    assert (front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])==
                    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    assert (front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])==
                    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

        
def test_SortLast():
    assert (sort_last([(1, 3), (3, 2), (2, 1)])==
                    [(2, 1), (3, 2), (1, 3)])
    assert (sort_last([(2, 3), (1, 2), (3, 1)])==
                    [(3, 1), (1, 2), (2, 3)])
    assert (sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])==
                    [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
        

