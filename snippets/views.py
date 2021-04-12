from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Snippet

from django.http import HttpResponse, JsonResponse
from .serializers import SnippetModelSerializer ,SnippetSerializer
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import qrcode
import io
import base64
import PIL.Image


from onfido.regions import Region
from onfido import Api

# ONFIDO_API_KEY = 'api_sandbox_us.ifJj_hVJhYs.Vnj1TrU2KD5ty6yhAyhXYv-TEzdMQjv1'


# # class ProfileList(APIView):
# #     renderer_classes = [TemplateHTMLRenderer]
# #     template_name = "profile_list.html"

# #     def get(self,request):
# #         queryset = Profile.objects.all()
# #         return Response({"profiles":queryset})

# # class ProfileDetail(APIView):r
# #     renderer_classes = [TemplateHTMLRenderer]
# #     template_name = 'profile_detail.html'

# #     def get(self, request, pk):
# #         profile = get_object_or_404(Profile, pk=pk)
# #         serializer = ProfileSerializer(profile)
# #         return Response({'serializer': serializer, 'profile': profile})

# #     def post(self, request, pk):
# #         profile = get_object_or_404(Profile, pk=pk)
# #         serializer = ProfileSerializer(profile, data=request.data)
# #         if not serializer.is_valid():
# #             return Response({'serializer': serializer, 'profile': profile})
# #         serializer.save()
# #         return redirect('profile-list')


# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         article = Snippet.objects.all()
#         print(article)
#         serializer = SnippetSerializer(article,many=True)
#         # print(serializer)
#         print(serializer.data)
#         return JsonResponse(serializer.data,safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = SnippetModelSerializer(data=data)
#         print(serializer)

#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

# @csrf_exempt
# def article_detail(request,pk):
#     try:
#         article = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(article,data=data)

#         if serializer.is_valid():
#             serializer.save()
#             # print(serializer.data)
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)


#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)



# def qrcode_demo(request):
#     invitation_url = "Shavej Shaikh"
#     stream = io.BytesIO()
#     qr_png = qrcode.make(invitation_url)
#     qr_png.save(stream, "PNG")
#     qr_png_b64 = base64.b64encode(stream.getvalue()).decode("utf-8")

#     return render(request,"qrcode.html",{"qrcode":qr_png_b64})


# def state(request):
#     print("state is heare ")
#     resp  = {"state":"Start","version":"1.0"}
#     return JsonResponse(resp)



# def onfido(request):
#     return render(request,"index.html")



# #Get JWT Token for initializing WEB_SDK_GUI
# def get_jwt_token(request):
#     api = Api(ONFIDO_API_KEY, base_url=Region.US)
#     all_applicants = api.applicant.all()
#     all_applicants_list = all_applicants.get('applicants')
#     applicant_id = None

#     for applicant in all_applicants_list:
#         if applicant['first_name'] == 'Test':
#             applicant_id = applicant['id']
#     if not applicant_id:
#         applicant_details = {
#             "first_name": "Test",
#             "last_name": "Demo",
#             }

#         applicant = api.applicant.create(applicant_details)
#         applicant_id = applicant.get('id')

#     print(applicant_id)
#     request_body = {"applicant_id": applicant_id, "referrer": "*://*/*"}
#     # request_body = {"applicant_id": applicant_id, 'referrer':'http://127.0.0.1:8000/onfido'}
#     jwt_token = api.sdk_token.generate(request_body)
#     print("JWT Token is :",jwt_token)
#     jwt_token.update({'applicant_id':applicant_id})
#     print("\n ",jwt_token)
#     return JsonResponse(jwt_token)


from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView



import onfido
# from onfido import DocumentType 
from onfido.regions import Region



from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse




ONFIDO_API_KEY = "api_sandbox_us.ifJj_hVJhYs.Vnj1TrU2KD5ty6yhAyhXYv-TEzdMQjv1"
api = onfido.Api(ONFIDO_API_KEY, base_url=Region.US)

