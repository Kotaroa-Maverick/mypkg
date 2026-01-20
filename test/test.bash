#!/bin/bash
# SPDX-FileCopyrightText: 2026 Kota Iwasaki
# SPDX-License-Identifier: BSD-3-Clause

dir=$(dirname $0)/../..
cd $dir

source /opt/ros/humble/setup.bash

colcon build

source install/setup.bash

timeout 10 ros2 launch mypkg system_monitor.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log

if grep -q 'CPU Usage' /tmp/mypkg.log; then
    echo "SUCCESS"
    exit 0
else
    echo "FAILED"
    exit 1
fi
