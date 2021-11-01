import requests
from requests.models import Response 

def legal_name_lookup(lei):
    #try: 
    resp =  requests.get(f"https://leilookup.gleif.org/api/v2/leirecords?lei={lei}")
    #except requests.exceptions.RequestException as err:
    #    return Response()
    