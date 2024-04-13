FROM python:3.11.6-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

RUN pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python -m src.manage runserver 0.0.0.0:8001"]