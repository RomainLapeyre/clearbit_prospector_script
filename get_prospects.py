import csv
import requests
import pandas as pd
from collections import defaultdict, OrderedDict
import re

contacts = []
role = 'ceo'  # Select the desired role of the contact

# Import company list from a csv with a header row "url"
domains = defaultdict(list)  # each value in each column is appended to a list
with open('domains.csv') as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            domains[k].append(v)  # append the value into the appropriate list
    domains = domains['domain']  # remove the head row
print domains


# Let's find the right person at the company with Clearbit prospector
def get_prospect(company, name, title, domain, role):
    url = 'https://prospector.clearbit.com/v1/people/search'
    payload = {'domain': domain, 'limit': 1, 'role': role}
    headers = {'Authorization': 'Bearer your_api_key'}
    people = requests.get(url, params=payload, headers=headers)
    if not people:
        print("List is empty")
    else:
        results = people.json()
        for r in results:  # adding this if we get more than 1 person
            contact = OrderedDict()
            contact['givenName'] = re.sub('[^a-zA-Z0-9-_*.]', '', r['name']['givenName'])
            contact['familyName'] = re.sub('[^a-zA-Z0-9-_*.]', '', r['name']['familyName'])
            contact['email'] = r['email']
            contact['domain'] = domain
            contact['title'] = r['title']
            contact['role'] = r['role']
            print contact
            contacts.append(contact)


for domain in domains:
    get_prospect('', '', '', domain, role)

pd.DataFrame(contacts).to_csv('contacts.csv')
