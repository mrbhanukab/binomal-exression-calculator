def form_series(co_a, co_b, n):
    """
    This method creates the Binomial Theorem Series.

    :param co_a: coefficient of a
    :param co_b: coefficient of b
    :param n: power of the equation
    :return: None
    """
    def formatting(next_term, coeffs):
        """
        This is an inner function which formats the
        terms of the binomial series.

        :param next_term: coefficient of next term
        :param coeffs: powers of a and b
        :return: formatted term
        """
        if next_term == 1:
            coeffs.insert(0, "")
        else:
            coeffs.insert(0, next_term)

        if coeffs[1] == "^0" and coeffs[2] == "^0":
            return coeffs[0]
        elif coeffs[1] == "^0":
            return "{}b{}".format(coeffs[0], coeffs[2])
        elif coeffs[2] == "^0":
            return "{}a{}".format(coeffs[0], coeffs[1])
        elif coeffs[1] == "^1" and coeffs[2] == "^1":
            return "{}ab".format(coeffs[0])
        elif coeffs[1] == "^1":
            return "{}ab{}".format(coeffs[0], coeffs[2])
        elif coeffs[2] == "^1":
            return "a{}b".format(coeffs[0], coeffs[1])
        return "{}a{}b{}".format(coeffs[0], coeffs[1], coeffs[2])

    # Initializing a list named as `series`
    series = list()

    # Calculating the First Term, Formatting it
    # and Appending it to our Series
    first_term = pow(co_a, n)
    coeffs = ["^" + str(n), "^0"]
    series.append(formatting(first_term, coeffs) + "  +  ")

    next_term = first_term

    # Calculating, Formatting and Appending
    # the remaining terms.
    for i in range(1, n + 1):
        # We can find next term using the
        # previous term and the formula
        # mentioned below.
        next_term = int(next_term * co_b * (n - i + 1) / (i * co_a))

        # Pre-formatted list creation
        coeffs = ["" if x == 1 else "^" + str(x) for x in [n - i, i]]

        # Append till last term is not reached
        if i != n:
            series.append(formatting(next_term, coeffs) + "  +  ")

        # Append the last term.
        else:
            series.append(formatting(next_term, coeffs))

    # Joining the series as a string and printing it.
    print("".join(series))


if __name__ == "__main__":
    # Taking inputs
    print("( a + b ) ^ n")
    co_a = int(input("Enter the coefficient of a: "))
    co_b = int(input("Enter the coefficient of b: "))
    n = int(input("Enter n: "))
    print("({}a+{}b)^{}  =  ".format(co_a, co_b, n),end=" ")

    # Calling the Function
    form_series(co_a, co_b, n)