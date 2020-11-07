#!/bin/bash

cd ../../backend/flask-api

set -e -o pipefail

if [ "${TRAVIS_BRANCH}" == "master" ]; then

  TARGET_APP_NAME="your_app_name"

  echo "Setting up '~/.ssh/config' to work with heroku."
  cat >> ~/.ssh/config <<EOF
Host heroku.com
   StrictHostKeyChecking no
   CheckHostIP no
   UserKnownHostsFile=/dev/null
EOF

  # DOC: https://devcenter.heroku.com/articles/authentication#usage-examples
  cat >> ~/.netrc <<EOF
machine api.heroku.com
  login ${HEROKU_API_LOGIN}
  password ${HEROKU_API_KEY}
EOF
  chmod 600 ~/.netrc

  echo "Installing heroku toolbelt"
  wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

  echo "Setting maintenance mode 'on' on heroku's app"
  heroku maintenance:on --app "${TARGET_APP_NAME}"

  echo "Caturing DB backup from heroku's app"
  # DOC: https://devcenter.heroku.com/articles/heroku-postgres-backups#creating-a-backup
  heroku pg:backups capture --app "${TARGET_APP_NAME}"
fi