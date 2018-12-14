from db import entry
from datetime import timedelta, date, time, datetime
import pandas as pd


today = date.today()
today_timestamp = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
one_week = today + timedelta(days=7)
two_weeks = today + timedelta(days=14)



def price_comparison(wanted_date):
	data = (
		entry.select()
		.where(entry.date == wanted_date)
		.where(entry.timestamp >= today_timestamp)
	)

	all_hotels = []

	for row in data:
		all_hotels.append(row.hotel)
	all_hotels = set(all_hotels)

	for hotel in all_hotels:
		hotel_price = (
			entry.select()
			.where(entry.date == wanted_date)
			.where(entry.hotel == hotel)
			.where(entry.ota == hotel)
			.where(entry.timestamp >= today_timestamp)
			.get().price
		)
		
		#print(hotel + ': ' + str(hotel_price))

	all_otas = []

	for row in data:
	   all_otas.append(row.ota)

	for ota in all_otas:
		hotel_name = entry.select().where(entry.hotel==hotel)
		print(hotel_name)

		ota_price =(
			entry.select()
			.where(entry.date == wanted_date)
			.where(entry.ota != hotel_name)
			.where(entry.timestamp >= today_timestamp)
			.get().price
		)

		print(ota_price)


#if function to compare the hotel's price with the ota's price

# send email

	#print(hotel_price)

#price_comparison(today)
#price_comparison(one_week)
#price_comparison(two_weeks)
