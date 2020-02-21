#####ansible awx invnetoary

#!/usr/bin/env python
import os
import sys
import argparse
import requests
import ipaddress

try:
    import json
except ImportError:
    import simplejson as json


class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
           self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()


        print (json.dumps(self.inventory))
        #json.dumps(self.inventory)

    # Example inventory for testing.
    def example_inventory(self):
        # del file
        # create get request
        resp = requests.get("https://api", verify=False)
        hosts = []
        groups = {}
        value = {}

        metadatos = {}
        print (resp)
        for i in resp.json():

            print ip

            d1 = {i['NetcoolName']: {'ansible_host': i['IP'], 'partner': i['Fabricant'], 'modelo': i['Modelo']}}
            metadatos.update(d1)

            if i['NetViewServerHostname'] not in groups:
                v = {i['NetViewServerHostname']: {}}
                groups.update(v)

        for key in groups:
            host =[]
            for b in resp.json():
                if b['NetViewServerHostname'] == key:
                    host.append(b['NetcoolName'])
            groups[key] =  {"hosts": host, 'vars': {'ansible_ssh_common_args': '-o ProxyCommand="ssh -W %h:%p -q usuario@proxy' }}

        #    ansible_ssh_common_args:

        with open('/tmp/data.json', 'w+') as file:
            json.dump(metadatos, file)

        return groups

    # Empty inventory for testing.
    def empty_inventory(self):
        a = sys.argv[2]
        with open("/tmp/data.json") as json_file:
             json_data = json.load(json_file)
             return  json_data[a]
        return {'_meta': {'hostvars': {}}}
    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()


# Get the inventory.
ExampleInventory()
