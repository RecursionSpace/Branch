#!/bin/bash

# Perform updates of the branch program.

# -------------------------------- Verify Root ------------------------------- #
if [ "$EUID" -ne 0 ]
  then echo "Please run as root with sudo."
  exit 1
fi

# ---------------------------- Read Stem Variables --------------------------- #
if [ -f /opt/Stem/stem.json ]; then
    branch_dir=$(jq --raw-output '.branch.directory' /opt/Stem/stem.json)
    config_file=$(jq --raw-output '.branch.config_file' /opt/Stem/stem.json)
    version_url_endpoint=$(jq --raw-output '.branch.version_url_endpoint' /opt/Stem/stem.json)
else
    echo "Required file stem.json file not found."
    exit 1
fi

# --------------------------- Read Branch Variables -------------------------- #
if [ -f "${branch_dir}${config_file}" ]; then
    current_version=$(jq --raw-output '.current_version' "${branch_dir}${config_file}")
    latest_version=$(curl --silent "${version_url_endpoint}")
    update_url=$(jq --raw-output '.update_url' "${branch_dir}${config_file}")
    access_token=$(jq --raw-output '.access_token' "${branch_dir}${config_file}")
else
    echo "Required file ${branch_dir}${config_file} not found."
    exit 1
fi

# ------------------------------- Update Branch ------------------------------ #
if [ "$current_version" != "$latest_version" ]; then

    # Create staging directory.
    if [ -d "/opt/Stem/branch_staging" ]; then
        rm -r /opt/Stem/branch_staging
    fi
    mkdir -p /opt/Stem/branch_staging;

    # Convert latest version separators to underscores.
    latest_version_underscored=$(echo "${latest_version}" | tr '.' '_')

    # Download the latest version.
    curl -H "Authorization: token  ${access_token}" \
        --output "/opt/Stem/branch_staging/${latest_version_underscored}.zip" \
        --silent --location "${update_url}"

    unzip /opt/Stem/branch_staging/"$latest_version_underscored".zip -d /opt/Stem/branch_staging    # Unzip the latest version.

    rm /opt/Stem/branch_staging/"$latest_version_underscored".zip                                   # Remove the zip file.

    # Rename the extracted directory to the latest version.
    mv /opt/Stem/branch_staging/"$(ls -N /opt/Stem/branch_staging)" /opt/Stem/branch_staging/"${latest_version_underscored}"

    cd /opt/Stem/branch_staging/"$latest_version_underscored" || exit

    # Run the installer.
    if [ "$(./install.sh)" -ne 0 ]; then
        echo "Installer failed."
    else
        echo "Branch updated to version ${latest_version}."
        tmp=$(mktemp)
        jq '.current_version = "$latest_version"' "${branch_dir}${config_file}" > "$tmp" && mv "$tmp" "${branch_dir}${config_file}"
    fi

else
    echo "Branch is up to date."
    exit 0
fi
