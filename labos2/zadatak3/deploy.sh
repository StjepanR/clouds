sudo apt-get update
sudo apt-get -y install python3 python3-dev
sudo apt install python3-pip
sudo apt-get -y install nginx
sudo apt-get -y install git
git clone https://StjepanR@github.com/StjepanR/clouds-assignment2-task2.git
cd clouds-assignment2-task2
sudo apt install python3-flask
export FLASK_APP=microservice.py
flask run -h 0.0.0.0