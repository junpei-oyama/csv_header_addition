import random
from pathlib import Path

import faker

"""
ダミーデータをつくるためのスクリプト
===============

- ディレクトリが存在していることが前提！

## ディレクトリ構造
score_data/
├── README.md
├── school_a
│   ├── english_score.csv
│   └── science_score.csv
└── school_b
    ├── final_score.csv
    ├── semester1
    │   ├── english_score.csv
    │   ├── mathematics_score.csv
    │   └── science_score.csv
    ├── semester2
    │   ├── english_score.csv
    │   ├── mathematics_score.csv
    │   └── science_score.csv
    └── semester3
        ├── english_score.csv
        ├── mathematics_score.csv
        └── science_score.csv

"""


def main():
    fake_factory = faker.Factory.create('ja_JP')

    data_path = Path(__file__).parent / 'score_data'

    for file_path in data_path.glob('**/*.csv'):
        with file_path.open(mode='w') as f:
            for _ in range(10):
                name = fake_factory.name()
                email = fake_factory.email()
                score = random.randint(0, 100)

                print(f'{name},{email},{score}', file=f)


if __name__ == "__main__":
    main()
