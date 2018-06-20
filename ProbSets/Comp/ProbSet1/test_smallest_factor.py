import smallfac as sf

def test_smallest_factor():
    assert sf.smallest_factor(1) == 1, "failed"
    assert sf.smallest_factor(4) == 2, "failed"
    assert sf.smallest_factor(6) == 2, "failed"
    assert sf.smallest_factor(5) == 5, "failed"
    assert sf.smallest_factor(9) == 3, "failed"
    assert sf.smallest_factor(10) == 2
