##############
# Question 1 #
##############


def count_matching_bracket(s):
    # Your code here
    pass


# Test cases
def test_q1():
    print("########## Q1 ##########")
    w = 25

    _ = count_matching_bracket("(())")
    print(_ == 2, 'count_matching_bracket("(())")'.ljust(w), repr(_), sep="\t")

    _ = count_matching_bracket("()()")
    print(_ == 2, 'count_matching_bracket("()()")'.ljust(w), repr(_), sep="\t")

    _ = count_matching_bracket("(()()()())")
    print(_ == 5, 'count_matching_bracket("(()()()())")'.ljust(w), repr(_), sep="\t")

    _ = count_matching_bracket("(()()()(()))")
    print(_ == 6, 'count_matching_bracket("(()()()(()))")'.ljust(w), repr(_), sep="\t")

    _ = count_matching_bracket("(()()()(()")
    print(_ == 4, 'count_matching_bracket("(()()()(()")'.ljust(w), repr(_), sep="\t")

    _ = count_matching_bracket("((((")
    print(_ == 0, 'count_matching_bracket("((((")'.ljust(w), repr(_), sep="\t")

    _ = count_matching_bracket("))")
    print(_ == 0, 'count_matching_bracket("))")'.ljust(w), repr(_), sep="\t")


# Uncomment to test question 1
# test_q1()


##############
# Question 2 #
##############


def count_adjacent_pairs(n):
    # Your code here
    pass


# Test cases
def test_q2():
    print("########## Q2 ##########")
    w = 25

    _ = count_adjacent_pairs(1122)
    print(_ == 2, "count_adjacent_pairs(1122)".ljust(w), repr(_), sep="\t")

    _ = count_adjacent_pairs(1221)
    print(_ == 1, "count_adjacent_pairs(1221)".ljust(w), repr(_), sep="\t")

    _ = count_adjacent_pairs(12223123)
    print(_ == 2, "count_adjacent_pairs(12223123)".ljust(w), repr(_), sep="\t")

    _ = count_adjacent_pairs(12233322111)
    print(_ == 6, "count_adjacent_pairs(12233322111)".ljust(w), repr(_), sep="\t")

    _ = count_adjacent_pairs(111111111)
    print(_ == 8, "count_adjacent_pairs(111111111)".ljust(w), repr(_), sep="\t")

    _ = count_adjacent_pairs(1)
    print(_ == 0, "count_adjacent_pairs(1)".ljust(w), repr(_), sep="\t")


# Uncomment to test question 2
# test_q2()
