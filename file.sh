/bin/bash 
clear 

echo ahoi world
var="too" 
a=5 
echo $var
expr $a + 1 

read -p "Write your name : " name
read -p "Write your age  : " age 
echo $name is $age years old 



echoFunc(){
echo "echo 1,2.."
}
if [ $name = tan ]
	then echoFunc;
fi

for i in 1 2 3 4 5
do
  echo "Looping ... number $i"
done

INPUT_STRING=hello
while [ "$INPUT_STRING" != "bye" ]
do
  echo "Please type something in (bye to quit)"
  read INPUT_STRING
  echo "You typed: $INPUT_STRING"
done

while read f
do
  case $f in
        hello)          echo English    ;;
        howdy)          echo American   ;;
        gday)           echo Australian ;;
        bonjour)        echo French     ;;
        "guten tag")    echo German     ;;
        *)              echo Unknown Language: $f         ;;
   esac
done < file