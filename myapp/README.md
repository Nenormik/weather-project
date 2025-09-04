# Weather APP

## Commands to create in Docker Container

### Build in docker
```
docker build -t weather-app .
```

### Run
```
docker run -d -p 8099:8099 --name weather-app weather-app
```

## Run localy
### Install Depends
```
pip install -r requirements.txt
```
### Run app
```
python app.py
```
