from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .repositories import add_investor, delete_investor, update_investor, get_investors, get_investor_by_id, generate_new_id
from .Serializers import InvestorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class InvestorPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_investor(request):
    serializer = InvestorSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        # Generate a new ID
        new_id = generate_new_id()
        # Add the new ID to the data
        data['id'] = new_id
        # Save the investor with the generated ID
        add_investor(data)
        # Re-serialize the data to include the ID field
        response_serializer = InvestorSerializer(data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_investor_view(request, id):
    if get_investor_by_id(id):
        delete_investor(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_investor_view(request, id):
    serializer = InvestorSerializer(data=request.data)
    if serializer.is_valid():
        updated_investor = serializer.validated_data
        if get_investor_by_id(id):
            update_investor(id, updated_investor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_investors(request):
    paginator = InvestorPagination()
    investors = get_investors()
    paginated_investors = paginator.paginate_queryset(investors, request)
    serializer = InvestorSerializer(paginated_investors, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_investor_by_id_view(request, id):
    investor = get_investor_by_id(id)
    if investor:
        serializer = InvestorSerializer(investor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
