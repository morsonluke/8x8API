import requests
from pprint import pprint as pp
import json
import yaml
import json
import sys
import argparse
from tabulate import tabulate

# Create an ArgumentParser object
parser = argparse.ArgumentParser()
parser.add_argument("uri", help="Select the relevant endpoint")
args = parser.parse_args()

host = 'localhost'
platform_url = "vcc-eu3.8x8.com"

f = open('config.yml')
params = yaml.load(f)
f.close()

my_tenant = params['hosts'][host]['tenant']
my_token = params['hosts'][host]['token']

if args.uri == "agents":
    r = requests.get('https://' + platform_url + '/api/rtstats/stats/agents.json', auth=(my_tenant, my_token))
    data = r.json()
    print(tabulate(data['agent'], showindex="always"))
elif args.uri == "queues":
    r = requests.get('https://' + platform_url + '/api/rtstats/stats/queues.json', auth=(my_tenant, my_token))
    data = r.json()
    print(tabulate(data['queue'], showindex="always"))
elif args.uri == "dailyagents":
    agent_id = input("Select agent-id: ")
    r = requests.get('http://' + platform_url + '/api/stats/agents/' + str(agent_id) + '/statistics.json?d=today-1d', auth=(my_tenant, my_token))
    data = r.json()
    statistics = data['statistics']
    if statistics == "":
        print("No data for agent-id: " + str(agent_id))
    else:
        print(tabulate(data['statistics']['statistic'], showindex="always"))
elif args.uri == "dailyqueues":
    queue_id = input("Select queue-id: ")
    r = requests.get('http://' + platform_url + '/api/stats/queues/' + str(queue_id) + '/statistics.json?d=today-1d', auth=(my_tenant, my_token))
    data = r.json()
    statistics = data['statistics']
    if statistics == "":
        print("No data for queue-id: " + str(queue_id))
    else:
        print(tabulate(data['statistics']['statistic'], showindex="always"))
else: 
    print("Select from: agents, queues, dailyagents, dailyqueues")