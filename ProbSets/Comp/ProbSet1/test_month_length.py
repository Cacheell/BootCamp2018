import monthlength as ml

def test_month_length():
    assert ml.month_length("September") == 30, "30 months fail"
    assert ml.month_length("January") == 31, "31rd months fail"
    assert ml.month_length("cache") == None, "None months fail"
    assert ml.month_length("February", leap_year=True) == 29, "Feb, leapyr fails"
    assert ml.month_length("February", leap_year=False) == 28, "Feb, nonlpyr fails"
