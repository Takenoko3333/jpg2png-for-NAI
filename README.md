# jpg2png-for-NAI

## リリースノート
2023/12/10 初版リリース。

## 説明
png2jpg改でJPEG変換したNovelAI生成画像をPNG画像に変換します。
png2jpg改でJPEG変換した画像はNovelAIやAutomatic1111に取り込ませることができませんが、本ツールでPNGに変換することで、元のPNG画像と同様にNovelAIやAutomatic1111に取り込ませることが可能になります。

### 1. png2jpg改でJPEG変換したNovelAI生成画像について
PNGに変換しメタデータを元のPNG画像と同じ形式に戻します。
NovelAIやAutomatic1111にメタデータを取り込ませることが可能になります。

### 2. png2jpgまたは、png2jpg改でJPEG変換したAutomatic1111生成画像について
png2jpg改でJPEG変換したAutomatic1111生成画像はAutomatic1111で利用可能なため、基本的に本ツールを使用する必要はありません。仮に本ツールで変換した場合でもAutomatic1111で利用可能な形式に変換されますので利便性に影響はありません。

## 前提
Python環境

## 準備
以下のライブラリを使用するため、入っていない場合はインストールします。
* PIL  
pip install pillow

* piexif  
pip install piexif

## 使い方
1. inputsフォルダに変換したいJPG画像（png2jpまたは、png2jpg改でJPEG変換した画像）を入れます。
2. jpg2png.batをダブルクリックします。
3. outputsフォルダにPNG画像が保存されます。

## 設定変更等
処理完了後にコマンドラインを閉じないようにしたい場合はjpg2png.bat内の@REM pauseのコメントアウトを外してください。
