#!/bin/env bash

files=$1
if [[ -n $files ]]; then
	git add $files
	echo "Added file(s) $1"
fi
echo ""
printf "What's the commit type ?\n ➛ feat: new feature for the user\n ➛ fix: bug fix for the user\n ➛ docs: changes to the documentation\n ➛ style: formatting, missing semi colons, etc; no production code change\n ➛ refactor: refactoring production code, eg. \
 renaming a variable, func, file etc\n ➛ test: adding missing tests, refactoring tests\n ➛ chore: updates on task/codes\n \n"

select type in feat fix docs style refactor test chore
do
        case $type in 
        feat|fix|docs|style|refactor|test|chore)
                break
                ;;
        *)
                echo "Invalid type" 
                ;;
        esac
done
clear
echo "$type"
printf "What's the scope ?\n\t"
read input
scope=${input:-$scope}

clear

if [[ -z $scope ]]; then
        echo "$type"
        commsg="$type"
else
	echo "$type[$scope]"
        commsg="$type[$scope]"
fi

printf "What exactly happened 🤔 ?\n\t" 
read input
message=${input:-$message}

clear
printf "Your commit message📨:\n$commsg: $message\n"
printf "Create Commit ?:\n y(Yes) n(Abort) r(Start Over) :\n"
read input
decide=${input}

if [ $decide == 'y' ]; then 
	git commit -m "$commsg: $message"
elif [ $decide == 'r' ]; then
	clear
	echo "Restarting ..."
	/home/imitor/Documents/git_repos/ids/git_commit.sh
elif [ $decide == 'n' ]; then
	exit
else
	echo "Invalid choice"
	exit
fi

printf "Wanna Push ?:\n y(Yes) n(No):\n"
read push
push_decide=${push}
if [ $push_decide == 'y' ]; then 
	clear
	git push
else
	clear
	exit
fi
