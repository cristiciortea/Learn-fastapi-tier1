FROM python:3.10-slim

# System variables
ARG ENV_STATE
ARG POETRY_VERSION

# Workaround
COPY .env /code/
WORKDIR /code/
RUN export .env

#ENV ENV_STATE=${ENV_STATE} \
#    # poetry:
#    POETRY_VERSION=${POETRY_VERSION}

ENV ENV_STATE=dev \
    # poetry:
    POETRY_VERSION=1.2.0

# System dependencies
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY "poetry.lock" "pyproject.toml" /code/

# Project initialization
# poetry tries to create a virtualenv,  we do not need it in docker. It is already isolated
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction $(test "$ENV_STATE" == prod && echo "--no-dev")

# Creating folders, and files for a project
COPY . /code/

# Expose container port
EXPOSE 8000
