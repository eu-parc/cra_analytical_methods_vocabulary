import csv
import yaml

input_csv = "methods.csv"      # adjust if needed
output_yaml = "methods.yaml"

methods = []

with open(input_csv, newline="", encoding="cp1250") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")  # change to "," if needed

    header = next(reader)  # skip header row
    print("HEADER:", header)

    for row in reader:
        # safety check
        if len(row) < 6:
            continue

        parent_method = row[2].strip()
        name_alter = row[3].strip()
        name = row[4].strip()
        method_id = row[5].strip()

        # skip rows without ID
        if not method_id:
            continue

        method_entry = {
            "id": method_id.lower(),
            "name": name if name else name_alter,
            "parent_method": parent_method,
            "unique_name": method_id
        }

        methods.append(method_entry)

print(f"Converted {len(methods)} methods")

with open(output_yaml, "w", encoding="utf-8") as yamlfile:
    yaml.dump(
        methods,
        yamlfile,
        allow_unicode=True,
        sort_keys=False
    )