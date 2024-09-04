from libray_code import sqlite_not_result, sqlite_have_result

database_request = 'you sqlite request'

def operation_EasySqlite_not_result():
    try:
        if sqlite_not_result("new_database.db", database_request) == 'Sucsefully':
            print("Operation completed")
        else:
            print("operation not completed")
    except:
        print("main script error")


def operation_EasySqlite_have_result():
    try:
        result = sqlite_have_result('new_database.db', database_request, 0, None)
        if result == "Error":
            print('Error in operation have result')
        else:
            result = str(result)
    except:
        print("main script error")
    