FROM python:3.10-slim

# System variables
ARG ENV_STATE
ARG POETRY_VERSION

ENV ENV_STATE=${ENV_STATE} \
    # poetry:
    POETRY_VERSION=${POETRY_VERSION}

# Initialize bash shell
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

# System dependencies
RUN pip install --upgrade pip
RUN pip install "poetry==${POETRY_VERSION}"

# Copy only requirements to cache them in docker layer
COPY "poetry.lock" "pyproject.toml" /code/
WORKDIR /code/

# Project initialization
# poetry tries to create a virtualenv, we do not need it in docker. It is already isolated.
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction $(test "${ENV_STATE}" == "prod" && echo "--no-dev")

# Creating folders, and files for a project
COPY . /code/

# Expose container port
#EXPOSE 8000
