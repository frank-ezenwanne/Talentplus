from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company
from .serializers import PostCompanySerializer

class GetCompanyName(APIView): #This fetches Talent Plus
    def get(self,request,*args,**kwargs):
        company = Company.objects.get(email='talentplus@gmail.com')
        return Response({'company_name':company.name}) #returns JSON data

class PostCompanyName(APIView):
    def post(self,request,*args,**kwargs):
        serializer = PostCompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status':'saved'})

class ListUrlsView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({
            'Fetch TALENT PLUS from stored record in sqlite': 'api/get_company_name',
            'Create company with name and email':'api/create_company'
            
        })
