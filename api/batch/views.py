from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


import os
from pyairtable import Api
from pyairtable.formulas import match


api = Api(os.environ.get('AIRTABLE_API_KEY'))
table = api.table(os.environ.get('IETAGRA_AIRTABLE_BASE_ID'), os.environ.get('BATCH_AIRTABLE_TABLE'))
# Create your views here.


@api_view(["GET"])
def BatchListAll(request):
    fields = [
        'batch',
        'Placements',
    ]
    records = table.all(fields=fields)
    return Response(records)


@api_view(["GET"])
def BatchDetail(request, pk):
    formula = match({'batch': pk})
    records = table.all(formula=formula)
    return Response(records)

