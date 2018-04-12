"""
Developed by: Yubaraj Poudel
yubarajpoudel708@gmail.com
convert the json file to sqllite file
provide the json file
prvide the name of the output file
"""
import sys
import sqlite3
import json
import os


def __convert(*args):
    try:
        option = 'M'
        while option.lower() == 'm':
            __showOptions()
            choice = int(input("Enter your choice "))
            if choice == 1:
                # print(args[2])
                __createTable(args[2])
                pass
            elif choice == 2:
                insertDataInTable(args[0], args[2])
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                tableJSON = input("Enter the file name: ")
                if tableJSON.lower().endswith(".json"):
                    with open(tableJSON, "r") as inputTableJSON:
                        for table in json.load(inputTableJSON):
                            createTableWith(table['name'], table['schemas'], args[2])
                else:
                    print("Invalid json file. The file name must endswith .json format")
                pass
            elif choice == 9:
                sys.exit(0)
                pass

            option = input("Enter m to continue: ")

    except Exception as e:
        print(e)


def insertDataInTable(data, dbPath):
    con = sqlite3.connect(dbPath)
    cursor = con.cursor()
    # parse the json and add the value in table
    dataJSON = json.loads(data)
    # print(dataJSON)
    # for tableKey in dataJSON :
    mSql = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(mSql)
    for tableName in cursor.fetchall():

        # print(tableName[0])
        tableDatas = dataJSON[tableName[0]]
        cursor.execute("PRAGMA table_info({})".format(tableName[0]))
        schemaList = cursor.fetchall()
        # tableKeyvalue = "["
        tableKeyvalue = []
        for tableData in tableDatas:
            # print(tableData)
            # data = "("
            data = []
            # first = True
            for schema in schemaList:
                # if not first:
                # 	data = data + ","
                # data = data + "\'"+ tableData[schema[1]]+"\""
                # first = False
                data.append(tableData[schema[1]])
            # data = data + ")"
            # print(data)

            # tableKeyvalue = tableKeyvalue + data+","
            tableKeyvalue.append(data)
        # print(json.dumps(tableKeyvalue))
        # tableKeyvalue = tableKeyvalue[:-1] + "]"
        # print(tableKeyvalue)

        optinalParam = "("
        for i in range(0, len(schemaList)):
            optinalParam = optinalParam + "?,"
        optinalParam = optinalParam[:-1] + ")"

        # print(optinalParam)
        print('Query = insert into {} values {}'.format(tableName[0], optinalParam))
        cursor.executemany('insert into {} values {}'.format(tableName[0], optinalParam), tableKeyvalue)
        con.commit()
        print("Data inserted at {} successfully".format(tableName[0]))
    # print(data)
    # print(dataJSON[tableName[0]])

    con.close()


# print(data)

def __showOptions():
    os.system("clear")
    print("....................................\n")
    print("Choose the option\n")
    print("1. Create new table\n")
    print("2. Insert data into table\n")
    print("3. Delete table\n")
    print("4. Alter table\n")
    print("5. Create Tables from jsonfile \n")
    print("9. Press 9 for exit\n")
    print(".............................")


def __createTable(dbPath):
    nextTable = 'y'
    while nextTable.lower() == 'y':
        tableName = input("Enter the table name : ")
        schemas = input("Enter the schema separated by space (for eg name,phone):")
        # print("tableName = {}, schemas = {}".format(tableName, schemas))
        createTableWith(tableName, schemas, dbPath)
        nextTable = input("Do you want to add more tables ? (Y | N): ")


def createTableWith(tableName, schemas, dbPath):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()

    # Create table
    sql = "CREATE TABLE {}(".format(tableName)
    first = True
    for schema in schemas.split(","):
        if not first:
            sql = sql + ","

        sql = sql + "{} text".format(schema)
        first = False
    sql = sql + ")"
    print(sql)
    c.execute(sql)
    print("{} created successfully \n".format(tableName))
    conn.commit()
    conn.close()


def main():
    # print("arguments lenght = %s"%(str(len(sys.argv))))
    try:
        if len(sys.argv) == 3:
            # print("valid")
            # print(sys.argv[1])
            if (sys.argv[1].lower().endswith('.json')):
                with open(sys.argv[1], "r") as inputJSON:
                    data = inputJSON.read()

                dbName = input("Enter Preferred DatabaseName ")
                # print("Database Name = {}".format(dbName))
                destination = sys.argv[2]
                # with open(destination, "w") as outputFile:
                __convert(data, dbName, destination)
            # print(data)
            else:
                print("invalid input jsonfile")
        else:
            print("invalid")
    except:
        print("Error in providing the arguments")


if __name__ == '__main__':
    main()
