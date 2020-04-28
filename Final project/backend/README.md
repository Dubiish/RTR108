# Project Back-End

- Written in Python
- Framework used is Flask

## How it works
- POST Request is received with data in body
- Data are then parsed and Netlist file is created for NGSPICE
- System call is called to run ngspice with netlist file
- Output file is producet
- Server reads output file and parse relevant data from it
- Response is sent back in JSON format

## How to start
- Additional packages are needed like: ngspice (for linux), Python packages: "flask", "flask-cors"
- python3 index.py
