#!/bin/bash

# Perform updates of the branch program.

branch_dir=$(jq --raw-output '.branch.directory' /opt/Stem/stem.json)
config_file=$(jq --raw-output '.branch.config_file' /opt/Stem/stem.json)

current_version=$(jq --raw-output '.current_version' "${branch_dir}${config_file}")

echo "Current version: $current_version"
