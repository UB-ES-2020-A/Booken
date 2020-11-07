#!/bin/bash

set -e -o pipefail

if [ "${TRAVIS_BRANCH}" == "master" ]; then

  TARGET_APP_NAME="your_app_name"

  echo "Setting maintenance mode 'off' on heroku's app"
  heroku maintenance:off --app "${TARGET_APP_NAME}"

  echo "Application ready again. YAY!"
fi

cd ../..
node_modules/.bin/newman run backend/tests/TEST----Account-Login.postman_collection.json
node_modules/.bin/newman run backend/tests/TEST----Author.postman_collection.json
node_modules/.bin/newman run backend/tests/TEST----Book.postman_collection.json
node_modules/.bin/newman run backend/tests/TEST----Contact.postman_collection.json