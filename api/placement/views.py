from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


import os
from pyairtable import Api
from pyairtable.formulas import match

print()
api = Api(os.environ.get('AIRTABLE_API_KEY'))
table = api.table(os.environ.get('IETAGRA_AIRTABLE_BASE_ID'), os.environ.get('PLACEMENT_AIRTABLE_TABLE'))
# Create your views here.


@api_view(["GET"])
def PlacementAPIOverview(request):
    api_urls = {
        "List All": "/placement-list-all/",
        "List Approved": "/placement-list-approved/",
        "Detail View": "/placement-detail/<str:pk>/",
        "Create": "/placement-create/",
        "Update": "/placement-update/<str:pk>/",
        "Delete": "/placement-delete/<str:pk>/",
    }

    return Response(api_urls)



@api_view(["GET"])
def PlacementListAll(request):
    records = table.all()
    return Response(records)


@api_view(["GET"])
def PlacementListApproved(request):
    formula = match({'status': 'Approved'})
    records = table.all(formula=formula)
    return Response(records)


@api_view(["GET"])
def PlacementCreate(request):
    if data := request.data:
        record = table.create(data)
        return Response(record, status=status.HTTP_201_CREATED)
    
    data_format = {
        "roll_no": "string",
        "student_name": "string",
        "student_branch": {
            "choices": [
                "Computer Science & Engineering",
                "Electronics & Communication Engineering",
                "Mechanical Engineering",
                "Civil Engineering",
                "Electrical Engineering",
            ]
        },
        'student_batch': {
            'id': 'rec6Z7nZw9j6V8z9c',
            'name': '2017 - 2021'
        },
        "company_name": "string",
        "student_salary": "number",
        "position_offered": "string",
        "offer_letter": "image",
        "remarks": "string",
    }
    return Response(data_format, status=status.HTTP_400_BAD_REQUEST)
