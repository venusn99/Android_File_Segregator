# https://unix.stackexchange.com/a/506609
# question https://unix.stackexchange.com/questions/29245/how-to-list-files-that-were-changed-in-a-certain-range-of-time


#!/bin/bash
#We want to exit if there is no argument submitted
if [ -z "$1" ]
then
  echo no input file
  exit
fi

#destDir should be set to where ever you want the files to go
destDir="/home/user/destination"

#Get the month and year of modification time
#--format %y returns the modification date in the format:
# 2016-04-26 12:40:48.000000000 -0400
#We then take the first column, split by a white space with awk
date=`stat "$1" --format %y | awk '{ print $1 }'`

#This sets the year variable to the first column split on a - with awk
year=`echo $date | awk -F\- '{print $1 }'`
#This sets the month variable to the second column split on a - with awk
month=`echo $date | awk -F\- '{print $2 }'`
#This sets the day variable to the third column split on a - with awk
#This is commented out because I didn't want to add day to mine
#day=`echo $date | awk -F\- '{print $3 }'`

#Here we check if the destination directory with year and month exist
#If not then we want to create it with -p so the parent is created if
# it doesn't already exist
if [ ! -d $destDir/$year/$month ]
then
  mkdir -p $destDir/$year/$month || exit
fi

#This is the same as above but utilizes the day subdirectory
#Uncommented this out and comment out the similar code above
#if [ ! -d $destDir/$year/$month/$day ]
#then
#  mkdir -p $destDir/$year/$month$day || exit
#fi

#Echoing out what we're doing
#The uncommented is for just year/month and the commented line includes day
#Comment the first and uncomment the second if you need day
echo Moving $1 to $destDir/$year/$month
#echo Moving $1 to $destDir/$year/$month/$day

#Move the file to the newly created directory
#The uncommented is for just year/month and the commented line includes day
#Comment the first and uncomment the second if you need day
mv "$1" $destDir/$year/$month
#mv "$1" $destDir/$year/$month/$day
