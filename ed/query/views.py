from django.shortcuts import render
from django.http import HttpResponse
# requests lib, 3rd party
import requests

# Create your views here.

def do_query(request):
    # read file from disk
    query = open('./query.json', 'r')
    actual_query = query.readlines()
    # actual_query should contain a string
    
    print(actual_query[0])
    # headers if you need to send a request directly to elasticsearch
    headers = {"Content-Type": "application/json"}

    # send requests
    r = requests.post('http://localhost:9200/_search', data=query, headers=headers)

    # es.search(data=actual_query)
    # convert response from elasticsearch to json
    json = r.json()


    #return response to user
    return HttpResponse(json)