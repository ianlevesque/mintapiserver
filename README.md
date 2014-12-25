mintapiserver
=============

This is a minimal, hosted version of an excellent mint.com scraper (https://github.com/mrooney/mintapi) suitable for deployment to a free heroku instance.

I use this to import my account information for local processing in F# without needing to run python on windows.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

After deployment you can import your account information easily using curl or any other http client like this:

    curl -i -u "mintusername:mintpassword" "https://my-personal-deployment-of-this.herokuapp.com/accounts"

HTTPS is strongly recommended.

The mint API library has more functionality than I've exposed here, pull requests welcome.
