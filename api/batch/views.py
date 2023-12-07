from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

import requests
import json

import os
from pyairtable import Api
from pyairtable.formulas import match


api = Api(os.environ.get('AIRTABLE_API_KEY'))
table = api.table(os.environ.get('IETAGRA_AIRTABLE_BASE_ID'), os.environ.get('BATCH_AIRTABLE_TABLE'))

# Airtable API endpoint
BASE_URL = f"https://api.airtable.com/v0/{os.environ.get('IETAGRA_AIRTABLE_BASE_ID')}/{os.environ.get('PLACEMENT_AIRTABLE_TABLE')}"
# Create your views here.

@api_view(["GET"])
def BatchListAll(request):
    fields = [
        'batch',
        'Placements',
    ]
    records = table.all(fields=fields)
    return Response(records)


class BatchDetail(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="batch",
                description="Batch name",
                required=True,
                type=OpenApiTypes.STR,
                examples=[
                    OpenApiExample(
                        "2020-2024",
                        summary="Difference should be 4 years",
                        value="2020-2024"
                    ),
                ]
            ),
        ],
        request=OpenApiTypes.OBJECT,
        responses={
            status.HTTP_200_OK: OpenApiTypes.OBJECT,
            status.HTTP_404_NOT_FOUND: OpenApiTypes.OBJECT,
        },
    )

    def get(self, request, record_id, *args, **kwargs):
        base_url = f"{BASE_URL}/{record_id}"
        
        # Airtable API headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
        }
        
        # Send GET request to Airtable API
        response = requests.get(base_url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == status.HTTP_200_OK:
            return Response(json.loads(response.text).get("fields", {}), status=status.HTTP_200_OK)
        else:
            # If unsuccessful, return the error details
            error_message = json.loads(response.text).get("error", {}).get("message", "Unknown error")
            return Response({"error": error_message}, status=response.status_code)



class BatchCreate(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="batch",
                description="Batch name",
                required=True,
                type=OpenApiTypes.STR,
                examples=[
                    OpenApiExample(
                        "2020-2024",
                        summary="Difference should be 4 years",
                        value="2020-2024"
                    ),
                ]
            ),
        ],
        request=OpenApiTypes.OBJECT,
        responses={
            status.HTTP_201_CREATED: OpenApiTypes.OBJECT,
            status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT,
        },
    )

    def post(self, request, *args, **kwargs):
        base_url = BASE_URL
        
        # Airtable Headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        # Data to be sent to Airtable
        data = {
            "records": [
                {
                    "fields": {
                        "batch": request.data.get('batch'),
                    }
                }
            ]
        }
        
        # Send POST request to Airtable
        response = requests.post(base_url, headers=headers, json=data)
        
        # Check if request was successful
        if response.status.code == status.HTTP_200_OK:
            return Response({"message": "Batch created successfully"}, status=status.HTTP_200_OK)
        else:
            # if unsuccessful, return error message
            error_message = json.loads(response.text).get('error', {}).get('message', 'Unknown error')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
        
        
class BatchUpdate(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="batch",
                description="Batch name",
                required=True,
                type=OpenApiTypes.STR,
                examples=[
                    OpenApiExample(
                        "2020-2024",
                        summary="Difference should be 4 years",
                        value="2020-2024"
                    ),
                ]
            ),
        ],
        request=OpenApiTypes.OBJECT,
        responses={
            status.HTTP_200_OK: OpenApiTypes.OBJECT,
            status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT,
        },
    )

    def patch(self, request, record_id, *args, **kwargs):
        base_url = f"{BASE_URL}/{record_id}"
        
        # Airtable Headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        # Data to be sent to Airtable
        data = {
            "records": [
                {
                    "id": record_id,
                    "fields": {
                        "batch": request.data.get('batch'),
                    }
                }
            ]
        }
        
        # Send PATCH request to Airtable
        response = requests.patch(base_url, headers=headers, json=data)
        
        # Check if request was successful
        if response.status.code == status.HTTP_200_OK:
            return Response({"message": "Batch updated successfully"}, status=status.HTTP_200_OK)
        else:
            # if unsuccessful, return error message
            error_message = json.loads(response.text).get('error', {}).get('message', 'Unknown error')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class BatchDelete(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="batch",
                description="Batch name",
                required=True,
                type=OpenApiTypes.STR,
                examples=[
                    OpenApiExample(
                        "2020-2024",
                        summary="Difference should be 4 years",
                        value="2020-2024"
                    ),
                ]
            ),
        ],
        request=OpenApiTypes.OBJECT,
        responses={
            status.HTTP_200_OK: OpenApiTypes.OBJECT,
            status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT,
        },
    )

    def delete(self, request, record_id, *args, **kwargs):
        base_url = f"{BASE_URL}/{record_id}"
        
        # Airtable Headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        # Send DELETE request to Airtable
        response = requests.delete(base_url, headers=headers)
        
        # Check if request was successful
        if response.status.code == status.HTTP_200_OK:
            return Response({"message": "Batch deleted successfully"}, status=status.HTTP_200_OK)
        else:
            # if unsuccessful, return error message
            error_message = json.loads(response.text).get('error', {}).get('message', 'Unknown error')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
        