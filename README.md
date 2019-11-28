# MachineManager
Manager to stop a VM from my proxmox with http address : for wiki start.wiki.DOMAIN.com


To reproduce this architecture, you need to perform these actions:
#### Create a django project
  
    django-admin.py startproject cloudmachinemanager cloud-machine-manager

#### Create a virtualenv

    python3.7 -m venv cloud-machine-managerenv

#### Connect to this virtualenv

    source cloud-machine-managerenv/bin/activate

#### Install every packages

    pip install -r requirements.txt 

#### Exit this virtualenv

    deactivate
