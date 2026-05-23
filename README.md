# CS&AI ダブルモーターをゲームパッドで動かすプログラム
## 概要
レゴ エデュケーション「コンピュータサイエンス＆AI」のダブルモーターをゲームパッドで動かすプログラムです。
USBゲームパッドとパソコンとPythonの開発環境が必要です。
ライブラリはlegoeducationとpygameを使用しています。pygameがインストールできない場合は、pygame-ceをインストールしてください。
## 操作方法
 (1)ダブルモーターの電源を入れる。
 
 (2)接続カードを読み込む。
 
 (3)ダブルモーターのボタンを押してBluetoothの接続待機状態にする（ボタンが点滅）。

ソースコード内の変数「card_color」「card_serial」の内容を書き換えて、実行します。
ゲームパッドの左アナログスティックで動かします。
上下で前進／後退。左右でその場旋回をします。

BUFFALOレトロ調USBゲームパッド(BSGP801)とXbox360コントローラで動作確認しました。
## Screenshot
<img width="642" height="512" alt="Image" src="https://github.com/user-attachments/assets/43d4253a-9812-4246-a377-3b13d56bd23f" />

## Movie
https://www.youtube.com/watch?v=2oBmjyul2Cg
