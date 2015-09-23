# Rundeck Sensu Node Query Plugin

## Description

This script is used to extract node information from Sensu and format the data into a resource YAML file that Rundeck uses.

## Requirements

- PyYAML
- PySensu

## Deploy

Copy this script where your resource YAML file is located

## Configuration

- Make sure the Sensu API is working

- Edit the script and fill in the information required to utilize the Sensu API.

```
client = pysensu.Pysensu(
    <hostname>,
    port=<port>,
    user=<username>,
    password=<password>,
    ssl=True
)
```

- Run the script

```
$ python sensu-q.py
```
