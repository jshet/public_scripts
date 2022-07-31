import roundrobin 

# tests

def test_duplicates():
    assert roundrobin.make_pairs([1,1,2]) == 0
