from django.http import JsonResponse
from .models import MyInfo
from .serializers import InfoSerializer

def info(request):
    
    # get all the drinks
    # serialize dem 
    # return json
    info = MyInfo.objects.all()
    serializer = InfoSerializer(info, many=True) #true meaning it will serialize all of dem coz we ve a list
    return JsonResponse(serializer.data[0], safe=False) # false inorder to allow non-dict objects to be serialized
