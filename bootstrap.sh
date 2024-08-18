#!/bin/bash

python -m venv car-venv
. car-venv/bin/activate
pip install --upgrade pip
pip install scapy python-can
