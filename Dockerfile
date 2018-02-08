FROM python:3-alpine

# -- Create WorkDir & Install Pipenv:
RUN set -ex \
    && mkdir /app \
    && python -m pip install pipenv --upgrade

WORKDIR /app

# -- Adding Pipfiles
COPY Pipfile* /app/

# -- Install Dependencies
RUN set -ex && python -m pipenv install --deploy --system

# -- Copy in the Application Code
COPY . .

EXPOSE 5000

CMD [ "python", "./app.py" ]
