from datetime import datetime, timedelta
def getIDbyTime(dt):
# dt is datetime type

  y= dt.year-2000
  m= 12
  d= 31
  h=23
  min= 0

  id= int ( y* 10000000 + m * 100000 + d*1000 + h*10 + min/10)
  return id
c= datetime.now()
print (getIDbyTime(c))
