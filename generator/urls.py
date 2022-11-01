from django.urls import path, include

from generator.views import password_home, liste_pass_generate, delete_record, recherche

urlpatterns = [
    path('', password_home, name="password_home"),
    path('coffre-fort/', liste_pass_generate, name="listall"),
    path('delete/<int:id>', delete_record, name="deleterecord"),
    path('search', recherche, name="search"),
]
