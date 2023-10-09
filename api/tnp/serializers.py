from rest_framework import serializers
from api.account.models import User
from api.tnp.models import Placement, Courses



class PlacementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'name', 'company_name', 'company_email', 'company_website', 'company_salary', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validate_data):
        return Placement.objects.create(**validate_data)
    
class PlacementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'name', 'company_name', 'company_email', 'company_website', 'company_salary', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class PlacementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'name', 'company_name', 'company_email', 'company_website', 'company_salary', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class PlacementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'user', 'name', 'company_name', 'company_email', 'company_website', 'company_salary', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.company_name = validate_data.get('company_name', instance.company_name)
        instance.company_email = validate_data.get('company_email', instance.company_email)
        instance.company_website = validate_data.get('company_website', instance.company_website)
        instance.company_salary = validate_data.get('company_salary', instance.company_salary)
        instance.is_approved = validate_data.get('is_approved', instance.is_approved)
        instance.save()
        return instance
    

class CoursesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'name', 'course_name', 'course_description', 'course_duration', 'course_fee', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validate_data):
        return Courses.objects.create(**validate_data)
    
class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class CoursesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class CoursesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'created_at', 'updated_at', 'is_approved']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def update(self, instance, validate_data):
        instance.course_name = validate_data.get('course_name', instance.course_name)
        instance.course_description = validate_data.get('course_description', instance.course_description)
        instance.course_duration = validate_data.get('course_duration', instance.course_duration)
        instance.course_fee = validate_data.get('course_fee', instance.course_fee)
        instance.is_approved = validate_data.get('is_approved', instance.is_approved)
        instance.save()
        return instance
    