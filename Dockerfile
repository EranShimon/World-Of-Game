FROM python:3.9-slim

WORKDIR /app

COPY Requirements.txt /app
COPY . /app


RUN pip install --upgrade pip
RUN pip install -r Requirements.txt
#--no-cache-dir
EXPOSE 8777

COPY score_file.txt /score_file.txt

CMD ["python", "MainScores.py"]
