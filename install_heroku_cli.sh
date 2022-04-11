wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
~/bin/heroku-cli/bin/heroku -v
cat >~/.netrc <<EOF
machine api.heroku.com
  login $HEROKU_EMAIL
  password $HEROKU_TOKEN
machine git.heroku.com
  login $HEROKU_EMAIL
  password $HEROKU_TOKEN
EOF
chmod 600 ~/.netrc # Heroku cli complains about permissions without this