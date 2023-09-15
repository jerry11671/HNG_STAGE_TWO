from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
from .serializers import PersonSerializer
from .models import Person

class UserGetCreate(APIView):
    # Create
    def post(self, request):
        if request.method == 'POST':
            serializer = PersonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors)
            
            return Response(serializer.data, status=HTTP_201_CREATED)

    # Read 
    def get(self, request, pk):
        try:
            person_detail = Person.objects.get(id=pk)
        except:
            return Response({"error": "There is no information for this person!!"}, status=HTTP_400_BAD_REQUEST)
        
        serializer = PersonSerializer(person_detail)
        return Response(serializer.data, status=HTTP_200_OK)
    
    
    # Update
    def put(self, request, pk):
        # Get the instance of the user
        person_instance = Person.objects.get(id=pk)

        # Get the updated data
        data = {
            'name': request.data.get('name'),
            'track': request.data.get('track'),
            'stage': request.data.get('stage')
        }

        # Create the serializer for the person object
        serializer = PersonSerializer(instance=person_instance, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data, status=HTTP_200_OK)

    
    # Delete
    def delete(self, request, pk):
        person_instance = Person.objects.get(id=pk)

        if not person_instance:
            return Response({"error":"This person's instance does not exist!!"})
        
        person_instance.delete()
        return Response({"Person Object Deleted!"}, status=HTTP_200_OK)
            
    

