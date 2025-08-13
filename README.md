# daikinpy
ダイキン製のエアコンを操作するコード

## How to use

1. daikin.pyのDaikinクラスの設定をする。TerminalidとPortを何らかの手段で取得する。(mitm等)
2. SendQueryのheaderを書き換える。(user-agent等)

## 運転モード
パワーオフ→0<br>
パワーオン→1<br>

| mode   | 値 |
|--------|----|
| 快適自動 | 1  |
| 除湿   | 2  |
| 冷房   | 3  |
| 暖房   | 4  |
| 送風   | 6  |