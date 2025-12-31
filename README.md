# ロボットシステム学-課題2
このパッケージは、ROS 2を使用してPCのCPU使用率をリアルタイムで監視し、その様子の配信・表示を行うシステムです。
- `talker`ノードがシステムのCPU負荷を取得し、トピック経由で配信します。
- `listener`ノードがそのデータを受信し、負荷状況に応じてステータス（NORMAL/HIGH LOAD）を判定して表示します。

# ノードの説明
### cpu_talker (talker.py)
- 役割: システムのCPU使用率を取得して配信する。
- 配信トピック: `/cpu_usage` (型: `std_msgs/Float64`)
- 依存ライブラリ: `psutil` (Pythonライブラリ)

### cpu_listener (listener.py)
- 役割: 配信されたCPU使用率を受信し、画面に表示する。
- 判定ロジック: 使用率が80%を超えると `[HIGH LOAD!]` と警告を表示します。


# 使い方
gitとpsutilをインストールしたのち、ローンチファイルを使用して、配信側と受信側の両方のノードを同時に立ち上げてください。
<pre>
$ sudo apt install git
$ sudo apt update
$ sudo apt install python3-psutil
$ ros2 launch mypkg system_monitor.launch.py
</pre>

# 動作環境
- Ubuntu 22.04.5 LTS

# ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025
- © 2025 Kota Iwasaki
