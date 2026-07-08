from fastapi import FastAPI
import subprocess

app = FastAPI()

def get_health():
    return {"status": "ok"}

def get_hostname():
    result = subprocess.run(["hostname"], capture_output=True, text=True)
    return result.stdout.strip() 


def get_memory():
    mem_info = subprocess.run(
        ["free", "-h"],
        capture_output=True,
        text=True
    )

    lines = mem_info.stdout.splitlines()
    memory = lines[1].split()

    return {
        "total": memory[1],
        "used": memory[2],
        "free": memory[3] 
    }

def get_disk():
    disk_info = subprocess.run(
	 ["df", "-h", "/"],
	 capture_output=True,
	 text=True,
    )

    lines = disk_info.stdout.splitlines()
    disk = lines[1].split()

    return {
	"filesystem": disk[0], 
	"size": disk[1],
	"used": disk[2],
	"available": disk[3],
	"use_percent": disk[4],
	"mount": disk[5],
	
    }

def get_uptime():
    uptime_info = subprocess.run(
	   ["uptime", "-p"],
	   capture_output=True,
	   text=True,
    )
    return uptime_info.stdout.strip()

def get_os():
    os_info = subprocess.run(
       ["bash", "-c", 'source /etc/os-release && echo "$PRETTY_NAME"'],
       capture_output=True,
       text=True,
    )
    return os_info.stdout.strip()


def get_kernel():
    kernel_info = subprocess.run(
       ["uname", "-r"],
       capture_output=True,
       text=True,
    )  
    return kernel_info.stdout.strip()

@app.get("/system")
def system():
	return {
	    "health": get_health(),
	    "hostname": get_hostname(),
	    "memory": get_memory(),
	    "disk": get_disk(),
	    "uptime": get_uptime(),
	    "os": get_os(),
            "kernel": get_kernel(),
	}


	
