import csv
from pathlib import Path


def header_add(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = [line for line in reader]

    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['氏名', 'メールアドレス', '得点'])
        writer.writerows(data)


def main():
    p = Path("test_data")
    file_list = list(p.glob('**/*.csv'))
    for f in file_list:
        header_add(f)


if __name__ == '__main__':
    main()
