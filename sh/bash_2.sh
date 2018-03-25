#!/bin/bash

# d-delete, p-print, s/pattern1/pattern2/ - subsitutes the pattern1 with pattern2
#cat food | sed '2,5d' | more 
#cat food | sed '2,+5d' | more
#cat food | sed '2,5d!' | more
#cat food | sed '2~5d' | more
#cat food | sed -n '2,5p' | more

# g enables global search, without it only first occurence will be replaced.
#cat food | sed 's/Sweet/Sour/g' >  sour.txt

#quiet subsitution on lines  7-10
cat food | sed '7,10s/Sweet/Sour/g' >  sour7.txt

#taking first 3 letters into parenthesis
cat food | sed -e 's/^[[:alpha:]][[:alpha:]][[:alpha:]]/(&)/g' > fooda.txt
cat food | sed -e 's/[[:space:]]/(&)/g' > foods.txt
cat food | sed -e 's/[[:space:]]\{2\}/(&)/g'  > food3.txt
cat food | sed -e 's/[[:space:]]/ -gap- /g'  > food2.txt





