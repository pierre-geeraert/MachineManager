import pymysql
from Cloudmanager.dashboard import function
from Cloudmanager.dashboard import credentials
import datetime


def DB_generation(host_in,port_in,user_in,password_in,db_in):
    db = pymysql.connect(host=host_in, port=port_in, user=user_in, passwd=password_in,db=db_in)
    return db


def Launch_sql_query(sql,db):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    # Prepare SQL query to INSERT a record into the database.

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        result_machine = []
        for row in results:
            id_scenario = row[0]
            id_hour = bool(row[1])
            name = row[2]
            proxmox = row[3]
            result_machine.append(proxmox)
        return result_machine

    except:
        print ("Error: unable to fetch data")


#Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
def Give_current_weekday():
    weekday = datetime.datetime.today().weekday()
    return weekday

def Give_current_hour():
    now = datetime.datetime.now()
    return now.hour


def Check_server_supposed_XXX(generated_db_in,wanted_status,Wanted_hour):
    #Wanted_hour = "18"
    sql_in=""
    if wanted_status == "up":
        sql_in = "select scenario_hour.id_scenario , scenario_hour.state_at_" + str(Wanted_hour) + " , machine.name, machine.id_proxmox from scenario_hour,machine where state_at_" + str(Wanted_hour) + "=1 and machine.hour_behaviour_id=scenario_hour.id_scenario;"
    elif wanted_status == "down":
        sql_in = "select scenario_hour.id_scenario , scenario_hour.state_at_" + str(Wanted_hour) + " , machine.name, machine.id_proxmox from scenario_hour,machine where state_at_" + str(Wanted_hour) + "=0 and machine.hour_behaviour_id=scenario_hour.id_scenario;"

    return_value = Launch_sql_query(sql_in, generated_db_in)
    return return_value

def Check_server_already_wanted_state(id_machine,wanted_state):
    #stopped/running
    bool_result = ""
    proxmox = function.proxmox_connection(credentials.zeus.url_proxmox,credentials.zeus.user,credentials.zeus.password)
    if str(function.check_state(id_machine,wanted_state,proxmox)) == str(wanted_state):
        bool_result = True
    else:
        bool_result = False
    return bool_result

def Perform_action():
    return 0

def main():

    generated_db = DB_generation('domain.com', 3306, 'user', 'password',
                                 'database')

    list_servers = Check_server_supposed_XXX(generated_db, "up", Give_current_hour())

    print(list_servers)
    for server in list_servers:
        XXX

    # disconnect from server
    generated_db.close()

    print(Check_server_already_wanted_state(112,"stopped"))

if __name__ == "__main__":
    main()


"""
TO DO:
 CREATE 2 FUNCTION(UP/DOWN) TO CHECK AND ALSO TO PERFORM CORRECT ACTION
 CREATE --MAIN-- IN ORDER TO LAUNCH THIS PROGRAMM THROUGH CRON
 EXTRACT TYPE OF MACHINE
 CREATE FUNCTION TO CHECK IF A MACHINE IS ALREADY DOWN OR NOT
 ADD FIELD IN SQL WITH PROJECT AND PUT DESCRIPTION -> ATTACH MACHINE TO PROJECT

"""
