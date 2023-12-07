from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
import json
from django.conf import settings

import os
from pyairtable import Api
from pyairtable.formulas import match


api = Api(os.environ.get('AIRTABLE_API_KEY'))
table = api.table(os.environ.get('IETAGRA_AIRTABLE_BASE_ID'), os.environ.get('PLACEMENT_AIRTABLE_TABLE'))
# Airtable API endpoint
BASE_URL = f"https://api.airtable.com/v0/{os.environ.get('IETAGRA_AIRTABLE_BASE_ID')}/{os.environ.get('PLACEMENT_AIRTABLE_TABLE')}"
# Create your views here.



@api_view(["GET"])
def PlacementListAll(request):
    fields = [
        'roll_number',
        'student_name',
        'student_branch',
        'student_batch',
        'company_name',
        'student_salary',
        'position_offered',
        'offer_letter',
        'remarks',
        'status',
    ]
    records = table.all(fields=fields)
    return Response(records)


@api_view(["GET"])
def PlacementListApproved(request):
    formula = match({'status': 'Approved'})
    fields = [
        'roll_number',
        'student_name',
        'student_branch',
        'student_batch',
        'company_name',
        'student_salary',
        'position_offered',
        'offer_letter',
        'remarks',
        'status',
    ]
    records = table.all(formula=formula, fields=fields)
    return Response(records)


class PlacementCreate(APIView):
    def post(self, request, *args, **kwargs):
        base_url = BASE_URL
        
        # Airtable API headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        # check if request has a data or not
        if not request.data:
            return Response({"error": "Please provide the data to create a record"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Data to be sent to Airtable API
        data = {
            "records": [
                {
                    "fields": {
                        "roll_number": request.data.get("roll_number"),
                        "student_name": request.data.get("student_name"),
                        "student_branch": request.data.get("student_branch"),
                        "student_batch": request.data.get("student_batch"),
                        "company_name": request.data.get("company_name"),
                        "student_salary": request.data.get("student_salary"),
                        "position_offered": request.data.get("position_offered"),
                        "offer_letter": request.data.get("offer_letter"),
                        "remarks": request.data.get("remarks"),
                    }
                },
            ]
        }

        # Send POST request to Airtable API
        response = requests.post(base_url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == status.HTTP_200_OK:
            return Response({"message": "Record created successfully"}, status=status.HTTP_201_CREATED)
        else:
            # If unsuccessful, return the error details
            error_message = json.loads(response.text).get("error", {}).get("message", "Unknown error")
            return Response({"error": error_message}, status=response.status_code)
