from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters

from profiles_api import serializers

class HelloApiView(APIView):

  """Test API View"""
  serializer_class = serializers.HelloSerializer
  def get(self, request,format=None):
    """return a list of APIview features """
    an_apiview=[
      'uses HTTP methods  as function (get ,post,patch,delete,put)',
      'Is similar to atraditional djangoGview '
      'Gives you the most control over you application logic  ',
      'is mapped mannauly to urls',

    ]
    return Response({'message':'hello','an_apiview': an_apiview})

  def post(self, request):
    """Create a hello message with our name"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}!'
      return Response({'message': message})
    else:
      return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
      )
  #serializer=self.serrializer_class(serial)
  
  def put(self, request, pk=None):
    """Handle updating an object"""

    return Response({'method': 'PUT'})

  def patch(self, request, pk=None):
    """Handle partial update of object"""

    return Response({'method': 'PATCH'})

  def delete(self, request, pk=None):
    """Delete an object"""

    return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
  """Test Api ViewSets"""

  serializer_class = serializers.HelloSerializer

  def list(self, request):
    """Return a hello message"""
    a_viewset=[
      'uses actions (list,create,retrieve,update,partial_update)',
      'Automatically maps to urls using  routers ',
      'provides more functionality with less code '
    ]
    return Response({'message':'Hello!','a_viewset':a_viewset})

  def create(self, request):
    serializer=self.serializer_class(data=request.data)
    if serializer.is_valid():
      name=serializer.validated_data['name']
      message=f"Hello {name}! "
      return Response({"message":message}, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request,pk=None):
    """handle getting an object by ID"""
    return Response({'httpmethod':'GET'})

  def updtae(self, request,pk=None):
    """handle updating an object """
    return Response({'httpmethod':'PUT'})

  def partial_update(self, request, pk=None):
    """hANDLE UPDATING PART OF AN OBJECT"""
    return Response({'Httpmethod':'Patch'})

  def destroy(self, request, pk=None):
    """handle destroying an object"""
    return Response({'Httpmethod':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
  """Handle creating and updating prodile """
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes=(TokenAuthentication,)
  permission_classes=(permissions.UpdateOwnProfile,)
  filter_backends=(filters.SearchFilter,)
  search_fields=('name','email',)
  

