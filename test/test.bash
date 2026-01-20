#!/bin/bash
# SPDX-FileCopyrightText: 2026 Kota Iwasaki
# SPDX-License-Identifier: BSD-3-Clause

dir=$(pwd)
[ -d "$dir/ros2_ws" ] && dir="$dir/ros2_ws"

cd $dir

source /opt/ros/humble/setup.bash

colcon build
if [ -f install/setup.bash ]; then
    source install/setup.bash
fi

timeout 10 ros2 launch mypkg system_monitor.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log

if grep -q 'CPU Usage' /tmp/mypkg.log; then
    echo "SUCCESS"
    exit 0
else
    echo "FAILED"
    exit 1
fi
