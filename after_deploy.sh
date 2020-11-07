#!/bin/bash

set -e -o pipefail
if [ "${TRAVIS_BRANCH}" == "master" ]; then
  TARGET_APP_NAME="booken-dev"
  heroku maintenance:off --app "${TARGET_APP_NAME}"
fi

cd ../..
node_modules/.bin/newman run backend/tests/TEST----Account-Login.postman_collection.json
node_modules/.bin/newman run backend/tests/TEST----Author.postman_collection.json
node_modules/.bin/newman run backend/tests/TEST----Book.postman_collection.json
node_modules/.bin/newman run backend/tests/TEST----Contact.postman_collection.json