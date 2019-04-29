#!/bin/bash
ROBOT=43

echo $ROBOT

echo $1
echo $2
echo $3
echo $@
TMP='bad robot'

DoRobot()
{
  echo $1
  TMP=$1
}

DoMath()
{
	if [[ $1 -eq 42 ]]
	then
		echo 'life, the univers, and everything'
	fi
	if [[ $1 -lt 42 ]]
	then
		echo 'less than 42'
	elif [[ $1 -gt 100 ]]
	then 
		echo 'above 100'
	else
		echo 'between 42 and 100'
	fi
}
ShowUsage()
{
	echo '-----------------------'
	echo '-----------------------'
	echo '-------help file-------'
	echo '-----------------------'
	echo '-----------------------'
}
case "$1" in
	'robots' )
		DoRobot $@
	;;
	'are' )
		DoAre
	;;
	'math' )
		DoMath $2
	;;
	*)
		ShowUsage
		exit 1
	;;
esac

echo $TMP
exit 0
