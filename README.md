# Detect-eye-position

FaceMesh Eye Detection (顔の目検出)
このリポジトリには、ウェブカメラを使用して、リアルタイムで顔の目の位置を検出し、目の中心に円を描くPythonプログラムが含まれています。このプロジェクトはMediaPipeのFace Meshモデルを使用しています。

## 必要なもの
Python 3.x
OpenCV
MediaPipe
## インストール
必要なライブラリのインストール
プロジェクトに必要なライブラリをインストールするには、以下のコマンドを使用してください。
```
pip install opencv-python
pip install mediapipe
```
## 使用方法
このリポジトリをクローンまたはダウンロードします。
```
git clone https://github.com/yourusername/facemesh-eye-detection.git
```
もしくは、ZIPファイルとしてダウンロードし、適当なディレクトリに解凍します。

ターミナルでプロジェクトディレクトリに移動します。
```
cd facemesh-eye-detection
```
Pythonスクリプトを実行します。
```
python eye_detection.py
```
ウェブカメラが起動し、顔の目の位置に円が描かれます。プログラムを終了するには、qキーを押してください。

## 注意事項
このプログラムはウェブカメラを必要とします。使用するカメラにアクセスできることを確認してください。
実行中に問題が発生した場合は、Pythonと各ライブラリが正しくインストールされているか確認してください。
