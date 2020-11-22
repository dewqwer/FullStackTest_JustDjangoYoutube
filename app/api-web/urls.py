# from django.urls import path, include

# from .views import (MajorCreateView,
#                     MajorDeleteView,
#                     MajorDetailView,
#                     MajorListView,
#                     MajorUpdateView,
#                     )
# from .views import index

# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [
#     path('', index, name="index"),


#     path('api-web/Major/', MajorListView.as_view(), name='list'),
#     path('Major/<pk>', MajorDetailView.as_view()),
#     path('Major/add/', MajorCreateView.as_view()),
#     path('Major/<pk>/update/', MajorUpdateView.as_view()),
#     path('Major/<pk>/delete/', MajorDeleteView.as_view()),


# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
