from django.http import HttpResponse, Http404
from django.shortcuts import render
from proxmoxer import ProxmoxAPI


def proxmox_connection(proxmox_target,username,password):
    proxmox = ProxmoxAPI(proxmox_target, user=username,
                         password=password, verify_ssl=False)
    return proxmox


def type_machine(id_machine,id_proxmox):
    tab_tryton = [["nfs","lxc"],"b"]
    print(tab_tryton[0][0])
    print(tab_tryton.index("b"))
    return 0

def action(request,id_proxmox,id_machine,action):
    """
    :id__proxmox: proxmox target
    :param id_machine: id of desired machine ( int)
    :param action: start, stop or shutdown
    :return:
    """

    id_proxmox == 'id'
    url_proxmox = 'domain.com'
    password = 'password'
    node = 'pve'

    type_machine = 'lxc'

    proxmox = ProxmoxAPI(url_proxmox, user='user@pve',
                         password=password, verify_ssl=False)

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

    return HttpResponse(
        "Vous avez demandées {0} de la machine {1} sur {2} !".format(sentence,id_machine,id_proxmox)
        #   "Vous avez demandé l'hyperviseur "
    )

def check_state(id_machine,wanted_state,proxmox):
    effective_status = ""

    for node in proxmox.nodes.get():
        for vm in proxmox.nodes(node['node']).lxc.get():
            if vm['vmid'] == str(id_machine):
                effective_status = (vm['status'])
            #print(proxmox.nodes(node['node']).lxc.get()[0])
    return effective_status

def test(request,id_article):
    return HttpResponse(
        "Vous avez demandée l'hyperviseur n° {0} !".format(id_article)
     #   "Vous avez demandé l'hyperviseur "
    )

#print(check_state(112,"down",proxmox_connection("geeraert.eu","cloudmanager@pve","D7wUhdzZm6D6FLeZHLVprYgt3bxok")))
