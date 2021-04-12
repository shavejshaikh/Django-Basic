from django.contrib import admin
from django.urls import path,include
from . import views


#Need to remove unused Urls
urlpatterns = [
    path('index',views.index,name="default_page"),
    path('jwt_token',views.get_jwt_token, name = "get_jwt_token"),
    path('viewsall',views.view_all_doc, name = "view_all_doc"),
    path("detailview",views.detail_all_doc,name = "detail_all_doc"),
    # path("viewcheck",views.viewcheck,name="viewcheck"),

    path("verifycheck/<str:application_id>/",views.verifycheck,name = "verifycheck"),
    path("viewcheck/<str:application_id>/",views.viewcheck,name="viewcheck"),
    path("clearcheck/<str:application_id>/",views.clearcheck,name="clearcheck"),


    path("verifyreport/<str:check_id>",views.verifyreport,name="verifyreport"),

#     path('state/<str:connection_id>/',views.index),
#     path('create-applicant/',views.CreateOnfidoUser.as_view()),
#     path('webhook/',views.create_webhook,name="webhook"),
#     path('create-applicant/',views.checkapplicant),
#     path('v3/applicants/<str:application_id>',views.applicants)
]

