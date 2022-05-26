#!/bin/sh.
current=${PWD##*/}
num=$(ls | wc -l)
two=$(($num*20/100))
echo $two
echo $current
mkdir ../../train2/$current
mv `ls | head -$two` ../../train2/$current
