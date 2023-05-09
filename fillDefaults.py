import pyodbc
from datetime import datetime, timedelta

def roundDate(dt):

    discard = timedelta(minutes=dt.minute % 10,
                        seconds=dt.second,
                        microseconds=dt.microsecond)
    dt -= discard
    if discard >= timedelta(minutes=5):
        dt += timedelta(minutes=10)
    return dt
###############################################################


def getIDbyTime(dt):
# dt is datetime type

  y= dt.year-2000
  m= dt.month
  d= dt.day
  h=dt.hour
  min= dt.minute
  id= int ( y* 10000000 + m * 100000 + d*1000 + h*10 + min/10)
  return id

###################################################################
def getLastTimeOfTab(tabName):
  cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=agr-dcontrol;"
                      "Trusted_Connection=yes;")

  cursor = cnxn.cursor()

  com=f"SELECT MAX (datetime)  FROM {tabName}";
  try:
      cursor.execute(com)
      row = cursor.fetchone()
      if row == None or row[0] == None:
        dt= datetime.now()
        dt = roundDate(dt)
      else:
       dt = roundDate(row[0])
  except:
      print ("cannot connect to table")
      dt = datetime.now() - timedelta(minutes=10)
      dt = roundDate(dt)

  return dt

################################################################

def getNext10mTime(dt):
    delta10m = timedelta(minutes=10)
    nextdate = dt+ delta10m
    return nextdate

################################################################
def makeTimeGridToTables(tabName):
  lastTime = getLastTimeOfTab(tabName)

  dt = datetime.now()
  delta10days= timedelta(days=2)
  enddate= dt+delta10days

  cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=agr-dcontrol;"
                      "Trusted_Connection=yes;")

  cursor = cnxn.cursor()
  tabVLDname= tabName+"v"
  nextdate= getNext10mTime(lastTime)

  while (nextdate< enddate):
    nextid= getIDbyTime(nextdate)
    dateStr=nextdate.strftime("%Y-%m-%dT%H:%M:%S")
    com = f"INSERT INTO {tabName} (id,datetime) VALUES ({nextid},'{dateStr}')"
    comVLD=f"INSERT INTO {tabVLDname} (id,datetime) VALUES ({nextid},'{dateStr}')"
    nextdate = getNext10mTime(nextdate)
    print (com)
    cursor.execute(com)
    cursor.execute(comVLD)
  cursor.commit()

def makeTimeGridToVLDTable(tabName):
      lastTime = getLastTimeOfTab(tabName)

      dt = datetime.now()
      delta10days = timedelta(days=2)
      enddate = dt + delta10days

      cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=localhost;"
                            "Database=agr-dcontrol;"
                            "Trusted_Connection=yes;")

      cursor = cnxn.cursor()

      nextdate = getNext10mTime(lastTime)

      while (nextdate < enddate):
          nextid = getIDbyTime(nextdate)
          dateStr = nextdate.strftime("%Y-%m-%dT%H:%M:%S")
          com = f"INSERT INTO {tabName} (id,datetime) VALUES ({nextid},'{dateStr}')"
          nextdate = getNext10mTime(nextdate)
          print(com)
          cursor.execute(com)
      cursor.commit()
makeTimeGridToTables(("z13"))
