python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=app.py
flask run

docker build -t my-hello-world .
docker run -p 5000:5000 my-hello-world

docker run my-hello-world python -m pytest
