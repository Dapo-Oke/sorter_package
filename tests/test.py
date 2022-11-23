from mypackage import myModule

def test_top_n():
    """
    tests top_n to make sure it works
    """
    assert myModule.top_n([8,7,6,6,4,3,2,2,2],4) == [8,7,6,4], "incorrect"
    assert myModule.top_n([12,5,8,1,8,9],3) == [12,9,8], "incorrect"
    assert myModule.top_n([7,9,3,3,1,1,2,5],4) == [9,7,5,3], "incorrect"
