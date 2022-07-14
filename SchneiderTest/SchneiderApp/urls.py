from django.urls import path
from django.views.generic import TemplateView

from .views import upload_file


urlpatterns = [
    path('', upload_file, name='files' ),
    path('task/', TemplateView.as_view(template_name="task.html",
                                  extra_context={"header": "О сайте"})),
]