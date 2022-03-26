cd ./output
docker-compose down
cd D:\Github\cyber_range\docker-net
python main.py
cd ./output
docker-compose build
docker-compose up