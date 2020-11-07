#!/bin/bash

set -e -o pipefail
if [ "${TRAVIS_BRANCH}" == "master" ]; then
  TARGET_APP_NAME="booken-dev"
  heroku maintenance:off --app "${TARGET_APP_NAME}"
fi
