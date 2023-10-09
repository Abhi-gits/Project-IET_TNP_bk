from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.tnp.serializers import PlacementCreateSerializer, PlacementListSerializer, PlacementDetailSerializer, PlacementUpdateSerializer, CoursesCreateSerializer, CoursesListSerializer, CoursesDetailSerializer, CoursesUpdateSerializer
from api.tnp.models import Placement, Courses
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from api.account.permissions import IsOwnerOrReadOnly


# Create your views here.
class PlacementViewSet(viewsets.ModelViewSet):
    queryset = Placement.objects.all()
    serializer_class = PlacementCreateSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'name', 'company_name', 'company_email', 'company_website', 'company_salary',  'created_at', 'updated_at', 'is_approved']
    search_fields = ['user', 'name', 'company_name', 'company_email', 'company_website', 'company_salary', 'created_at', 'updated_at', 'is_approved']
    ordering_fields = ['user', 'name', 'company_name', 'company_email', 'company_website', 'company_salary', 'created_at', 'updated_at', 'is_approved']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PlacementListSerializer
        elif self.action == 'create':
            return PlacementCreateSerializer
        elif self.action == 'update':
            return PlacementUpdateSerializer
        return PlacementDetailSerializer

    def get_queryset(self):
        return Placement.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [IsOwnerOrReadOnly()]
        return []

    @action(detail=False, methods=['GET'])
    def get_my_placements(self, request):
        user = request.user
        placements = Placement.objects.filter(user=user)
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_approved_placements(self, request):
        placements = Placement.objects.filter(is_approved=True)
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_unapproved_placements(self, request):
        placements = Placement.objects.filter(is_approved=False)
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_latest_placements(self, request):
        placements = Placement.objects.all().order_by('-created_at')[:5]
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_approved_latest_placements(self, request):
        placements = Placement.objects.filter(is_approved=True).order_by('-created_at')[:5]
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_unapproved_latest_placements(self, request):
        placements = Placement.objects.filter(is_approved=False).order_by('-created_at')[:5]
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Class for listing authenticated users Placement details
class PlacementListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        placements = Placement.objects.filter(user=request.user)
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Class for listing all the Placement without user approval
class PlacementListAllAPIView(APIView):
    def get(self, request, format=None):
        placements = Placement.objects.filter(is_approved=True)
        serializer = PlacementListSerializer(placements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'created_at', 'updated_at', 'is_approved']
    search_fields = ['user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'created_at', 'updated_at', 'is_approved']
    ordering_fields = ['user', 'course_name', 'course_description', 'course_duration', 'course_fee', 'created_at', 'updated_at', 'is_approved']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CoursesListSerializer
        elif self.action == 'create':
            return CoursesCreateSerializer
        elif self.action == 'update':
            return CoursesUpdateSerializer
        return CoursesDetailSerializer

    def get_queryset(self):
        return Courses.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [IsOwnerOrReadOnly()]
        return []

    @action(detail=False, methods=['GET'])
    def get_my_courses(self, request):
        user = request.user
        courses = Courses.objects.filter(user=user)
        serializer = CoursesListSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_approved_courses(self, request):
        courses = Courses.objects.filter(is_approved=True)
        serializer = CoursesListSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_unapproved_courses(self, request):
        courses = Courses.objects.filter(is_approved=False)
        serializer = CoursesListSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CoursesListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        courses = Courses.objects.filter(user=request.user)
        serializer = CoursesListSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CoursesListAllAPIView(APIView):
    def get(self, request, format=None):
        courses = Courses.objects.filter(is_approved=True)
        serializer = CoursesListSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    