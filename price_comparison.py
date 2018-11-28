from sqlalchemy import *
import pandas as pd
from datetime import timedelta, date, time, datetime
engine = create_engine('XXXX')
df = pd.read_sql_query("SELECT * FROM entry", engine)

#defining time
today = datetime.now()
one_week = today + timedelta(days=7)
two_weeks = today + timedelta(days=14)

cheaper_offers = []

def price_comparison(wanted_date):
''' takes a date and compares prices between the hotel and other providers'''
    df_for_wanted_date = df[df.date == wanted_date.strftime('%Y-%m-%d')] 
    my_hotel= df_for_wanted_date[df_for_wanted_date.ota =='XXXXXX'].price.iloc[0]
    other_hotels = df_for_wanted_date[df_for_wanted_date.ota !='XXXXXX']

    cheaper_offers.append(f'\n\nOn {wanted_date} these providers are offering a better deal:')
    for row in other_hotels.itertuples():
        if row.price <= my_hotel:
            cheaper_offer_info = f'\n{row.ota} is {my_hotel - row.price} cheaper. The price is {row.price} On {row.date}'
            cheaper_offers.append(cheaper_offer_info)
            
price_comparison(today)
price_comparison(one_week)
price_comparison(two_weeks)

#sending email - TO BE updated
server = "email.server"
sender = ""
recipient =""
subject= "Metasearch warning"
message = ','.join(cheaper_offers) + '.'

#TODO create if function to send email if list cheaper_offers has anything appended
  if len(cheaper_offers) > 3:
      #send email
      server = smtplib.SMTP(server)
            server.login("NAME","PAssword")
            server.sendmail(sender, recipient, subject, message)
            server.quit()
            
#TODO if price has been lower for more than 24 hours, append to list and send email           
  
  
  
