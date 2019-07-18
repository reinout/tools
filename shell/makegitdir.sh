#!/bin/bash
set -e
cd ~/repos
mkdir "$1"
cd "$1"
git init --bare
