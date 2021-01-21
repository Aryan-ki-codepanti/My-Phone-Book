
import mysql.connector as sqlcon

#Database details
#DB name : work
#Table name : contacts

#Attributes of a contact
#1.Name (Str) !primary key
#2.Nationality (Str)
#3.Phone(Work) (Long Int/Big int in sql)
#4.Sticky Note (Str/Text in sql)
#5.Profession (Str)
#6.Address (Str)

class Contact:

    database_name = "work"
    table_name = "contacts"

    def __init__(self,name,nationality,phone,note,profession,address):
        self.name = name
        self.nationality = nationality
        self.phone = phone
        self.note = note
        self.profession = profession
        self.address = address

    def add_to_table(self):
        query = "INSERT INTO {} VALUES('{}','{}',{},'{}','{}','{}')".format(Contact.table_name,
        self.name,self.nationality,self.phone,self.note,self.profession,self.address)

        db = sqlcon.connect(user = "root",host = "localhost",database = Contact.database_name,passwd = "12345")
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        db.close()

    #remove if exists and then add to table method continue
    def remove_contact_from_database(self):
        db = sqlcon.connect(host = "localhost",database = Contact.database_name,user = "root",passwd = "12345")
        cursor = db.cursor()
        
        if Contact.is_exists(self.name):
            cursor.execute("DELETE FROM {} WHERE NAME = '{}'".format(Contact.table_name,self.name))
            db.commit()
        db.close()

    def delete_if_exists_then_add(self):
        if Contact.is_exists(self.name):
            db = sqlcon.connect(user = "root",host = "localhost",database = Contact.database_name,passwd = "12345")
            cursor = db.cursor()
            cursor.execute("DELETE FROM {} WHERE NAME = '{}'".format(Contact.table_name,self.name))
            db.commit()
            db.close()

        self.add_to_table()

    @classmethod
    def is_exists(cls,name):
        db = sqlcon.connect(user = "root",host = "localhost",passwd = "12345",database = cls.database_name)
        cursor = db.cursor()
        cursor.execute(f"SELECT NAME FROM {cls.table_name}")
        
        names = [i[0] for i in cursor]

        if name in names:
            return True

        else:
            return False

        db.close()

    
    @classmethod
    def create_table(cls):
        db = sqlcon.connect(host = "localhost",user = "root",passwd = "12345",database = cls.database_name)
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")

        tables = [i[0] for i in cursor]
        if cls.table_name not in tables:

            query = f"CREATE TABLE {cls.table_name}(NAME VARCHAR(40),NATIONALITY VARCHAR(20),PHONE BIGINT,NOTE TEXT,PROFESSION VARCHAR(40),ADDRESS VARCHAR(100))"
            cursor.execute(query)

        db.close()

    @classmethod
    def create_database(cls):
        db = sqlcon.connect(host = "localhost",user = "root",passwd = "12345")
        
        cursor = db.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [i[0] for i in cursor]
        if cls.database_name not in databases:
            cursor.execute(f"CREATE DATABASE {cls.database_name}")
        db.close()
        cls.create_table()    

    @classmethod
    def contact_lookup(cls,name):
        
        db = sqlcon.connect(host = "localhost",user = "root",passwd = "12345",database = cls.database_name)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {} WHERE NAME = '{}'".format(cls.table_name,name))
        
        record =  list(cursor)[0]
        db.close()
        return record
    
    @classmethod
    def contact_lookup_by_field_matching(cls,key,value):
        #key = "NAME"/"NATIONALITY"/"NOTE"/"ALL"
        #If value is other than above then display all results

        db = sqlcon.connect(host = "localhost",user = "root",passwd = "12345",database = cls.database_name)
        cursor = db.cursor()
        
        query1 = "SELECT * FROM {} WHERE LOWER(NAME) LIKE '%{}%' ORDER BY NAME".format(cls.table_name,value.lower())
        query2 = "SELECT * FROM {} WHERE LOWER(NATIONALITY) LIKE '%{}%' ORDER BY NAME".format(cls.table_name,value.lower())
        query3 = "SELECT * FROM {} WHERE LOWER(NOTE) LIKE '%{}%' ORDER BY NAME".format(cls.table_name,value.lower())

        if value.isspace() or not value:
            result = cls.get_all_contacts()
        elif key == "NAME":
            cursor.execute(query1)
            result = list(cursor)

        elif key == "NATIONALITY":
            cursor.execute(query2)
            result = list(cursor)

        elif key == "NOTE":
            cursor.execute(query3)
            result = list(cursor)
        elif key == "ALL":
            result = set()

            for i in [query1,query2,query3]:
                cursor.execute(i)
                result.update(list(cursor))

            sort_func = lambda x:x[0]
            result = list(result)
            result.sort(key = sort_func)
        else:
            result = []
        db.close()
        return result

    @classmethod
    def get_all_contacts(cls):
        db = sqlcon.connect(host = "localhost",user = "root",passwd = "12345",database = cls.database_name)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {} ORDER BY NAME".format(cls.table_name))

        l = [i for i in cursor]    
        db.close()
        
        return l

    @classmethod
    def get_nationalities(cls):
        db = sqlcon.connect(user = "root",host = "localhost",passwd = "12345",database = cls.database_name)
        cursor = db.cursor()

        cursor.execute("SELECT LOWER(NATIONALITY) FROM {}".format(cls.table_name))
        result = list(filter(lambda x:bool(x),[i[0] for i in cursor]))
        db.close()
        return result
#Contact.create_database()