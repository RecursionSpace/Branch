#!/bin/bash

# Perform updates of the branch program.

branch_dir=$(jq --raw-output '.branch.directory' /opt/Stem/stem.json)
config_file=$(jq --raw-output '.branch.config_file' /opt/Stem/stem.json)

current_version=$(jq --raw-output '.current_version' "${branch_dir}${config_file}")

version_url_endpoint=$(jq --raw-output '.branch.version_url_endpoint' /opt/Stem/stem.json)

latest_version=$(curl --silent "${version_url_endpoint}")

echo "Current version: $current_version"
echo "Latest version: $latest_version"

if [ "$current_version" != "$latest_version" ]; then
    echo "Update available."
else
    echo "Branch is up to date."
    exit 0
fi
