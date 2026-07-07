Day 1

Today I started building my homelab dashboard monitoring system as a practical DevOps learning project. I created the Git repo structure and documented the purpose and planned scope of the project in the README.

I then proceeded to create a Bash host inventory script that used Linux commands to pull system information including:

Hostname
OS
Kernel Version
System Uptime
Memory Statistics
Disk Usage

The collector script was initially tested on my main machine running Bazzite and then copied to the ZimaBoard using SCP. Running the same script successfully on a Debian distro proved that the collector was portable between different Linux distributions.

After reviewing the architecture, I identified that generating inventory through text files would not be ideal for a live dashboard. I changed the design to implement an API-based approach where each monitored host would expose system information as JSON.

I then created a Python virtual environment on the ZimaBoard, installed FastAPI and Uvicorn, built and tested my first API endpoint, and successfully queried it remotely from Bazzite using curl.

I also began using the subprocess module in Python to execute Linux commands and capture their output. I created a hostname endpoint to run the Linux hostname command and return the following JSON:

{
  "hostname": "casaos"
}

Key technologies used: Bash, Linux, SSH, SCP, Git, Python, FastAPI, Uvicorn, REST API concepts and JSON.

Learning Outcome for Day 1: I moved from collecting local system information with Bash to exposing live host information through an HTTP API. I also made architectural decisions during development by recognising that SSH-based collection and static text files would not fit the design of a live dashboard.