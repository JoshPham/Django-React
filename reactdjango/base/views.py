from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializer import * 

class ReactView(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ReactSerializer
    def get(self, request):
        output = [{"question": output.question, 
                   "answer": output.answer}
                  for output in Problem.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)