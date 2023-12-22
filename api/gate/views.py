from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

import requests
import json

import os
from pyairtable import Api
from pyairtable.formulas import match


api = Api(os.environ.get("AIRTABLE_API_KEY"))
table = api.table(
    os.environ.get("IETAGRA_AIRTABLE_BASE_ID"),
    os.environ.get("GATE_AIRTABLE_TABLE"),
)
# Airtable API endpoint
BASE_URL = f"https://api.airtable.com/v0/{os.environ.get('IETAGRA_AIRTABLE_BASE_ID')}/{os.environ.get('GATE_AIRTABLE_TABLE')}"
# Create your views here.


@api_view(["GET"])
def GateListAll(request):
    fields = [
        "roll_number",
        "student_name",
        "student_branch",
        "student_batch",
        "registration_no",
        "rank",
        "student_photo",
        "score_card",
        "status"
    ]
    records = table.all(fields=fields)
    return Response(records)


@api_view(["GET"])
def GateListApproved(request):
    formula = match({"status": "Approved"})
    fields = [
        "roll_number",
        "student_name",
        "student_branch",
        "student_batch",
        "registration_no",
        "rank",
        "student_photo",
        "score_card",
        "status"
    ]
    records = table.all(formula=formula, fields=fields)
    return Response(records)


class GateDetail(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="record_id",
                type=OpenApiTypes.STR,
            ),
        ],
        responses={
            status.HTTP_200_OK: OpenApiTypes.OBJECT,
            status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT,
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
            return Response(
                json.loads(response.text).get("fields", {}), status=status.HTTP_200_OK
            )
        else:
            # If unsuccessful, return the error details
            error_message = (
                json.loads(response.text)
                .get("error", {})
                .get("message", "Unknown error")
            )
            return Response({"error": error_message}, status=response.status_code)


class GateCreate(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="roll_number",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="student_name",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="student_branch",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="student_batch",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="registration_no",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="rank",
                type=OpenApiTypes.INT,
            ),
            OpenApiParameter(
                name="student_photo",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="score_card",
                type=OpenApiTypes.STR,
            )
        ],
        request=OpenApiTypes.OBJECT,
        responses={
            status.HTTP_201_CREATED: OpenApiTypes.OBJECT,
            status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                name="Student Gate Record",
                value={
                    "roll_number": "123456",
                    "student_name": "John Doe",
                    "student_branch": "Computer Science & Engineering",
                    "student_batch": ["recNwNXEQpYWCqWIm"],
                    "registration_no": "123456",
                    "rank": "1",
                    "student_photo": "attachment",
                    "score_card": "attachment",
                },
                request_only=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        base_url = BASE_URL

        # Airtable API headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json",
        }

        # check if request has a data or not
        if not request.data:
            return Response(
                {"error": "Please provide the data to create a record"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Data to be sent to Airtable API
        data = {
            "records": [
                {
                    "fields": {
                        "roll_number": request.data.get("roll_number"),
                        "student_name": request.data.get("student_name"),
                        "student_branch": request.data.get("student_branch"),
                        "student_batch": request.data.get("student_batch"),
                        "registration_no": request.data.get("registration_no"),
                        "rank": request.data.get("rank"),
                        "student_photo": request.data.get("student_photo"),
                        "score_card": request.data.get("score_card"),
                    }
                },
            ]
        }

        # Send POST request to Airtable API
        response = requests.post(base_url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == status.HTTP_200_OK:
            return Response(
                {"message": "Record created successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            # If unsuccessful, return the error details
            error_message = (
                json.loads(response.text)
                .get("error", {})
                .get("message", "Unknown error")
            )
            return Response({"error": error_message}, status=response.status_code)


class GateUpdate(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="record_id",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="roll_number",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="student_name",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="student_branch",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="student_batch",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="registration_no",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="rank",
                type=OpenApiTypes.INT,
            ),
            OpenApiParameter(
                name="student_photo",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="score_card",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="status",
                type=OpenApiTypes.STR,
            )
        ],
        request=OpenApiTypes.OBJECT,
        responses={
            status.HTTP_200_OK: OpenApiTypes.OBJECT,
            status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                name="Student Gate Record",
                value={
                    "roll_number": "123456",
                    "student_name": "John Doe",
                    "student_branch": "Computer Science & Engineering",
                    "student_batch": ["recNwNXEQpYWCqWIm"],
                    "registration_no": "123456",
                    "rank": "1",
                    "student_photo": "attachment",
                    "score_card": "attachment",
                    "status": "Approved"
                },
                request_only=True,
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        record_id = kwargs.get("record_id")
        base_url = f"{BASE_URL}/{record_id}"

        # Airtable API headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json",
        }

        # check if request has a data or not
        if not request.data:
            return Response(
                {"error": "Please provide the data to update the record"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Data to be sent to Airtable API
        data = {
            "fields": {
                "roll_number": request.data.get("roll_number"),
                "student_name": request.data.get("student_name"),
                "student_branch": request.data.get("student_branch"),
                "student_batch": request.data.get("student_batch"),
                "registration_no": request.data.get("registration_no"),
                "rank": request.data.get("rank"),
                "student_photo": request.data.get("student_photo"),
                "score_card": request.data.get("score_card"),
                "status": request.data.get("status")
            }
        }

        print(data)
        # Send PATCH request to Airtable API
        response = requests.patch(base_url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == status.HTTP_200_OK:
            return Response(
                {"message": "Record updated successfully"}, status=status.HTTP_200_OK
            )
        else:
            try:
                # Try to parse the response as JSON
                error_message = (
                    json.loads(response.text)
                    .get("error", {})
                    .get("message", "Unknown error")
                )
            except (json.JSONDecodeError, AttributeError):
                # If parsing fails, use the entire response as the error message
                error_message = response.text

            return Response({"error": error_message}, status=response.status_code)


class GateDelete(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="record_id",
                type=OpenApiTypes.STR,
            ),
        ],
        responses={
            status.HTTP_200_OK: OpenApiTypes.OBJECT,
            status.HTTP_400_BAD_REQUEST: OpenApiTypes.OBJECT,
        },
    )
    def delete(self, request, record_id, *args, **kwargs):
        base_url = f"{BASE_URL}/{record_id}"

        # Airtable API headers
        headers = {
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
        }

        # Send DELETE request to Airtable API
        response = requests.delete(base_url, headers=headers)

        # Check if the request was successful
        if response.status_code == status.HTTP_200_OK:
            return Response(
                {"message": "Record deleted successfully"}, status=status.HTTP_200_OK
            )
        else:
            # If unsuccessful, return the error details
            error_message = (
                json.loads(response.text)
                .get("error", {})
                .get("message", "Unknown error")
            )
            return Response({"error": error_message}, status=response.status_code)
