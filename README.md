# PA2026
## プログラムとアルゴリズムの基礎 （放送大学）
- Fundamentals of Computer Programming and Algorithms (OUJ)
- 科目コード 1579525  (2026)

---
## 目次
- 01 プログラミング言語
- 02 演算
- 03 リストとタプル
- 04 制御
- 05 制御の応用
- 06 辞書と集合
- 07 関数
- 08 関数の応用
- 09 関数とデコレータ
- 10 文字列
- 11 クラス
- 12 ファイル
- 13 データの分析
- 14 データの可視化
- 15 機械学習

---
## Google Colab　（グーグル・コラボ）
- Google が提供するクラウド上のノートブック環境です。ブラウザだけで Python を実行でき、GPU・TPU も使えます。[https://colab.research.google.com/](https://colab.research.google.com/)

- 本科目のコード
    - [https://colab.research.google.com/github/slzp6/PA2026/blob/main/pa.ipynb](https://colab.research.google.com/github/slzp6/PA2026/blob/main/pa.ipynb)  

---
## Anaconda
- Python + ライブラリ + 環境管理ツール（conda）をまとめたパッケージ
- 公式ダウンロードページ [https://www.anaconda.com/download](https://www.anaconda.com/download)

- conda env create は、conda において 新しい環境を作るためのコマンドです。
   - 15章のTensorFlowのバージョンの関係で、python 3.11 を利用しています（2025年11月時点）。
```
conda env create --file oujpy311.yaml
```

- activate は環境を使い始める操作、deactivate は使い終わる操作 です。conda による環境切り替えは、異なるプロジェクトが異なるライブラリを必要とする場合でも、互いに干渉せずに安全に作業できるようにするための大切な仕組みです。
```
conda activate oujpy311
conda deactivate
```

---
## 利用しているパッケージ（1章〜15章）
```
h5py
imageio
keras
matplotlib
numpy
pandas
pillow
plotly
psutil
pylint
python-graphviz
seaborn
scikit-learn
tensorflow
yapf
```

---
11/2025