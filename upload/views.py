from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from upload.models import Media
from rest_framework.decorators import api_view
from upload.serializer import MediaSerializer

@api_view(['GET'])
def list_arquivos(request):
    #nome = request.query_params.get('nome', None)

    if request.method == 'GET':
        query = Media.objects.all()
        
        media_serializer = MediaSerializer(query, many=True)
     
        return JsonResponse(media_serializer.data, safe=False)