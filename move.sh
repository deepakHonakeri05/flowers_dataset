#!/bin/sh.
current=${PWD##*/}
num=$(ls | wc -l)
two=$(($num*20/100))
echo $two
echo $current
mv `ls | head -$two` ../../test/$current