import csv
import statistics
from collections import Counter

filename = "fb_ads_president_scored_anon.csv"

with open(filename, mode="r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)

print(f"Dataset loaded successfully!")
print(f"Total rows: {len(data)}")
print(f"Total columns: {len(data[0])}")

print("\nColumn Names:")
for column in data[0]:
    print(column)


MISSING_VALUES = {"", "NA", "N/A", "NULL", "null", "None"}

missing_counts = {}

for column in data[0]:
    count = 0

    for row in data:
        value = row[column].strip()

        if value == "" or value.upper() in {"NA", "N/A", "NULL", "NONE"}:
            count += 1

    missing_counts[column] = count

print("\nMissing Values Per Column:")

for column, count in missing_counts.items():
    print(f"{column}: {count}")


data_types = {}

for column in data[0]:
    numeric = True

    for row in data:
        value = row[column].strip()

        if value == "" or value.upper() in {"NA", "N/A", "NULL", "NONE"}:
            continue

        try:
            float(value)
        except ValueError:
            numeric = False
            break

    if numeric:
        data_types[column] = "Numeric"
    else:
        data_types[column] = "Non-numeric"

print("\nInferred Data Types:")

for column, dtype in data_types.items():
    print(f"{column}: {dtype}")


def compute_numeric_stats(values):
    """
    Compute descriptive statistics for a numeric column.
    Assumes 'values' contains only valid numeric values.
    """

    if len(values) == 0:
        return {
            "Count": 0,
            "Mean": None,
            "Minimum": None,
            "Maximum": None,
            "Standard Deviation": None,
            "Median": None
        }

    stats = {
        "Count": len(values),
        "Mean": statistics.mean(values),
        "Minimum": min(values),
        "Maximum": max(values),
        "Standard Deviation": statistics.stdev(values) if len(values) > 1 else 0,
        "Median": statistics.median(values)
    }

    return stats


print("\nNumeric Column Statistics:")

for column in data[0]:

    if data_types[column] == "Numeric":

        numeric_values = []

        for row in data:
            value = row[column].strip()

            if value == "" or value.upper() in {"NA", "N/A", "NULL", "NONE"}:
                continue

            numeric_values.append(float(value))

        stats = compute_numeric_stats(numeric_values)

        print(f"\nColumn: {column}")
        print(f"Count: {stats['Count']}")
        print(f"Mean: {stats['Mean']}")
        print(f"Minimum: {stats['Minimum']}")
        print(f"Maximum: {stats['Maximum']}")
        print(f"Standard Deviation: {stats['Standard Deviation']}")
        print(f"Median: {stats['Median']}")


def compute_categorical_stats(values):
    """
    Compute descriptive statistics for a non-numeric column.
    Assumes missing values have already been removed.
    """

    if len(values) == 0:
        return {
            "Count": 0,
            "Unique Values": 0,
            "Mode": None,
            "Mode Frequency": 0,
            "Top 5 Values": []
        }

    counts = Counter(values)

    mode, frequency = counts.most_common(1)[0]

    stats = {
        "Count": len(values),
        "Unique Values": len(counts),
        "Mode": mode,
        "Mode Frequency": frequency,
        "Top 5 Values": counts.most_common(5)
    }

    return stats


print("\nCategorical Column Statistics:")

for column in data[0]:

    if data_types[column] == "Non-numeric":

        categorical_values = []

        for row in data:
            value = row[column].strip()

            if value == "" or value.upper() in {"NA", "N/A", "NULL", "NONE"}:
                continue

            categorical_values.append(value)

        stats = compute_categorical_stats(categorical_values)

        print(f"\nColumn: {column}")
        print(f"Count: {stats['Count']}")
        print(f"Unique Values: {stats['Unique Values']}")
        print(f"Mode: {stats['Mode']}")
        print(f"Mode Frequency: {stats['Mode Frequency']}")

        print("Top 5 Values:")

        for i, (value, frequency) in enumerate(stats["Top 5 Values"], start=1):
            print(f"  {i}. {value}: {frequency}")
