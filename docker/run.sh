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
  mycommand=${1}
  if ! output=$(${mycommand}); then
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: Command failed!: --$1--"
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: Command output: ${output}"
  else
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ INFO]: Command ran successfully: --$1--"
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S")]:[ERROR]: Command output: ${output}"
  fi

}

: '
This function starts the mongodb container
'
function start_mongodb() {
    docker run --name mongodb -v C:\data\db\:/data/db -p 27017:27017 --network bridge -d mongo
}


# ------------------------------------------------------- main ------------------------------------------------------- #

run_cmd start_mongodb
