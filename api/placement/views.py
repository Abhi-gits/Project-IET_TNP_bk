from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.placement.serializers import PlacementCreateSerializer, PlacementListSerializer, PlacementDetailSerializer, PlacementUpdateSerializer
from api.placement.models import Placement
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from api.account.permissions import IsOwnerOrReadOnly


# Create your views here.
class PlacementViewSet(viewsets.ModelViewSet):
    queryset = Placement.objects.all()
    serializer_class = PlacementCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at', 'is_approved']
    search_fields = ['user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at', 'is_approved']
    ordering_fields = ['user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at', 'is_approved']
    
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
    

