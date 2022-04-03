import yaml
import os
import re
import sys
dict={}
yamlpath=os.path.join("D:/Github/cyber_range/docker-net/output/docker-compose.yml")
file = open(yamlpath, 'r', encoding='utf-8')
filer = file.read()
content=yaml.load(filer,Loader=yaml.SafeLoader)
content2=content['services']
for key in content2.keys():
    if re.search(r'router',key) is not None:
        trans=content2[key]
        dict[key]=trans['container_name']
script= open('script.sh',"w")
for key in dict.keys():
    script.write("docker exec "+dict[key]+"tc qdisc del dev net0 root \n")
    script.write("docker exec "+dict[key]+"tc qdisc add dev eth0 root netem delay 100ms 20ms distribution normal \n")
script.close()
print(dict)