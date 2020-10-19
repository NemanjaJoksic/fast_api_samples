# set base image (host OS)
FROM python:3.6

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY ./requirements.txt ./requirements.txt

# install dependencies
RUN pip install -r ./requirements.txt

# expose port 80
EXPOSE 80

# copy source code
COPY ./src ./src

# startup command
ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
