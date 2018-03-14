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

echo 'enter first value:'
read var1

echo 'enter second value:'
read var2


sum=$(( var1+var2 ))
sub=$(( var1-var2 ))
mult=$(( var1*var2 ))
div=$(( var1/var2 ))

echo "$sum"
echo "$sub"
echo "$mult"
echo "$div"
