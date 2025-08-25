from kubernetes import client, config
import db_interaction
import credentials
def k8s_connection(kube_config):
    config.load_kube_config(config_file=kube_config)

def modify_replica_count(namespace_name,deploy_name,desired_replicas):
    api = client.AppsV1Api()
    deployment = api.read_namespaced_deployment(name=deploy_name, namespace=namespace_name)
    deployment.spec.replicas = desired_replicas
    resp = api.patch_namespaced_deployment(
        name=deploy_name, namespace=namespace_name, body=deployment);
    return resp

def k8s_list_deploy():
    v1 = client.AppsV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_deployment_for_all_namespaces(watch=False)
    
    deploy_list = []
    
    for i in ret.items:
        print("%s\t%s\t%s" % (i.metadata.namespace, i.metadata.name,i.spec.replicas ))
        deploy_list.append([i.metadata.namespace, i.metadata.name,i.spec.replicas])
    return deploy_list
    
def get_expected_replica_for_deploy(namespace_name,deploy_name):
    #DB query to get the expected replica count
    return "expected replica count"
def compare_expected_replicas_count(array_list_current_deploy):
    for deploy in array_list_current_deploy:
        Namespace = deploy[0]
        Name = deploy[1]
        replicas = deploy[2]
        expected_replica_count = get_expected_replica_for_deploy(Namespace,Name) 
        
        if replicas != expected_replica_count:
            modify_replica_count(Namespace,Name,expected_replica_count)
        
def main():
    """
    k8s_connection("/home/pi-ux-ce/.kube/config")
    
    array_list_deploy = k8s_list_deploy()



    deployments = {}
    
    for deploy in array_list_deploy:  # Assuming this is your list of deployments
        namespace = deploy[0]
        name = deploy[1]
        replicas = deploy[2]
    
        # Ensure the namespace exists in the dictionary
        if namespace not in deployments:
            deployments[namespace] = {}
    
        # Add the deployment info
        deployments[namespace][name] = {
            "replica_count": replicas,
            # Add other fields if needed
        }

    #print(deployments["wikijs"])
    #print(deployments["bitwarden"])
    #print(deployments["unifi"]["unifi-db"]["replica_count"])
    #print(deployments)
"""    
    #compare_expected_replicas_count(array_list_deploy)
    generated_db = db_interaction.DB_generation(credentials.sql.url, credentials.sql.port, credentials.sql.user, credentials.sql.password,credentials.sql.database)
    
    ###operation:
    
    ## Server(s) supposed to be UP
    list_servers_up = db_interaction.Check_server_supposed_XXX(generated_db, "up", db_interaction.Give_current_hour(),db_interaction.Give_current_weekday())
    print("------------------------------------------")
    print("-----------------UP-----------------------")
    print("------------------------------------------")
    print(list_servers_up)
    #print(db_interaction.all_operations("running", list_servers_up))
    
    
    ## Server(s) supposed to be DOWN
    list_servers_down = db_interaction.Check_server_supposed_XXX(generated_db, "down", db_interaction.Give_current_hour(),db_interaction.Give_current_weekday())
    
    print("------------------------------------------")
    print("----------------DOWN----------------------")
    print("------------------------------------------")
    print(list_servers_down)
    #print(db_interaction.all_operations("stopped",list_servers_down))
    
    
    # disconnect from server
    generated_db.close()
    


if __name__ == "__main__":
    main()
