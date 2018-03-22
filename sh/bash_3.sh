#!/bin/bash


# echo 'Enter 2 integers'
# read var1
# read var2

# if [ $var1 -gt $var2 ]; then
# 	echo "X is greater than Y"
# elif [[ $var1 -eq $var2 ]]; then
# 	echo 'X is equals to Y'
# elif [[ $var1 -lt $var2  ]]; then
# 	echo 'X is less than Y'
# fi

# echo 'Y/N'
# read var3
# if [ $var3 == 'y' -o $var3 == 'Y' ]; then
# 	echo 'YES'
# elif [ $var3 == 'n' -o $var3 == 'N' ]; then
# 	echo 'NO'
# fi

# echo 'Bermuda Triangle'

# read edge1
# read edge2
# read edge3

# if [[ $edge1 == $edge2 && $edge2 == $edge3 ]]
# 	then
# 	echo "EQUILATERAL"
# elif [[ $edge1 == $edge2 || $edge2 == $edge3 || $edge1 == $edge3 ]]
# 	then 
# 	echo "ISOSCELES"
# else
# 	echo "SCALENE"
# fi

# read calc
# echo $calc | bc -l | xargs printf '%.3f'

# echo 'number of integers:'
# read nri
# cnt=0
# total=0
# while [ $nri -lt 500 ]
# do
# 	while [ $cnt -lt $nri ]
# 	do
# 		echo 'enter integers'
# 		read -r val
# 		total=$((total+val))
# 		((cnt++)) 
# 	done
# 	printf "%.3f" $(echo $total/$nri | bc -l) 
# 	break 
# done

 
# while read line 
# do
# 	echo $line | cut -c3 - #just third letter
# 	echo $line | cut -c2,7 - #second and seventh letter
# 	echo $line | cut -c1-4 - #first four letters
# 	echo $line | cut -c2-7 - #between second and seventh
# 	echo $line | cut -c2-7 - #between second and seventh
# 	echo $line | cut -c13- #until end
# 	echo $line | cut -d' ' -f4
# 	echo $line | cut -d' ' -f1-3 #first 3 words
# 	echo $line | cut -f2- #from second until end / TAB is default delimiter.

# 	awk -F "   " '{print $1 $2 $3}' city
# 	#head -n 20 city
# 	head -c20 city
# 	head -22 | tail -11 city
# 	break 
# done

#TR
# tr 'S' 'J' < food
# tr -d [:lower:] < food
# tr -d [:upper:] < food
# tr -s ' ' < food

#SORT 
# cat food | sort -k1 #lexicographical order 
# cat food | sort -r -k1 #reverse lexicographical order 
# cat numbers | sort -g #floating sort
# cat numbers | sort -r -g #floating sort

# sort -t $'\t' -k2,2 -n -r temp # TAB seperated
# sort -t $'|' -k2,2 -n -r  temp # | seperated 

# uniq -d dupl
# uniq -c dupl
# uniq -ci | cut -c7- dupl # case sensitive and eliminates first gap
# uniq -u dupl  #display lines that are not repeated 


paste -s food 
paste -s -d '\t\t\n' food 




