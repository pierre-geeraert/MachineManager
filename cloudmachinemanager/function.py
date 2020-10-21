from django.http import HttpResponse, Http404
from django.shortcuts import render
from proxmoxer import ProxmoxAPI
import credentials
#from . import views

def proxmox_connection(proxmox_target,username,password):
    proxmox = ProxmoxAPI(proxmox_target, user=username,
                         password=password, verify_ssl=False)
    return proxmox


def type_machine(id_machine,id_proxmox):
    tab_tryton = [["nfs","lxc"],"b"]
    print(tab_tryton[0][0])
    print(tab_tryton.index("b"))
    return 0

def action(request,id_machine,action,type_machine):
    """
    :id__proxmox: proxmox target
    :param id_machine: id of desired machine ( int)
    :param action: start, stop or shutdown
    :return:
    """

    node = credentials.proxmox.server1.node
    #type_machine = 'lxc'

    proxmox = ProxmoxAPI(credentials.proxmox.server1.url_proxmox, user=credentials.proxmox.server1.user,
                         password=credentials.proxmox.server1.password, verify_ssl=False)

    if type_machine == 'lxc':
        proxmox.nodes(node).lxc(id_machine).status(action).post()
    elif type_machine == 'qemu':
        proxmox.nodes(node).qemu(id_machine).status(action).post()
    else:
        print("incorrect value")

    if action == "stop":
        sentence = 'l`arret brutal'
    elif action == "start":
        sentence = "le démarrage"
    elif action == "shutdown":
        sentence = "l`arret doux"

    """
    return HttpResponse(
        "Vous avez demandées {0} de la machine {1} !".format(sentence,id_machine)
        #   "Vous avez demandé l'hyperviseur "
    )
    """

def check_state_mix(id_machine,wanted_state,proxmox,instance_type):
    effective_status = ""
    if instance_type == "lxc":
        for node in proxmox.nodes.get():
            for vm in proxmox.nodes(node['node']).lxc.get():
                if vm['vmid'] == str(id_machine):
                    effective_status = (vm['status'])
                #print(proxmox.nodes(node['node']).lxc.get()[0])
    elif instance_type == "qemu":
        for node in proxmox.nodes.get():
            for vm in proxmox.nodes(node['node']).qemu.get():
                if vm['vmid'] == str(id_machine):
                    effective_status = (vm['status'])
                #print(proxmox.nodes(node['node']).lxc.get()[0])

    else:
        print("bad instance type")
    return effective_status

def test(request,id_article):
    return HttpResponse(
        "Vous avez demandée l'hyperviseur n° {0} !".format(id_article)
     #   "Vous avez demandé l'hyperviseur "
    )
