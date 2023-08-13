from rest_framework import serializers
from api.account.models import User
from api.tnp.models import Placement, Courses



class PlacementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validate_data):
        return Placement.objects.create(**validate_data)
    
class PlacementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class PlacementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class PlacementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def update(self, instance, validate_data):
        instance.company_name = validate_data.get('company_name', instance.company_name)
        instance.company_email = validate_data.get('company_email', instance.company_email)
        instance.company_website = validate_data.get('company_website', instance.company_website)
        instance.company_address = validate_data.get('company_address', instance.company_address)
        instance.company_phone = validate_data.get('company_phone', instance.company_phone)
        instance.company_salary = validate_data.get('company_salary', instance.company_salary)
        instance.company_location = validate_data.get('company_location', instance.company_location)
        instance.company_category = validate_data.get('company_category', instance.company_category)
        instance.company_status = validate_data.get('company_status', instance.company_status)
        instance.is_approved = validate_data.get('is_approved', instance.is_approved)
        instance.save()
        return instance
    

class CoursesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'course_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validate_data):
        return Courses.objects.create(**validate_data)
    
class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'course_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class CoursesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'course_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class CoursesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'course_status', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def update(self, instance, validate_data):
        instance.course_name = validate_data.get('course_name', instance.course_name)
        instance.course_description = validate_data.get('course_description', instance.course_description)
        instance.course_duration = validate_data.get('course_duration', instance.course_duration)
        instance.course_fee = validate_data.get('course_fee', instance.course_fee)
        instance.course_status = validate_data.get('course_status', instance.course_status)
        instance.is_approved = validate_data.get('is_approved', instance.is_approved)
        instance.save()
        return instance
    