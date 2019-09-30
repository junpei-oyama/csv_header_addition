# README

## Background
複数の学校における試験の結果をCSVファイルとして管理しています。
一生懸命CSVファイルをつくったのですが、うっかりheader(一行目)を書き忘れてしまいました。

たすけて〜

## ディレクトリ構造
- データは下記のような構造で管理しています。
- csvファイルはすべて試験の結果です。

```
score_data/
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
```


## Goal
- すべてのcsvファイルにheaderを追加する。
    - headerは `氏名,メールアドレス,得点` とすること。
- データ準備にはこのリポジトリをクローンかzipをダウンロードで対応してください。


### 現状のCSVファイルの中身(抜粋)
```csv
西之園 太一,atsushisasada@yoshida.org,13
渡辺 康弘,unohiroshi@hotmail.com,46
斉藤 稔,hsasaki@kano.jp,64
```

### こうなればOK(headerが正しく挿入されている)
```csv
氏名,メールアドレス,得点
西之園 太一,atsushisasada@yoshida.org,13
渡辺 康弘,unohiroshi@hotmail.com,46
斉藤 稔,hsasaki@kano.jp,64
```

## Hint
- ファイルに対して書き込みなどを行う場合はバックアップをとりましょう！
- 利用すると便利なモジュールを紹介しておきます
  - パス関連 → [pathlib](https://docs.python.org/ja/3/library/pathlib.html)
  - ファイル操作 → [shutil](https://docs.python.org/ja/3/library/shutil.html)



以上
