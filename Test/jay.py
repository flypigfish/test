import jaydebeapi as jay

arg_mysql="E:/Development/java/mysql-connector-java.jar"
arg_oracle="E:/Development/java/ojdbc7.jar"

# jdbc_connect_string='jdbc:mysql://127.0.0.1:3306/xinjiang'
# user='root'
# password='162526'
# jay.connect('driverName','connection_string', user, password)
#'jdbc:oracle:thin:user/pass@server:1521:dbname'

print('Begin')
try:
    #conn=jay.connect("com.mysql.jdbc.Driver", ['jdbc:mysql://127.0.0.1:3306/xinjiang','root','162526'], arg_mysql)
    conn=jay.connect("oracle.jdbc.driver.OracleDriver", ['jdbc:oracle:thin:@192.168.127.128:1521:ZHI', 'system','manager'],arg_oracle)
except jay.exceptions as e:
    print('fail:', e.args())
    exit(-1)
    
print('Connect successfully')