#!/bin/bash
# SPDX-FileCopyrightText: 2026 Kota Iwasaki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg system_monitor.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep 'Listen: 10'
