FROM python:3.10

RUN apt-get update && \
    apt-get upgrade -y

WORKDIR /app

COPY ./Pipfile ./Pipfile.lock /app/
COPY ./src /app/src

RUN python3 -m pip --no-cache-dir install --upgrade pip && \
    python3 -m pip install pipenv==2022.9.8 && \
    pipenv requirements > requirements.txt && \
    python3 -m pip install -r requirements.txt && \
    rm /app/Pipfile && rm /app/Pipfile.lock && rm /app/requirements.txt && \
    python3 -m pip uninstall pipenv && \
    # Clean Python cache
    find /usr/local/ -name '*.pyc' -print0 | xargs -0 rm -rf || true && \
    find /usr/local/ -type d -name '__pycache__' -print0 | xargs -0 rm -rf || true


EXPOSE 8000



CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]