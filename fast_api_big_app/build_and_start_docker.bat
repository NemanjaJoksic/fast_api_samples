docker rmi fast_api_auth
docker build -t fast_api_auth .
docker run -it --rm --name fast_api_auth -p 80:80 fast_api_auth
