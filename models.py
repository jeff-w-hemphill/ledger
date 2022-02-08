from datetime import date
import json

class Loan:
    def __init__(self, id, amount, interest):
        self.id = id
        self.amount = amount
        self.interest = interest
        self.entries = []
        
  
    
    def addEntry(self, entry):
        self.entries.append(entry)
    
    def to_json(self):
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)
        

class Entry:
    def __init__(self, createdAt, effectiveDate, bucketId, value):
        self.createdAt = createdAt
        self.effectiveDate = effectiveDate
        self.bucketId = bucketId
        self.value = value
    
    def to_json(self):
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)