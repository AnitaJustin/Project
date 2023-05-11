from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage, name="homepage"),
    path('next_page/', views.nextpage, name="next_page"),
    path('levels/',views.levels,name="levels"),
    path('info_page/',views.info_page,name="info_page"),
    path('questions/',views.questions,name="questions")

]