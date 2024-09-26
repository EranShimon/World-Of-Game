FROM python:3-alpine
COPY Requirements.txt Requirements.txt
RUN pip install --no-cache-dir -r Requirements.txt
COPY score_file.txt /scores_file.txt
ENV FLASK_APP=MainScores.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]