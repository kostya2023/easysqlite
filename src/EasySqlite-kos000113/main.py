import sqlite3 as db

def sqlite_not_result(base_data_name, sql_request):
    try:
        base_data_name = str(base_data_name)
        sql_request = str(sql_request)
        sucsefull = 'Sucsefully'
        Unsucsefull = 'Error'
        
        connection = db.connect(base_data_name)
        cursor = connection.cursor()
        cursor.execute(sql_request)
        connection.commit()
        return sucsefull
    
    except:
        print("Error in sqlite have result")
        return Unsucsefull
    
    finally:
        connection.close()

def sqlite_have_result(base_data_name, sql_request, choice_of_fet, fetchmany_numbers):
    try:
        base_data_name = str(base_data_name)
        sql_request = str(sql_request)
        Unsucsefull = 'Error'
        choice_of_fet = int(choice_of_fet)
        fetchmany_numbers = int(fetchmany_numbers)
        
        connection = db.connect(base_data_name)
        cursor = connection.cursor()
        cursor.execute(sql_request)
        
        if choice_of_fet == 0:
            data = cursor.fetchall()
        elif choice_of_fet == 1:
            data = cursor.fetchmany(fetchmany_numbers)
        elif choice_of_fet == 2:
            data = cursor.fetchone()
            
        for datas in data:
            return datas
    
    except:
        print("Error in sqlite have result")
        return Unsucsefull
    
    finally:
        connection.close()
        