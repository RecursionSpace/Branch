#!/bin/bash

# Perform updates of the branch program.

branch_dir=$(jq '.branch.directory' stem.json)
config_file=$(jq '.branch.config_file' stem.json)

current_version=$(jq '.current_version' $branch_dir$config_file)

echo "Current version: $current_version"
