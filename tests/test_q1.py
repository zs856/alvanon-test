from alvanon_test.q1 import Solution


def test_odd_with_positive_numbers():
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == [3, 4, 1, 5, 2]
    # 3*4/1*5/2 ==30
    assert u == 30


def test_odd_with_negative_numbers():
    s = Solution()
    nums = [-1, -2, -3, -4, -5]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == [-3, -2, -5, -1, -4]
    # -(3 * 2 / 5 * 1 / 4) == -0.3
    assert u == -0.3


def test_even_with_positive_numbers():
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == [2, 3, 1, 4, 5, 6]
    # 2*3/1*4*5*6 == 720
    assert u == 720


def test_even_with_negative_numbers():
    s = Solution()
    nums = [-1, -2, -3, -4, -5, -6]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == [-6, -5, -1, -4, -3, -2]
    # equal to -(5*4/6*1*2*3) == 720
    assert u == 720


def test_even_mixed_with_positive_and_negative_numbers():
    s = Solution()
    nums = [1, 2, 3, -4, -5, -6]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == [-5, -4, -6, 1, 2, 3]
    # equal to -(5*4/6*1*2*3) == -20.0
    assert u == -20.0


def test_odd_mixed_with_positive_and_negative_numbers():
    s = Solution()
    nums = [1, 2, 3, -4, -5]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == [-5, -4, 1, 3, 2]
    # equal to (5*4/1*3/2) == 30
    assert u == 30


def test_numbers_with_zero():
    # If there are 0s in the input array, the U value is 0 and \
    # the input array remains unchanged.
    s = Solution()
    nums = [-5, 0, 0, 0, 0]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == nums
    assert u == 0


def test_empty_input():
    # If there are no elements in the input array, the U value is None and \
    # the input array remains unchanged.
    s = Solution()
    nums = []
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == nums
    assert u == None


def test_numbers_with_non_integer_elements():
    # If there are non-integer elements in the input array, the U value is None and \
    # the input array remains unchanged.
    s = Solution()
    nums = [1, 2, 3, "c", "a"]
    res, u = s.calculate_maximum_u(nums=nums)
    assert res == nums
    assert u == None
