#!/bin/bash

cd /root/production/cloud-machine-manager/cloudmachinemanager
cp credentials.py /tmp
cd /root/git/repo
git pull
cp cloudmachinemanager/* /root/production/cloud-machine-manager/cloudmachinemanager/
source /root/production/cloud-machine-manager/cloud-machine-managerenv/bin/activate
pip install -r /root/production/cloud-machine-manager/cloudmachinemanager/requirements.txt
deactivate
cp /tmp/credentials.py /root/production/cloud-machine-manager/cloudmachinemanager
systemctl restart gunicorn_cloudmachinemanager.service
systemctl restart nginx
