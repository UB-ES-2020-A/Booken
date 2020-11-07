#!/bin/bash

cd ../../backend/flask-api

set -e -o pipefail

if [ "${TRAVIS_BRANCH}" == "dev" ]; then

  TARGET_APP_NAME="booken-dev"

  cat >> ~/.ssh/config <<EOF
Host heroku.com
   StrictHostKeyChecking no
   CheckHostIP no
   UserKnownHostsFile=/dev/null
EOF

  cat >> ~/.netrc <<EOF
machine api.heroku.com
  login ${HEROKU_API_LOGIN}
  password ${HEROKU_API_KEY}
EOF
  chmod 600 ~/.netrc

  wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

  heroku maintenance:on --app "${TARGET_APP_NAME}"

  heroku pg:backups capture --app "${TARGET_APP_NAME}"
fi