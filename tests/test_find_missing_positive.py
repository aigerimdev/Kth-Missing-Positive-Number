from missing_num.main import kth_missing_positive_number

def test_kth_missing_positive_number_finds_num_before_entire_given_list():
    # Arrange
    list = [2,3,4,7,11]
    k = 1

    # Act
    answer = kth_missing_positive_number(list, k)

    # Assert
    assert 1 == answer

def test_kth_missing_number_finds_num_near_end_of_list():
    # Arrange
    list = [2,3,4,7,11]
    k = 5

    # Act
    answer = kth_missing_positive_number(list, k)
    
    # Assert
    assert 9 == answer

def test_kth_missing_positive_number_finds_num_after_entire_given_list():
    # Arrange
    list = [1,2,3,4]
    k = 2

    # Act
    answer = kth_missing_positive_number(list, k)
    
    # Assert
    assert 6 == answer

def test_kth_missing_positive_number_2nd_number_before_list_starts():
    # Arrange
    list = [3,4,5,7,11]
    k = 2

    # Act
    answer = kth_missing_positive_number(list, k)
    
    assert 2 == answer
    
def test_empty_array():
    arr = []
    k = 4
    assert kth_missing_positive_number(arr, k) == 4


def test_starting_after_1():
    arr = [10, 11, 12]
    k = 3
    # missing: [1, 2, 3, ...]
    assert kth_missing_positive_number(arr, k) == 3


def test_large_k():
    arr = [2, 3, 4]
    k = 100
    assert kth_missing_positive_number(arr, k) == 103

def test_no_missing_until_end():
    arr = [1, 2, 3, 4, 5]
    k = 1
    # next missing is 6
    assert kth_missing_positive_number(arr, k) == 6


def test_one_element_k_in_middle():
    arr = [3]
    k = 2
    # missing: [1, 2]
    assert kth_missing_positive_number(arr, k) == 2
#-------------------------------------------------------/



# example input 1: arr=[], k=4
# expected output 1: 4

# example input 2: arr=[1, 2, 3], k=3
# expected output 2: 6

# example input 2: arr=[2,3,4,7,11], k=5
# expected output 2: 9

# Example input 1: arr = [], k = 4
# Expected output: 4

# Example input 2: arr = [1, 2, 3], k = 3
# Expected output: 6

# Example input 3: arr = [2, 3, 4, 7, 11], k = 5
# Expected output: 9

# test 1
def test_empty_array():  
    # Arrange
    arr = []
    k = 4
    # Act
    result = kth_missing_positive_number(arr, k)
    # Assert
    assert result == 4

# test 2
def test_no_missing_until_end():
    # Arrange
    arr = [1, 2, 3]
    k = 3
    # Act
    result = kth_missing_positive_number(arr, k)
    # Assert
    assert result == 6
    
# test 3
def test_finds_missing_num_before_arr_ends():
    # Arrange
    arr = [2, 3, 4, 7, 11]
    k = 5
    # Act
    result = kth_missing_positive_number(arr, k)
    # Assert
    assert result == 9

# test 4
def test_start_large_k_large():
    arr = [100, 200, 300]
    k = 10
    # missing: [1–99] -> 10th = 10
    assert kth_missing_positive_number(arr, k) == 10

# test 5
def test_sparse_array():
    arr = [1, 10, 20]
    k = 5
    # missing: [2,3,4,5,6,...] -> 5th = 6
    assert kth_missing_positive_number(arr, k) == 6
    
# test 6
def test_k_equal_1():
    arr = [2, 3, 4]
    k = 1
    # missing: [1]
    assert kth_missing_positive_number(arr, k) == 1


