from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from .models import Placement, Courses, Batch
from .serializers import PlacementSerializer, CoursesSerializer, BatchSerializer


@api_view(['GET'])
def PlacementAPIOverview(request):
    api_urls = {
        'List': '/placement-list/',
        'Detail View': '/placement-detail/<str:pk>/',
        'Create': '/placement-create/',
        'Update': '/placement-update/<str:pk>/',
        'Delete': '/placement-delete/<str:pk>/',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def CoursesAPIOverview(request):
    api_urls = {
        'List': '/courses-list/',
        'Detail View': '/courses-detail/<str:pk>/',
        'Create': '/courses-create/',
        'Update': '/courses-update/<str:pk>/',
        'Delete': '/courses-delete/<str:pk>/',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def PlacementList(request):
    placements = Placement.objects.all()
    placement_serializer = PlacementSerializer(placements, many=True)
    return Response(placement_serializer.data)


@api_view(['POST'])
def PlacementCreate(request):
    placement_item = PlacementSerializer(data=request.data)
    
    if item.objects.filter(**request.data).exists():
        return Response({'message': 'Placement already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if placement_item.is_valid():
        placement_item.save()
        return Response(placement_item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(placement_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def PlacementDetail(request, pk):
    try:
        placement_item = Placement.objects.get(pk=pk)
    except Placement.DoesNotExist:
        return Response({'message': 'Placement does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    placement_serializer = PlacementSerializer(placement_item)
    return Response(placement_serializer.data)


@api_view(['POST'])
def PlacementUpdate(request, pk):
    try:
        placement_item = Placement.objects.get(pk=pk)
        placement_data = PlacementSerializer(placement_item, data=request.data)
    except Placement.DoesNotExist:
        return Response({'message': 'Placement does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if placement_data.is_valid():
        placement_data.save()
        return Response(placement_data.data)
    
    return Response(placement_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def PlacementDelete(request, pk):
    try:
        placement_item = Placement.objects.get(pk=pk)
        placement_data = PlacementSerializer(placement_item, data=request.data)
    except Placement.DoesNotExist:
        return Response({'message': 'Placement does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    placement_item.delete()
    return Response({'message': 'Placement deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def CoursesList(request):
    courses = Courses.objects.all()
    courses_serializer = CoursesSerializer(courses, many=True)
    return Response(courses_serializer.data)


@api_view(['POST'])
def CoursesCreate(request):
    courses_item = CoursesSerializer(data=request.data)
    
    if item.objects.filter(**request.data).exists():
        return Response({'message': 'Courses already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if courses_item.is_valid():
        courses_item.save()
        return Response(courses_item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(courses_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def CoursesDetail(request, pk):
    try:
        courses_item = Courses.objects.get(pk=pk)
    except Courses.DoesNotExist:
        return Response({'message': 'Courses does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    courses_serializer = CoursesSerializer(courses_item)
    return Response(courses_serializer.data)


@api_view(['POST'])
def CoursesUpdate(request, pk):
    try:
        courses_item = Courses.objects.get(pk=pk)
        courses_data = CoursesSerializer(courses_item, data=request.data)
    except Courses.DoesNotExist:
        return Response({'message': 'Courses does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if courses_data.is_valid():
        courses_data.save()
        return Response(courses_data.data)
    
    return Response(courses_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def CoursesDelete(request, pk):
    try:
        courses_item = Courses.objects.get(pk=pk)
        courses_data = CoursesSerializer(courses_item, data=request.data)
    except Courses.DoesNotExist:
        return Response({'message': 'Courses does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    courses_item.delete()
    return Response({'message': 'Courses deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




    