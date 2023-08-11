
# a = b   assignes new value for 'a' from 'b'
# a == b  compares the value or equality

# True = 1
# False = 0

# Example:
    # '5 and True' = True = 1
        # Numbers that are not 0 are considered True.
    # '3 + False' = 3 + 0 = 3

# % - remainder of:
    # 101 % 4 = 1
# // - floor division:
    # 101 // 4 = 25

# difference, intersection, union, simmetric difference:
list_a = [5.6, 6.7, 9.2]
list_b = [6.7, 5.6, 9.4]
# set(list_a) — set(list_b) - difference - items in list_a that are not in list_b: {9.2}
# set (list_a) ^ set (list_b) - simmetric difference - items in list_a and list_b that do not appear in both lists: {9.2, 9.4}
# set(list_a) & set(list_b) - intersection - items that are in both list_a & list_b: {5.6, 6.7}
# set (list_a) | set (list_b) - union - items that are unique to both lists: {5.6, 6.7, 9.2, 9.4}

# 'is' operator:
# 1.
    # a = 45
    # b = 45
    # a is b -> True
#  5. 
    # a = 'Test'
    # b = 'Test'
    # print(a is b) -> True
    # print(a == b) -> True
    # print(a = b) -> Error
# 3. The following print statement will not display True:
    # c = [2, 4, 7]
    # d = [2, 4, 7]
    # c is d -> False!!!!
        # c and d are equal, but not identical. These lists are MUTABLE and for that reason the interpreter will place
        # them in separate locations in memory.
# 2.
    # testl = "This is a test"
    # test2 = 'This is a test‘.upper()
    # test1 is test2 -> False
# 4. 
    # 'h' in "Python" -> True




