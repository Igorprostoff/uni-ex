FROM python:3.7.16-slim-bullseye

COPY *.py .
RUN pip install Flask

ENTRYPOINT ["flask", "--app", "app", "run"]
