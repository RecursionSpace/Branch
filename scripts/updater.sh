#!/bin/bash

# Perform updates of the branch program.

# -------------------------------- Verify Root ------------------------------- #
if [ "$EUID" -ne 0 ]
  then echo "Please run as root with sudo."
  exit
fi

# ---------------------------- Read Stem Variables --------------------------- #
branch_dir=$(jq --raw-output '.branch.directory' /opt/Stem/stem.json)
config_file=$(jq --raw-output '.branch.config_file' /opt/Stem/stem.json)
version_url_endpoint=$(jq --raw-output '.branch.version_url_endpoint' /opt/Stem/stem.json)

# --------------------------- Read Branch Variables -------------------------- #
current_version=$(jq --raw-output '.current_version' "${branch_dir}${config_file}")
latest_version=$(curl --silent "${version_url_endpoint}")
update_url=$(jq --raw-output '.update_url' "${branch_dir}${config_file}")
access_token=$(jq --raw-output '.access_token' "${branch_dir}${config_file}")

echo "Current version: $current_version"
echo "Latest version: $latest_version"

if [ "$current_version" != "$latest_version" ]; then
    echo "Update available."

    if [ -d "/opt/Stem/branch_staging" ]; then
        rm -r /opt/Stem/branch_staging
    fi

    mkdir -p /opt/Stem/branch_staging;

    # Convert latest version separators to underscores.
    latest_version=$(echo "${latest_version}" | tr '.' '_')

    echo "Update URL: ${update_url}"

    # Download the latest version.
    curl -H "Authorization: token  ${access_token}" \
        --output "/opt/Stem/branch_staging/${latest_version}.zip" \
        --silent --location "${update_url}"

    # Unzip the latest version.
    unzip /opt/Stem/branch_staging/"$latest_version".zip -d /opt/Stem/branch_staging

    rm /opt/Stem/branch_staging/"$latest_version".zip

    # Rename the extracted directory to the latest version.
    mv /opt/Stem/branch_staging/"$(ls -N /opt/Stem/branch_staging)" /opt/Stem/branch_staging/"${latest_version}"

    cd /opt/Stem/branch_staging/"$latest_version" || exit

    # Run the installer.
    ./install.sh

else
    echo "Branch is up to date."
    exit 0
fi
