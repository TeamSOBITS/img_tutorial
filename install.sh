#!/bin/sh

echo "install usb-cam node for ROS-Kinetic"

sudo apt-get update
sudo apt-get install ros-kinetic-usb-cam 
sudo apt-get install ros-kinetic-cv-bridge

echo "finish"
