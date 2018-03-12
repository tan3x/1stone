#!/bin/bash

echo 'ahoi'

for var in {0..100}
do
	rest=$(($var % 2))
	#if [ $rest -ne 0]; then  
	if [ $rest != 0 ]; then
		echo $var 
	fi
done 
echo 'Como se dice?'
read var

echo "se dice" $var
