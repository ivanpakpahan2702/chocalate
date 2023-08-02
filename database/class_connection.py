import pymysql


class db_connection:

    def __init__(self):
        self.Database = 'cochalate_db'
        self.User     = 'root'
        self.Password = ''
        self.Hostname = 'localhost'

        self.connection_database = pymysql.connect(host=self.Hostname, user=self.User, password=self.Password)
        self.connection          = self.connection_database.cursor()
        self.connection.execute("USE %s" % (self.Database))
    

    def select_data(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state
        else:
            queri = queri + col + ' FROM ' + table_name
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()
        return results
    
    
    def search_data(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        order_state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" IN "+str(statement[x])) + ' AND '
            state = state[:-5]
            j = 1
            for i in statement['id_postingan']:
                order_state = order_state + 'WHEN id_postingan = '+str(i)+' then '+str(j)+' '
                j = j + 1
            order_state = order_state + 'END ASC'
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state+' ORDER BY CASE '+ order_state
        else:
            queri = queri + col + ' FROM ' + table_name 
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()    
        return results
    
    
    def add_data(self, table_name = '',data_field=(), data = ()):
        data_field = str(data_field)
        queri = 'INSERT INTO ' + str(table_name) + data_field.replace("'","") +' VALUE '+ str(data)
        try:
            print(queri)
            self.connection.execute(queri)
            self.connection_database.commit()
            result = 'Successed'
        except:
            print("Something Wrong!")
            self.connection_database.rollback()
            result = 'Failed'
        finally:
            self.connection.close()
        return result
    

    def update_data(self, table_name = '', data_field=(), data = (),statement={}):
        string = ''

        for i in range(len(data_field)):
            if type(data[i])==str:
                data_ = '"'+str(data[i])+'"'
            else:
                data_ = data[i]
            string = string + data_field[i] + '=' +data_ + ','
        string = string[:-1]
        

        state = ''

        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = 'UPDATE '  + str(table_name) + ' SET '+string+" WHERE "+state
        
        try:
            print(queri)
            self.connection.execute(queri)
            self.connection_database.commit()
            result = 'Successed'
        except:
            print("Something Wrong!")
            self.connection_database.rollback()
            result = 'Failed'
        finally:
            self.connection.close()
        return result