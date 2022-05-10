# Branch Configuration

There are two sources of configuration files for branch, the branch.json file and the branch.conf file.

## stem.json

The branch.json file is found in the root of the Branch directory and is used to establish which programs are being branched into.

``` json
{
    "branch": {
        "name": "",
        "directory": "",
        "config_file": "{branch_name}.json",
        "version_url_endpoint": "",
    },
}
```

| Key                  | Value                                                                            |
|----------------------|----------------------------------------------------------------------------------|
| name                 | The name of the branch.                                                          |
| directory            | The directory that the branch is located in.                                     |
| config_file          | The name of the branches config file within the branch directory.                |
| version_url_endpoint | The url endpoint to get the latest version from. Needs to be full URL with HTTPS |
| zip_url              | The url of the program to be branched                                            |

## branch.conf

The branch.conf file is found in the root of the directory imported by Branch.
