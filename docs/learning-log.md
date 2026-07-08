#==================

Day 1

#==================

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

#===============

Day 2

#===============

Created a systemd service for the FastAPI app so the ZimaBoard metrics API runs continuously without needing a terminal session.

ZimaBoard boot/service layer
    ↓
systemd
    ↓
homelab-api.service
    ↓
FastAPI/Uvicorn
    ↓
GET /system returns live JSON

Today I continued development of the homelab dashboard by expanding the API backend and creating the working front end dashboard.

I refactored the API so system collection tasks were separated into python functions. I used the functions to collect hostname, memory statistics, disk use, uptime, os and kernel information. The functions were then combined into a sinlge endpoint which returns JSON containing the system information from the Zimaboard its hosted on.

After this I configured the API application to run as a systemd service on the Zimaboard to allow the API to run continuously without manual intervention and to make sure the service can be managed using standard linux commands.

The front end was created using HTML/CSS/Javascript. It uses the fetch() function in javascript to query the API endpoint and display the information. During this part of development I encountered a CORS issue where the browser blocked requests to the API. THis was diagnosed using developer console via the browser and CORS middleware was configured in FastAPI to allow the requests.

Automatic polling was added via setInterval() and try catch to add error handling so the front end can detect when the API is not available. The host status will dynamically change between LIVE and DOWN, while stale metrics are then cleared when the API is unreachable.

I then expanded on the API to collect container information from docker to return the container name and status. Python processes this and returns as a set of JSON objects.

The front end was updated to dynamically create application rows from the API using javascript forEach(). Container states are visually represented as running, health or stopped with blue, green and red status indicators. Testing was performed by stopping a container and starting to confirm change of status and indicator during the 30 second polling cycle.

Key technologies used: Python, FastAPI, Uvicorn, systemd, Docker, REST APIs, JSON, HTML, CSS, JavaScript, CORS, Git and Linux.

Learning Outcome for Day 2: I developed the project from a basic API into an end-to-end monitoring application. I learned how backend API data can be consumed by a JavaScript frontend, how browser CORS restrictions affect cross-origin API requests, how to implement automatic polling and error handling, and how Docker container state can be collected and dynamically represented in a monitoring dashboard. I also debugged several issues involving JavaScript scope, HTML/CSS class matching and application state handling.