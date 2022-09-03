#!/bin/bash

# ----------------------------------------------- function definitions ----------------------------------------------- #

: '
This function runs a command with a status check. It takes only one argument.
'
function run_cmd()  {
  # Gather arguments info
  arguments_number=${#}
  arguments_array=(" $@ ")

  # Check before running command
  if [ ${arguments_number} -gt 1 ]; then
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: To many arguments given to the run_cmd function! It accepts only one."
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: Number of arguments given: ${arguments_number}"

    # Show input args to the user
    for arg_nr in ${!arguments_array[*]}; do
      echo "ARG $((arg_nr+1)): ${arguments_array[arg_nr]}"

    done
    exit 1
  fi

  # Run given command and heck status of ran command
  my_command=${1}
  if ! output=$(${my_command}); then
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: Command failed!: --$1--"
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: Command output: ${output}"
  else
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ INFO]: Command ran successfully: --$1--"
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: Command output: ${output}"
  fi

}

: '
This function builds application image
'
function build_fastapi_app() {
    docker build -t fastapi_learn:v0.4 . -f './docker/Dockerfile' --no-cache --build-arg ENV_STATE=dev --build-arg POETRY_VERSION=1.2.0
}

: '
This function starts the mongodb container
'
function start_mongodb() {
#    docker run --name mongodb -v ~/Projects/Personal/Learn_fastapi/mongodb/:/data/db -p 27017:27017 --network host -d --rm mongo
    docker run --name mongodb -v ~/Projects/Personal/Learn_fastapi/mongodb/:/data/db -p 27017:27017 -d --rm mongo
}

: '
This function starts the fastAPI container
'
function start_fastapi_app() {
#    docker run --name fastapi_learn -p 8000:8000 --network host -d --rm -it fastapi_learn:v0.4 /bin/bash -c 'poetry run uvicorn app.main:app --reload'
    docker run --name fastapi_learn -p 8000:8000 -d --rm -it fastapi_learn:v0.4 /bin/bash -c 'poetry run uvicorn app.main:app --reload'
}

: '
This function to kill all containers
'
function kill_docker_containers() {
    docker kill $(docker ps -q)
}

# ------------------------------------------------------- main ------------------------------------------------------- #

run_cmd build_fastapi_app
run_cmd start_mongodb
run_cmd start_fastapi_app
