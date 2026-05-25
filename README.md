# ダブルモーターをゲームパッドで動かすプログラム
<img width="887" height="320" alt="Image" src="https://github.com/user-attachments/assets/46e46b97-2367-4304-bdf4-be36b80f28ed" />

## 概要
「レゴ エデュケーション コンピュータサイエンス＆AI」のダブルモーターをパソコン+ゲームパッドで動かすプログラムです。
パソコンにはPythonの開発環境が必要です。
ライブラリは「legoeducation」と「pygame」を使用しています。「pygame」がインストールできない場合は「pygame-ce」をインストールしてください。

BUFFALOレトロ調USBゲームパッド(BSGP801)とXbox360コントローラで動作確認しました。
## 操作方法
(1)ダブルモーターの電源を入れる。
 
(2)接続カードを読み込む。
 
(3)ダブルモーターのボタンを押してBluetoothの接続待機状態にする（ボタンが点滅）。

(4)ソースコード内の変数「card_color」「card_serial」の内容を書き換えて、実行する。

(5)ゲームパッドの左スティックで動かします。上下方向で前進／後退。左右方向でその場旋回をします。

## Screenshot
<img width="642" height="512" alt="Image" src="https://github.com/user-attachments/assets/43d4253a-9812-4246-a377-3b13d56bd23f" />

## Movie
https://www.youtube.com/watch?v=2oBmjyul2Cg
