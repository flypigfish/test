import cx_Oracle
import j

try:
    conn= cx_Oracle.connect('system/manager@192.168.127.128/ZHI')
except cx_Oracle.DatabaseError as e:
    error,=e.args
    print('Connect error ', error.code)
    exit(-1)
    
print('Connect oracle ok')
