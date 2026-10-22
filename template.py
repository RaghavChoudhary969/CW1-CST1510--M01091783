
"""Week 3 mini-project: IT Record Check."""


def status_of(percent):
    """Return a status based on the percentage used."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return free capacity and percentage used."""
    free = limit - value
    percent = (value / limit) * 100
    return free, percent


def print_report(hostname, used, total, free, percent, status):
    """Print the formatted record check report."""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  Used        : {used:10.2f}")
    print(f"  Total       : {total:10.2f}")
    print(f"  Free        : {free:10.2f}")
    print(f"  Percent     : {percent:10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def main():
    """Process records until the user types quit."""
    over_limit_count = 0

    while True:
        hostname = input("Hostname (or 'quit' to stop): ").strip()

        if hostname.lower() == "quit":
            break

        try:
            used = float(input("GB used: "))
            total = float(input("GB total: "))

            if total <= 0:
                print("Error: GB total must be greater than zero.")
                continue

            free, percent = check(used, total)
            status = status_of(percent)

            print_report(
                hostname, used, total, free, percent, status
            )

            if status == "OVER LIMIT":
                over_limit_count += 1

        except ValueError:
            print("Error: enter valid numeric values.")

    print(f"Records OVER LIMIT: {over_limit_count}")


if __name__ == "__main__":
    main()
