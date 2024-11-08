import datetime
import time
import calendar
issuedate=datetime.datetime.now().date()
returndate=issuedate+datetime.timedelta(days=14)
id=str(issuedate)
rd=str(returndate)
print(id)
print(rd)
current=datetime.datetime.now()
print(current)
ct=time.ctime()

fine=0
returndate1=issuedate+datetime.timedelta(days=21)
print(returndate1)

late=returndate1-returndate
latedays=late.days
fine=latedays*2
print(fine)

#m=datetime.datetime.now().month
#y=datetime.datetime.now().year
#print(m)
#print(y)
#print(calendar.month(y,m))
#print(ct)
#cal=calendar.month(2008,1)
#print(cal)

#m=datetime.datetime.now().month
#y=datetime.datetime.now().year
#cal2=calendar.month(y,m)
#print(cal2)

#ctm=time.localtime()
#print(time.strftime('%a, %d %b %Y %H:%M:%S %Z', ctm))

