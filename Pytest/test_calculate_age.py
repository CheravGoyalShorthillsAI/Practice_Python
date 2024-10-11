from calculate_age import get_age

def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "2002/12/14".split("/"))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 22