#!/bin/bash


echo 'PID of current shell:' $$

echo f.arg: $1 s.arg: $2
echo t.arg: $@
echo n.arg: $#

for TOKEN in $@
do
	echo 'token' $TOKEN
done

arr=(amarillo azul laranja negro blanco)
arr2=(1 2 3 4 5)

echo ${arr[@]}

for var in {0..5}
do
	rest=$(($var % 2))
	#if [ $rest -ne 0]; then  
	if [ $rest != 0 ]; then
		echo $var 
	fi
done

vals=`expr ${arr2[1]} + ${arr2[2]}`
echo "Total value : $vals"

if [ ${arr2[1]} -le  ${arr2[2]} -a  ${arr2[2]} -ne ${arr2[3]} ]; then 
	echo 'less is more'
fi 
 
echo 'Como se dice?'
#read sign
echo "se significa" $sign

#echo 'enter first value:'
#read var1

#echo 'enter second value:'
#read var2


summ=$(( var1+var2 ))
sub=$(( var1-var2 ))
mult=$(( var1*var2 ))
div=$(( var1/1 ))

#echo "$sum"
#echo "$sub"
#echo "$mult"
#echo "$div"

boo1=$true
boo2=$false
var3=0

while [ "$var3" -ge 5 ]
do 
	var4=$var3
	echo  $var4

	while  [ "${arr2[1]}" -ne "${arr2[1]}" ];
		do
			echo "le vent nous portera"
			echo $boo1
		done
	j
done 

while [ $var3 -lt 10 ]
do 
	echo $var3 
	if [ $var3 -eq 5 ]
		then 
			break
	fi
	var3=`expr $var3 + 1`
done 

NUMS="15 25 35 45 55 65 75"

for NUM in $NUMS
	do 
		q=`expr $NUM % 3`
		if [ $q -eq 0 ]
		then
			echo -e "driple\n"
			continue
		fi
		echo "non-driple"
	done 

# filename=sw_result.txt
# vi -c  $filename <<EndOfCommands
# i
# Swift results to be shown
# ^[
# ZZ
# EndOfCommands

last=$?
echo "captured value by last command: $last"

swift_1() {
	echo "swift_1 is active"
	echo "$1 $2"
	# stuff
	
}

swift_2() {
	echo "swift_2 is active"
	# stuff
	swift_1 arg1 arg2
}
swift_2












