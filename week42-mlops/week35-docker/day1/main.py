from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello, World!"
    }


@app.get("/predict")
def predict():
    return {
        "prediction": "positive"
    }


#Concept	Easy meaning
#Dockerfile	Instructions for building the image
#Image	Packaged application
#Container	Running image
#docker build	Build image
#docker run	Start container
#docker ps	Show running containers
#.dockerignore	Files Docker should ignore
#Layer	One step in the image build


#FROM              → foundation
#WORKDIR           → choose the room
#COPY requirements → bring dependency list
#RUN pip install   → install dependencies
#COPY app          → bring your application
#CMD               → start the application