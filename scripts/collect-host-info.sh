#!/bin/bash

echo "========================================"
echo " HOMELAB HOST INVENTORY"
echo "========================================"

echo
echo "==> Hostname"
hostname

echo
echo "==> Operating System"
source /etc/os-release
echo "$PRETTY_NAME"

echo
echo "==> Kernel Version"
uname -r

echo
echo "==> System Uptime"
uptime -p

echo 
echo "==> Memory Statistics" 
free -h | grep '^Mem:' | awk '{ 
print "Total: " $2 
print "Used: " $3 
print "Free: " $4 }'

