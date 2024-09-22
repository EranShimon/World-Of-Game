FROM python:3.9-slim

WORKDIR /app

COPY Requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r Requirements.txt

COPY . /app

EXPOSE 8777

COPY score_file.txt /score_file.txt

CMD ["python", "MainScores.py"]
