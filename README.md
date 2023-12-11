# jpg2png-for-NAI

## リリースノート
* 2023/12/10 初版リリース。
* 2023/12/12 日付情報の維持に対応。Windowsの場合は更新日時と作成日時、Mac, Linuxの場合は更新日時が変換後の画像に引き継がれます。

## 説明
png2jpg-for-a1111-and-NAI(旧名称:png2jpg改)でJPEG変換したNovelAI生成画像はNovelAIやAutomatic1111に取り込ませることができませんが、本ツールでPNGに変換することで、元のPNG画像と同様にNovelAIやAutomatic1111に取り込ませることが可能になります。

### 1. png2jpg-for-a1111-and-NAI(旧名称:png2jpg改)でJPEG変換したNovelAI生成画像について
PNG画像に変換しメタデータを元のPNG画像と同じ形式に変換します。  
変換したPNG画像はNovelAIやAutomatic1111にメタデータを取り込ませることが可能です。

### 2. png2jpg-for-a1111-and-NAI(旧名称:png2jpg改)または、png2jpg（過去バージョン）でJPEG変換したAutomatic1111生成画像について
png2jpg-for-a1111-and-NAI(旧名称:png2jpg改)または、png2jpg（過去バージョン）でJPEG変換したAutomatic1111生成画像はAutomatic1111で利用可能なため、基本的に本ツールを使用する必要はありません。  
仮に本ツールで変換した場合でもAutomatic1111で利用可能な形式に変換されますので利便性に影響はありません。

### 3. 日付情報について
元画像の日付情報を変換後の画像に引き継ぎます。  
Windows: 更新日時, 作成日時  
Mac, Linux: 更新日時

## 前提
Python環境

## 準備
以下のライブラリを使用するため、入っていない場合はインストールします。
* PIL  
pip install pillow

* piexif  
pip install piexif

Windowsの場合  
* pywin32  
pip install pywin32

## 使い方
1. inputsフォルダに変換したいJPEG画像(png2jpg-for-a1111-and-NAI(旧名称:png2jpg改)で変換した画像）を入れます。※JPEG画像の拡張子は".jpg"である必要があります。
2. jpg2png.batをダブルクリックします。
3. outputsフォルダにPNG画像が保存されます。

## 設定変更等
処理完了後にコマンドラインを閉じないようにしたい場合はjpg2png.bat内の@REM pauseのコメントアウトを外してください。
