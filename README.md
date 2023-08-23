# xkcd-display


# Setting up from fresh

# Install Docker
TODO


# Set up on raspberry Pi

Try and get hold of an .env.production file

XKCD_ENVIRONMENT=production
XKCD_REMOTE_WEBSITE
XKCD_SCREEN_SOCKET_URL
XKCD_VIRTUAL_IMAGE_PATH

Get these Environment variables from Cloudflare

CLOUDFLARE_API_KEY - you can create a new API key with permissions just for the tunnel
CLOUDFLARE_ACCOUNT_ID - this is in the URL when you are in the account page
CLOUDFLARE_TUNNEL_ID - in the tunnel web page

Once you have these, run `./setup_cloudflare.sh`
This will copy a token into your clipboard

set a final variable in your production.env file
CLOUDFLARE_TUNNEL_TOKEN=[PASTE_TOKEN_HERE]

# Run docker-compose

in .env, set `XKCD_ENVIRONMENT=production`

run `./start-services.sh` - this will start 

- the website
- the tunnel
- the virtual screen