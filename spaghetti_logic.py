def calculate_total(amount, multiplier=1.15):
    """Return the scaled value for a given amount."""
    return amount * multiplier


def format_total(amount):
    """Format a numeric amount as a human-readable total string."""
    return f"Total: {amount:.2f}"


def write_log(values, path="log.txt", mode="a", encoding="utf-8"):
    """Append a list of values to a log file."""
    with open(path, mode, encoding=encoding) as f:
        f.write(str(values) + "\n")


def process_data(data, multiplier=1.15):
    """Process raw data values by applying a multiplier and returning results."""
    return [calculate_total(d, multiplier) for d in data]


def process_and_log(data, log_path="log.txt", multiplier=1.15, to_console=True):
    """Process data, optionally print formatted totals, and write results to a log."""
    results = process_data(data, multiplier=multiplier)

    if to_console:
        for value in results:
            print(format_total(value))

    write_log(results, path=log_path)
    return results
