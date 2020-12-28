import sqlite3

def create_table():
  conn = sqlite3.connect('database.db')
  with conn:
    curs = conn.cursor()

    # retrieve data from database
    sql = """select i.facility_name, i.facility_address, i.facility_city, i.facility_zip 
    from inspections as i, violations as v 
    where i.serial_number = v.serial_number 
    group by facility_name 
    order by facility_name
    """

    # Display the data into console & store data into list 
    rows = []
    for row in curs.execute(sql):
      print(row[0])
      rows.append(row)

    # create table "Previous Violations"
    curs.execute("DROP TABLE IF EXISTS 'Previous Violations'")
    curs.execute("""CREATE TABLE 'Previous Violations'(
                    facility_name TEXT,
                    facility_address TEXT,
                    facility_city TEXT,
                    facility_zip VARCHAR(15))
                    """)

    # insert data into table
    curs.executemany("INSERT INTO 'Previous Violations' VALUES (?,?,?,?)", rows)

  conn.close()

def number_violations():
  conn = sqlite3.connect('database.db')
  with conn:
    curs = conn.cursor()
    # retrieve data from database
    sql = """select i.facility_name, count(v.serial_number)
            from inspections as i, violations as v
            where i.serial_number = v.serial_number  
            group by facility_name 
            order by count(v.serial_number)"""
    rows = curs.execute(sql)
    
    # display the data
    print("{:55}{}".format("Business", "Number of Violations"))
    for row in rows:
      print("{:55}{}".format(row[0], row[1]))
  conn.close()
  
if __name__ == '__main__':
  print("\n==================Distinctive Business Name====================\n")
  create_table()
  print("\n============Number of violations for each business=============\n")
  number_violations()
