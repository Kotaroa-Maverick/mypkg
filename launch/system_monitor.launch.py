#!/usr/bin/python3
# SPDX-FileCopyrightText: 2026 Kota Iwasaki
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='talker',
            name='cpu_talker'
        ),
        Node(
            package='mypkg',
            executable='listener',
            name='cpu_listener'
        ),
    ])
