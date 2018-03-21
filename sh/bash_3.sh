#!/bin/bash


echo 'Enter 2 integers'
read var1
read var2

if [ $var1 -gt $var2 ]; then
	echo "X is greater than Y"
elif [[ $var1 -eq $var2 ]]; then
	echo 'X is equals to Y'
elif [[ $var1 -lt $var2  ]]; then
	echo 'X is less than Y'
fi

echo 'Y/N'
read var3
if [ $var3 == 'y' -o $var3 == 'Y' ]; then
	echo 'YES'
elif [ $var3 == 'n' -o $var3 == 'N' ]; then
	echo 'NO'
fi

echo 'Bermuda Triangle'
read edge1
read edge2
read edge3

if [[ $edge1 == edge2 && $edge2 == $edge3 ]]
	then
	echo "EQUILATERAL"
elif [[ $edge1 == $edge2 || $edge2 == $edge3 || $edge1 == $edge3 ]]
	then 
	echo "ISOSCELES"
else
	echo "SCALENE"
fi



