import csv

def save_csv(file_path: str, dict_list: list[dict]) -> None:
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict_list[0].keys())
        writer.writeheader()
        for item in dict_list:
            writer.writerow(item)