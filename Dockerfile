FROM python:3.10

RUN apt-get update && \
    apt-get upgrade -y

WORKDIR /app

COPY ./Pipfile ./Pipfile.lock /app/
COPY ./src /app/src

RUN python3 -m pip --no-cache-dir install --upgrade pip
RUN python3 -m pip install pipenv==2022.9.8
RUN pipenv requirements > requirements.txt
RUN python3 -m pip install -r requirements.txt
RUN rm /app/Pipfile && rm /app/Pipfile.lock && rm /app/requirements.txt
    # Clean Python cache
RUN find /usr/local/ -name '*.pyc' -print0 | xargs -0 rm -rf || true 
RUN find /usr/local/ -type d -name '__pycache__' -print0 | xargs -0 rm -rf || true


EXPOSE 8000



CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]