FROM python:3.10.10-bullseye

WORKDIR /app


COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install spacy
RUN python -m spacy download en_core_web_md

COPY . .

CMD python watch_next.py