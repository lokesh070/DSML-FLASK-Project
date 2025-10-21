FROM python:3.13.9-slim-trixie

#creating working directory
WORKDIR C:/Users/lokes/OneDrive/Desktop/GIT_Projects/DSML-FLASK-Project/DOCKER

#adding requirements txt file to the working directory
COPY requirements.txt ./

# auto update pip and python versions
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

#adding command not to hold any cache from the requiremnts document
# installing recursively for the libraries in requirements.txt

#RUN pip install --no--cache-dir -r requirements.txt
 #copy reaminng files from current directory to Working directory
COPY . .

#command to run the docker
CMD ["python", "-m", "flask", "--app", "predictions", "run", "--host=0.0.0.0", "--port=5000"]

# Building Image: docker built -t my_app_name .  [ t = tag, . = current directory]
# Run The Image : docker run -p hostport:container_port your_image_name