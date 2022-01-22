from datetime import datetime, timedelta
from calendar import HTMLCalendar
import calendar
from .models import Meeting


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:

			d += f'<li> {event.get_html_url}</li>'

		if day != 0:
			return f'<td class="calendar"><span class="date"> {day}</span><ul> {d} </ul></td>'
		return '<td ></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		
		for d, weekday in theweek:
		    if weekday!=6 and weekday!=5:
		        week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Meeting.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table style=" background-color:powderblue;" class="calendar" >\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		##cal += f'{self.formatweekheader()}\n'
		cal += f'<td class="calendar"><span class="date"> Monday </span><ul> </ul></td><td class="calendar"><span class="date"> Tuesday</span><ul> </ul></td><td class="calendar"><span class="date"> Wednesday </span><ul> </ul></td><td class="calendar"><span class="date"> Thursday</span><ul> </ul></td><td class="calendar"><span class="date"> Friday </span><ul> </ul></td>'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
