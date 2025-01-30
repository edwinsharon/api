from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

@api_view(['POST'])  # Only allow POST requests
def add_todo(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    



@api_view(['GET'])  # Only allow GET requests
def get_todos(request):
    if request.method == 'GET':
        # Get all todos from the database
        todos = Todo.objects.all()
        
        # Serialize the queryset
        serializer = TodoSerializer(todos, many=True)
        
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    
    
@api_view(['DELETE'])  # Only allow DELETE requests
def delete_todo(request, id):
    try:
        # Get the todo item by primary key
        todo = Todo.objects.get(pk=id)
        
        # Delete the todo item
        todo.delete()
        
        # Return success message
        return Response(
            {'message': 'Todo deleted successfully'}, 
            status=status.HTTP_204_NO_CONTENT
        )
        
    except Todo.DoesNotExist:
        return Response(
            {'error': 'Todo not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )                                                            