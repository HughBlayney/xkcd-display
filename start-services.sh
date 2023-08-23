source .env
if [ "$XKCD_ENVIRONMENT" == "production" ]; then
    source .env.production
    export $(cut -d= -f1 .env.production)
    docker-compose up xkcd_remote screen_server tunnel
else
    docker-compose up xkcd_remote screen_server
fi