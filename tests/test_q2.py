from alvanon_test.q2 import Solution


def test_find_matches_normal_case_1():
    s = Solution()
    team_a = [1, 2, 3]
    team_b = [2, 4]
    matches = s.find_matches(team_a, team_b)
    assert matches == [2, 3]


def test_find_matches_normal_case_2():
    s = Solution()
    team_a = [1, 2, 3]
    team_b = [2, 4, 5, 6]
    matches = s.find_matches(team_a, team_b)
    assert matches == [2, 3, 3, 3]


def test_find_matches_with_one_empty_list_1():
    s = Solution()
    team_a = []
    team_b = [2, 4, 5, 6]
    matches = s.find_matches(team_a, team_b)
    assert matches == [0, 0, 0, 0]


def test_find_matches_with_one_empty_list_2():
    s = Solution()
    team_a = [1, 2, 3]
    team_b = []
    matches = s.find_matches(team_a, team_b)
    assert matches == []


def test_find_matches_with_two_empty_lists():
    s = Solution()
    team_a = []
    team_b = []
    matches = s.find_matches(team_a, team_b)
    assert matches == []


def test_find_matches_with_non_integer_elements():
    """
    If team_a or team_b contain non-integer element, then find_matches should only return []
    """
    s = Solution()
    team_a = ["243"]
    team_b = [1, 2, 3, 4]
    matches = s.find_matches(team_a, team_b)
    assert matches == []


def test_find_matches_with_none():
    """
    If team_a or team_b is None, then find_matches should only return []
    """
    s = Solution()
    team_a = None
    team_b = None
    matches = s.find_matches(team_a, team_b)
    assert matches == []
