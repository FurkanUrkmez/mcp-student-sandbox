def average_ratios(numbers):
    """Return average of 100/n for non-zero n values.

    Raises ValueError when list has no non-zero entries.
    """
    ratios = []
    for n in numbers:
        if n == 0:
            continue
        ratios.append(100 / n)

    if not ratios:
        raise ValueError("Cannot compute average_ratios with only zero values")

    return sum(ratios) / len(ratios)


if __name__ == "__main__":
    print(average_ratios([10, 5, 0]))
