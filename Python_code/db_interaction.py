import time
import pymysql
#simport function
import credentials
import datetime
import cryptography



def DB_generation(host_in,port_in,user_in,password_in,db_in):
    db = pymysql.connect(host=host_in, port=port_in, user=user_in, passwd=password_in,db=db_in)
    return db


def Launch_sql_query(sql,db):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    #print(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        result_machine = []
        #result_machine_type = []
        for row in results:
            result_machine_type = []
            id_scenario = row[0]
            id_hour = bool(row[1])
            name = row[2]
            namespace = row[3]
            replicas = row[4]
            
            result_machine_type.append(namespace)
            result_machine_type.append(name)
            result_machine_type.append(replicas)
            result_machine.append(result_machine_type)
        return result_machine

    except:
        print ("Error: unable to fetch data")


#Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
def Give_current_weekday():
    #weekday = datetime.datetime.today().weekday()
    weekday = datetime.date.today().strftime("%A")
    return weekday

def Give_current_hour():
    now = datetime.datetime.now()
    return now.hour


def Check_server_supposed_XXX(generated_db_in,wanted_status,Wanted_hour,Wanted_day):
    sql_in=""
    if wanted_status == "up" or wanted_status == "start":
        sql_in = "select scenario_hour.id_scenario , scenario_hour.state_at_" + str(Wanted_hour) + " , machine.name, machine.namespace, machine.replicas from scenario_hour,machine where state_at_" + str(Wanted_hour) + "=1 and machine.hour_behaviour_id=scenario_hour.id_scenario;"
        #sql_in = "select scenario_hour.id_scenario , scenario_hour.state_at_" + str(Wanted_hour) + " , machine.name, machine.id_proxmox, machine.type  from scenario_hour,machine,scenario_day_of_week where (state_at_" + str(Wanted_hour) + "=1 and state_" + str(Wanted_day) + "=1) and machine.hour_behaviour_id=scenario_hour.id_scenario and machine.day_behaviour_id=scenario_day_of_week.id_scenario;"
    elif wanted_status == "down" or wanted_status == "stop":
        sql_in = "select scenario_hour.id_scenario , scenario_hour.state_at_" + str(Wanted_hour) + " , machine.name, machine.namespace, machine.replicas from scenario_hour,machine where state_at_" + str(Wanted_hour) + "=0 and machine.hour_behaviour_id=scenario_hour.id_scenario;"
        #sql_in = "select scenario_hour.id_scenario , scenario_hour.state_at_" + str(Wanted_hour) + " , machine.name, machine.id_proxmox, machine.type  from scenario_hour,machine,scenario_day_of_week where (state_at_" + str(Wanted_hour) + "=0 or state_" + str(Wanted_day) + "=0) and machine.hour_behaviour_id=scenario_hour.id_scenario and machine.day_behaviour_id=scenario_day_of_week.id_scenario;"
    else:
        print("error value")
    return_value = Launch_sql_query(sql_in, generated_db_in)
    return return_value

def Is_the_server_already_wanted_state(id_machine, wanted_state,instance_type):
    #stopped/running
    bool_result = ""
    proxmox = function.proxmox_connection(credentials.proxmox.server1.url_proxmox,credentials.proxmox.server1.user,credentials.proxmox.server1.password)
    if str(function.check_state_mix(id_machine,wanted_state,proxmox,instance_type)) == str(wanted_state):
        bool_result = True
    else:
        bool_result = False
    return bool_result

def all_operations(wanted_state,list_machine):
    info_to_display = ""
    if wanted_state == "running":
        operation_to_perform = "start"
    elif wanted_state == "stopped":
        operation_to_perform = "stop"
    else:
        print("Incorrect wanted state")


    for machine_target in list_machine:
        if not(Is_the_server_already_wanted_state(machine_target[0], wanted_state,machine_target[1])):
            function.action(False,machine_target[0],operation_to_perform,machine_target[1])
            print(str(machine_target[0])+" is now "+str(wanted_state))
        elif Is_the_server_already_wanted_state(machine_target[0], wanted_state,machine_target[1]):
            info_to_display = "operation already performed for "+machine_target[2]
            print(info_to_display)
    #return info_to_display
    return ""

def main():
    time.sleep(20)
    generated_db = DB_generation(credentials.sql.url, credentials.sql.port, credentials.sql.user, credentials.sql.password,credentials.sql.database)

    ###operation:

    ## Server(s) supposed to be UP
    list_servers_up = Check_server_supposed_XXX(generated_db, "up", Give_current_hour(),Give_current_weekday())
    print("hey")
    print(credentials.sql.url)
    print("------------------------------------------")
    print("-----------------UP-----------------------")
    print("------------------------------------------")
    print(list_servers_up)
    print(all_operations("running", list_servers_up))


    ## Server(s) supposed to be DOWN
    list_servers_down = Check_server_supposed_XXX(generated_db, "down", Give_current_hour(),Give_current_weekday())

    print("------------------------------------------")
    print("----------------DOWN----------------------")
    print("------------------------------------------")
    print(list_servers_down)
    print(all_operations("stopped",list_servers_down))


    # disconnect from server
    generated_db.close()


if __name__ == "__main__":
    main()


"""
TO DO:
 EXTRACT TYPE OF MACHINE
 CREATE FUNCTION TO CHECK IF A MACHINE IS ALREADY DOWN OR NOT
 ADD FIELD IN SQL WITH PROJECT AND PUT DESCRIPTION -> ATTACH MACHINE TO PROJECT

"""
