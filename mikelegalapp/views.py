from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subscriber

# Create your views here.


@api_view(['POST'])
def add_subscriber(request):
    email = request.data.get('email')
    first_name = request.data.get('first_name')

    if not email or not first_name:
        return Response({'error': 'Email and first_name are required.'}, status=status.HTTP_400_BAD_REQUEST)

    subscriber, created = Subscriber.objects.get_or_create(email=email)
    subscriber.first_name = first_name
    subscriber.is_active = True
    subscriber.save()

    return Response({'message': 'Subscriber added successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unsubscribe(request):
	email = request.data.get('email')
	subscriber = get_object_or_404(Subscriber, email=email)
	subscriber.is_active = False
	subscriber.save()

	return Response({'message': 'Subscriber unsubscribed successfully.'})
