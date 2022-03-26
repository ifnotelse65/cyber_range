#!/usr/bin/bash
cd /home/seed/Desktop/cyber_range/output
docker-compose down
/home/seed/Desktop/cyber_range
python3 main.py
cd output/
docker-compose build
docker-compose up
