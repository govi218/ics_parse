from icalendar import Calendar, Event
from datetime import datetime
import time


cal_ics = open('example.ics')
gcal = Calendar.from_ical(cal_ics.read())
employee_dict = {}
for component in gcal.walk():
	if component.name == "VEVENT":
		print component.get('summary')
		start = component.get('dtstart')
		end = component.get('dtend')
		print start.dt
		print end.dt
		out = "duration: " + str(end.dt - start.dt)
		print out
		wage = str(15.75*((int(time.mktime(end.dt.timetuple())) 
			- int(time.mktime(start.dt.timetuple())))/3600))
		print "wage: " + wage + '\n'

		if employee_dict.has_key(component.get('summary')):
                        employee_dict[component.get('summary')] = float(employee_dict[component.get('summary')]) + float(wage)
                else:
                        employee_dict[component.get('summary')] = float(wage)


print '\n'

for employee in employee_dict:
        print employee + " " + str(employee_dict[employee]) + '\n'
cal_ics.close()
