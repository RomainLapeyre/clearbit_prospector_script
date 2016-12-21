# clearbit_prospector_script
Given a domain, get the contact info of the CEO. 

# How to us it
* Create an account on [Clearbit](http://clearbit.com)
* Get your API key 
* Add your api key to `get_prospects.py`, line 25
* Edit the role name to the desired one. The list of available roles can be found [here](http://support.clearbit.com/article/120-employment-role-and-seniority)
* Add the domains you want to look up to `domains.csv`
* Run `python get_prospects.py` 

This will create a file called `contacts.csv` with the list of contacts
