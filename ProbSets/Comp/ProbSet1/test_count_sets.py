
import count_sets as cg
import pytest

hand1 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110", "1020"]

def test_count_sets():
    assert cg.count_sets(hand1) == 6, "Number of Sets"
    with pytest.raises(ValueError) as excinfo:
        cg.count_sets(["1022", "1022", "0100", "2021",
                        "0010", "2201", "2111", "0020",
                        "1102", "0210", "2110"])
    with pytest.raises(ValueError) as excinfo:
        cg.count_sets(["1022", "1022", "0100", "2021",
                        "0010", "2201", "2111", "0020",
                        "1102", "0210", "2110", "1020"])
    with pytest.raises(ValueError) as excinfo:
        cg.count_sets(["10220", "1022", "0100", "2021",
                        "0010", "2201", "2111", "0020",
                        "1102", "0210", "2110", "1020"])
    with pytest.raises(ValueError) as excinfo:
        cg.count_sets(["1322", "1022", "0100", "2021",
                        "0010", "2201", "2111", "0020",
                        "1102", "0210", "2110", "1020"])
def test_is_set():
    a = "1022"
    b = "2021"
    c = "1102"
    d = "0020"

    assert cg.is_set(a, b, c) == False, "Not a set"
    assert cg.is_set(a, b, d) == True, "Verified set"
