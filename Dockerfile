FROM python:3-alpine
COPY Requirements.txt Requirements.txt
RUN pip install --no-cache-dir -r Requirements.txt
COPY score_file.txt /scores_file.txt
COPY MainGame.py :
COPY Live.py :
COPY CurrencyRouletteGame.py :
COPY GuessGame.py :
COPY MemoryGame.py :
COPY MainScores.py :
COPY Score.py :
COPY Utils.py :
ENV FLASK_APP=MainScores.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]