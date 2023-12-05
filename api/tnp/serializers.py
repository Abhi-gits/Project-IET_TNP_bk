from rest_framework import serializers
from api.account.models import User
from api.tnp.models import Placement, Courses, Batch


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = (
            "id",
            "user",
            "student_name",
            "student_branch",
            "student_roll_no",
            "student_batch",
            "company_name",
            "student_salary",
            "position_offered",
            "company_offer_letter",
            "remarks",
            "status",
        )


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            "id",
            "user",
            "student_name",
            "student_branch",
            "student_roll_no",
            "student_batch",
            "course_name",
            "course_description",
            "course_duration",
            "course_certificate",
            "course_fee",
            "status",
        )


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ("id", "starting_year", "ending_year")
