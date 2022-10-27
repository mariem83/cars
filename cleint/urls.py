from django.urls import path
from cleint.views import index,get_car,get_cleint,get_company

urlpatterns = [
path ('car/',get_car),
path ('cleint/',get_cleint),
path ('company/',get_company)
]
# http://127.0.0.1:8000/cleint/