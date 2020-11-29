#!/usr/bin/env sh

SPEC_VERSION=`grep "Version:" cryfs.spec | awk '{print $2}'`
REMOTE_VERSION=`git ls-remote --tags https://github.com/cryfs/cryfs.git | awk '{print $2}' | sort --version-sort | tail -n 1 | cut -d '/' -f 3`

if [ "${SPEC_VERSION}" = "${REMOTE_VERSION}" ]
then
    echo "No new version : skipping update"
    exit 0
fi

echo "New version {${REMOTE_VERSION}} : updating"
sed -ri "s/(Version:\s+) [0-9]+.[0-9]+.[0-9]+/\1 ${REMOTE_VERSION}/" cryfs.spec