def index(request):
    # api=onfido.Api("api_sandbox_us.ifJj_hVJhYs.Vnj1TrU2KD5ty6yhAyhXYv-TEzdMQjv1",base_url=Region.US)
    param={
        "first_name":"Rounak",
        "last_name":"Ghosh"
    }
    applicant_object=api.applicant.create(param)
    return render(request,'index.html',{'applicant_object':applicant_object})

def get_jwt_token(request):
    # api_key = "api_sandbox_us.ifJj_hVJhYs.Vnj1TrU2KD5ty6yhAyhXYv-TEzdMQjv1"
    # api = onfido.Api(api_key, base_url=Region.US)
    all_applicants = api.applicant.all()
    all_applicants_list = all_applicants.get('applicants')
    applicant_id = None
    for applicant in all_applicants_list:
        if applicant['first_name'] == 'Shavej':
            applicant_id = applicant['id']
    if not applicant_id:
        applicant_details = {
            "first_name": "Shavej",
            "last_name": "Shaikh",
            }

        applicant = api.applicant.create(applicant_details)
        applicant_id = applicant.get('id')

    print(applicant_id)
    request_body = {"applicant_id": applicant_id, "referrer": "*://*/*"}
    jwt_token = api.sdk_token.generate(request_body)
    jwt_token.update({'applicant_id':applicant_id})
    return JsonResponse(jwt_token)


def view_all_doc(request):
    all_app = api.applicant.all()
    return JsonResponse(all_app)


'''
{'id': '0937415e-b23d-4e09-8e84-87b2c67e77a2', 'created_at': '2021-01-21T10:03:11Z', 'status': 'in_progress',
 'redirect_uri': None, 'result': None, 'sandbox': True, 'tags': [], 
 'results_uri': 'https://dashboard.us.onfido.com/checks/0937415e-b23d-4e09-8e84-87b2c67e77a2', 
 'form_uri': None, 'paused': False, 'version': '3.0', 'report_ids': ['439d12a7-6f69-4620-9f08-12be0d1f78ce',
  '29082ddf-e838-40df-b3af-ff93cf84e1c1'], 'href': '/v3/checks/0937415e-b23d-4e09-8e84-87b2c67e77a2',
   'applicant_id': 'e32e716f-36c5-457d-bc79-b3454acbe7a8', 'applicant_provides_data': False}'''

def verifycheck(request,application_id):
    applicant_id = application_id
    request_body = {"applicant_id": applicant_id, "report_names": ["document", "facial_similarity_photo"]}
    response = api.check.create(request_body)
    # print("Verify-Check",response)
    # print("check Id",response['id'])
    return redirect("viewcheck",application_id = application_id)

def viewcheck(request,application_id):
    response = api.check.all(application_id)
    context = {"response":response,"application_id":application_id}
    return render(request,"checkreport.html",context)


def clearcheck(request,application_id):
    response = api.check.all(application_id)
    status   = response['checks'][0]['result']
    context  = {"response":response,"status":status}
    return JsonResponse(context)


def verifyreport(request,check_id):
    response= api.report.all(check_id)
    print("report is :",response)
    result  = response['reports'][0]['result']

    doc  = response['reports'][1]['properties']

    context = {"response":response,
                "result":result,
                # "nationality":doc['nationality'],
                "doc_type":doc['document_type'],
                "date_of_birth":doc['date_of_birth'],
                "date_of_exp":doc['date_of_expiry'],
                "doc_no":doc['document_numbers'][0]['value'],
                "issuing_country":doc['issuing_country']}

    return JsonResponse(context)

# 81321b78-9715-4218-bc5a-6f3cf28a45c2', 
# 'id': '81321b78-9715-4218-bc5a-6f3cf28a45c2'
def detail_all_doc(request):
    # applicant_id = "a11ed3d1-9fda-4bed-a845-b0e881b65dbc"
    my_doc_type  = api.report.find('81321b78-9715-4218-bc5a-6f3cf28a45c2')
    print("Check ID is:",my_doc_type['check_id'])
    return JsonResponse(my_doc_type)

# def viewcheck(request):
#     # api.document.download("22035edd-0451-4246-a171-73e50e9e6826")  
#     response = api.check.all("a11ed3d1-9fda-4bed-a845-b0e881b65dbc")
#     return JsonResponse(response)
