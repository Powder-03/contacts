from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from rest_framework import permissions
from .serializers import ContactSerializer

class ContactList(ListCreateAPIView):
    
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    """
    View to list and create contacts.
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    
    
class ContactDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    """
    View to retrieve, update or delete a contact.
    """
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)




