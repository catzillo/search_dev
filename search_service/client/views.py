from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SearchQuerySerializer


@api_view(['POST'])
def search_view(request):
    serializer = SearchQuerySerializer(data=request.data)
    if serializer.is_valid():
        return Response({
            "results": [],
            "status": "succes"
        })
    return Response(serializer.errors, status=400)


