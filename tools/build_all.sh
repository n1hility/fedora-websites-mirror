#!/bin/bash

sites=()

# Sites to build
sites+=(alt.fedoraproject.org)
sites+=(arm.fedoraproject.org)
sites+=(fedoracommunity.org)
sites+=(flocktofedora.org)
sites+=(labs.fedoraproject.org)
sites+=(spins.fedoraproject.org)
sites+=(start.fedoraproject.org)

[ -d out ] && rm -Rf out
mkdir  out
for site in ${sites[@]}; do
  echo
  echo "************ Building $site ***************"
  pushd $site
  make BASEPATH=/$site en 2>&1 | tee build.log
  if [ $? -ne 0 ]; then
    echo "!! Build Failed for $site !!"
    rm -Rf out
    mkdir out
  fi
  mv build.log out/
  sed "s|@SITE@|$site|" ../.ci/htaccess.in > out/.htaccess
  rm -Rf ../out/$site
  mv out ../out/$site
  popd
done
