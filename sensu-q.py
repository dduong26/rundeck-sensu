"""

This script is used to extract node information from Sensu and
format the data into YAML that Rundeck supports

Author:  David Duong
Email: dduong26@gmail.com
Date:  April 7th 2015

Last Updated: April 21th 2015

"""

# import PyYAML and PySensu modules
import yaml
from pysensu import pysensu

# Using PySensu to connect to Sensu's API
client = pysensu.Pysensu(
    <hostname>,
    port=<port>,
    user=<username>,
    password=<password>,
    ssl=True
)

# Grabbing all the clients (aka nodes) data and throwing it into a variable
hosts = client.get_all_clients()

# Setting hostsobj dictionary
hostsobj = {}

# Iterating through the clients
for host in hosts:

    # Taking the subscriptions objects and putting them into the items variable
    # because the subsciptions are in a list format
    items = host['subscriptions']

    # Variable to add the username option
    usr = '${job.username}'

    # If the host is Windows, write out the Windows YAML entry
    if items[1] == 'Windows':
        osFamily = 'Windows'
        osName = 'Windows'
        osVersion = 'Windows Server 2012 R2'
        osArch = 'x86_64'
        executor = 'overthere-winrm'

        hostsobj[host['name']] = {
            'hostname': host['address'],
            'username': usr,
            'osArch': osArch,
            'osFamily': osFamily,
            'osName': osName,
            'osVersion': osVersion,
            'node-executor': executor,
            'tags': ','.join(host['subscriptions'])
        }
    # If the host is Linux, write out the Linux YAML entry
    else:
        osFamily = 'unix'
        osName = 'Unix'
        osVersion = '2.6.32-504.1.3.el6.x86_64'
        osArch = 'x86_64'

        hostsobj[host['name']] = {
            'hostname': host['address'],
            'username': usr,
            'osArch': osArch,
            'osFamily': osFamily,
            'osName': osName,
            'osVersion': osVersion,
            'ssh-password-option': 'option.sshPassword',
            'sudo-command-enabled': 'true',
            'sudo-password-option': 'option.sshPassword',
            'tags': ','.join(host['subscriptions'])
        }
# Writes the data to a file called resources.yaml for Rundeck to use
with open('resources.yaml', 'w') as outfile:
    outfile.write(yaml.safe_dump(hostsobj, default_flow_style=False))
    # Closes file
    outfile.closed
