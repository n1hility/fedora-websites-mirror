#!/bin/bash

sites=()
# BUILD_ENV = stg or prod 

# Sites to build
sites+=(alt.fedoraproject.org)
sites+=(arm.fedoraproject.org)
sites+=(fedoracommunity.org)
sites+=(flocktofedora.org)
sites+=(labs.fedoraproject.org)
sites+=(spins.fedoraproject.org)
sites+=(start.fedoraproject.org)

[ -z "$OUTPUT" ] && OUTPUT="$(pwd)/out"
[ ! -d $OUTPUT ] && mkdir $OUTPUT
for site in ${sites[@]}; do
  (
  set -e
  set -o pipefail
  echo
  echo "**** Building $BUILD_ENV $site to ${OUTPUT}/${site} ****"
  pushd $site
  if [ -z "$BUILD_ENV" ]; then
    # local build or in CI
    make BASEPATH=/$site en 2>&1 | tee ${OUTPUT}/${site}.log
    sed "s|@SITE@|$site|" ../.ci/htaccess.in > out/.htaccess
  else
    # stg or prod build
    make pullpos
    make
    [ -d ${OUTPUT}/${site}.new ] && rm -rf ${OUTPUT}/${site}.new
    [ -d ${OUTPUT}/${site}.old ] && rm -rf ${OUTPUT}/${site}.old
  fi

  date +%s > out/build.timestamp
  git rev-parse HEAD > out/build.commit
  mv out ${OUTPUT}/${site}.new

  # Final quick move
  [ -d ${OUTPUT}/$site ] && mv ${OUTPUT}/$site ${OUTPUT}/${site}.old
  mv ${OUTPUT}/${site}.new ${OUTPUT}/$site

  # cleaning
  rm -Rf ${OUTPUT}/${site}.old
  rm -f  ${OUTPUT}/${site}.log

  popd
  )
done
echo "Completed"

