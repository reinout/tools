#!/bin/bash
# Run command with variables loaded from an env file
#
# I have .env-style files that I don't always want to use via `source
# /some/dir/.restic-env-vars` because the env vars stick around in the environment that
# way, I only want to load them for a single command.
#
# I can now use it like this:
#
#     $ run-with-env.sh /some/dir/.restic-env-vars restic ....
#
# Source: https://stackoverflow.com/a/69812128/27401

ENV_FILE="$1"
CMD=${@:2}

set -o allexport
source $ENV_FILE
set +o allexport

$CMD
