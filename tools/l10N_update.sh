#!/bin/bash
# this script pull all translations to tranlation repository,
#      make an new POT and push it if asked,
#      and then fill the LINGUAS file

# This represent the relative path to the website.
site=( ../boot.fedoraproject.org
       ../fedoracommunity.org
       ../fedorahosted.org
       ../fedoraproject.org
       ../fudcon.fedoraproject.org
       ../spins.fedoraproject.org
       ../start.fedoraproject.org )

root=$PWD

usage()
{
cat << EOF
usage: $0 [OPTIONS] [-w WEBSITE_PATH]

This script update all L10n things. Will never git push.
 * pull translations from translation repository against WEBSITE_PATH in current branch
 * make new POT in WEBSITE_PATH
 * update the LINGUAS file in WEBSITE_PATH

OPTIONS:
   -h      Show this message
   -p      update POT on tranlation repository

WEBSITE:
    The website targeted (like "fedoraproject.org")
    Without WEBSITE specifyed, will parse the whole website array.

EXAMPLES:
         $ $0                                  (1)
         $ $0 -w ../spins.fedoraproject.org    (2)
         $ $0 -p                               (3)

   1. Update all but let you git add and push to tranlation repository.
   2. Update POs POT and LINGUAS of spins.fedoraproject.org website. Let you test localy.
   3. Update all and commit changes in 3 different commits. That's what you were looking for.

EOF
}

while getopts ":hacpw:" OPTION
do
  case $OPTION in
    h)
      usage
      exit 1
      ;;
    p)
      POT_PUSH=1
      ;;
    w)
      WEBSITE=$OPTARG
      ;;
    ?)
      usage
      exit
      ;;
  esac
done


if [ -z $WEBSITE ]
then
  echo "Going to update the following websites:"
  echo "${site[*]}"
else
  echo "Going to update $WEBSITE"
  if [ ! -d $WEBSITE ]
  then
     echo "$WEBSITE not found!"
     exit 111
  fi
  site=( $WEBSITE )
fi


### POs

echo "- Updating POs"
for i in "${site[@]}"
do
   cd $i
   make pullpos
   cd $root
done

### POT

for i in "${site[@]}"
do
   echo "- Updating $i POT"
   cd $i
   make pot
   insertion_number=`git diff --numstat po/*.pot 2>&1 | awk '{print $1}'` # record the number of insertion,
									 #if no new string found at least the build time could change (i.e. check if > 1)
   let "$((++insertion_number))"     # cause in case the file is exactly the same, prevent no git diff output
   if [ $insertion_number -gt 2 ]
   then								 # POT should be uploaded
     NEED_COMMIT=1					 # don't commit if any POT modified!
     if [ ! -z $ADD ]
     then
       git add po/*.pot
       if [ ! -z $POT_PUSH ] && [ ! -z $COMMIT ]
       then
         make pushpot
       fi
     fi
     echo "POT updated"
   fi

   cd $root
done

### LINGUAS
# This is now handled in pullpos


exit 0
