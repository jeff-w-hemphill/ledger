import requests
from models import Entry, Loan
from datetime import date, timedelta
import json
from flask import jsonify

# 1. Create the buckets in in-memory storage

if __name__ == '__main__':

    def create_buckets():
        
        new_buckets = [
                        {'identifier': 'accounts-receivable-principal'},
                        {'identifier': 'accounts-receivable-interest'},
                        {'identifier': 'income-interest'},
                        {'identifier': 'future-receivable-principal'},
                        {'identifier': 'loan-commitment-liability'},
                        {'identifier': 'cash'}]

        ENDPOINT = 'http://127.0.0.1:5000/ledger/buckets'
        for bucket in new_buckets:
            print(bucket)
            r = requests.post(url = ENDPOINT, data = bucket)
        
    create_buckets()    


# 2. Create the loan by adding ledger entries for origination of loan
loan = Loan(1, 1100, 0.08)
frp = Entry(str(date.today()), str(date.today()) ,'future-receivable-principal', loan.amount)
lcl = Entry(str(date.today()), str(date.today()),'loan-commitment-liability', -loan.amount)

loan.addEntry(frp)
loan.addEntry(lcl)

# 3. Activate the loan by adding the ledger entries specified in “Activation of the Loan”
lcl2 = Entry(str(date.today()), str(date.today()),'loan-commitment-liability', loan.amount)
frp2 = Entry(str(date.today()), str(date.today()) ,'future-receivable-principal', -loan.amount)

loan.addEntry(frp2)
loan.addEntry(lcl2)

arp = Entry(str(date.today()), str(date.today()),'accounts-receivable-principal', loan.amount)
cash = Entry(str(date.today()), str(date.today()) ,'cash', -loan.amount)

loan.addEntry(arp)
loan.addEntry(cash)
# 4. Accrue daily interest for 60 days, booking the interest daily using the above API as specified in “Daily Interest Accrual”
for i in range(60):
    day_delta = timedelta(days=1)*i
    ari = Entry(str(date.today() + day_delta), str(date.today() + day_delta),'accounts-receivable-interest', loan.amount * loan.interest / 365)
    ii = Entry(str(date.today() + day_delta), str(date.today() + day_delta),'income-interest', -loan.amount * loan.interest / 365)
    
    loan.addEntry(ari)
    loan.addEntry(ii)
