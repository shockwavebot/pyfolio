# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "tabulate",
# ]
# ///
from tabulate import tabulate

data = [["Alice", 24, "NYC"],
        ["Bob", 29, "LA"],
        ["Charlie", 35, "Chicago"]]

# Print as a table
print(tabulate(data, headers=["Name", "Age", "City"], tablefmt="fancy_grid"))
