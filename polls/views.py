from django.shortcuts import render
from django.http import HttpResponse
import json




def index(request):
  some_data_to_dump = {
    'some_var_1': 'What is your favorite color?',
    'some_var_2': 'Is it red?',
  }

  data = json.dumps(some_data_to_dump)

  return HttpResponse(data, content_type='application/json')

  



 