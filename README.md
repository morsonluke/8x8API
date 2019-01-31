## What you can find here

* A extremely basic console applicaton to get basic data for a few endpoints from the 8x8 API. Used for data validation 
* Update the `tenant`, `token` and `platform url`
* Run the file in the console using `8x8api.py {argument}`

| Argument    | Description | URI |
| ----------- | ----------- | --- |
| `agents`      | Shows [real time statistics](https://support.8x8.com/us/Cloud_Contact_Center/Virtual_Contact_Center/Developers/virtual_contact_center_real_time_statistics_reporting_api#Agent) for the agents |`https://{platform url}/api/rtstats/stats/agents.json` |
| `queues`      | Shows [real time statistics](https://support.8x8.com/us/Cloud_Contact_Center/Virtual_Contact_Center/Developers/virtual_contact_center_real_time_statistics_reporting_api#Queue) for the queue | `https://{platform url}/api/rtstats/stats/queues.json` |
| `dailyagents` | Shows statistics for the previous day for the specified agent. Requires the `agent-id` | `http://{platform url}/api/stats/agents/{agent-id}/statistics?d=today-1d` |
| `dailyqueues` | Shows statistics for the previous day for the specified queue. Requires the `queue-id` | `http://{platform url}/api/stats/queues/{queue-id}/statistics?d=today-1d` |

### Requirements
* Python 3.6
* [tabulate](https://bitbucket.org/astanin/python-tabulate)

### Improvements
The table format is not readble unless you have a knowledge of the data. However it is sufficient to check the data against a different source.
