from django.urls import path
from .views import *
urlpatterns = [
    path('',Dashboard.as_view(), name='dashboard'),
    path('writer/list', WriterListView.as_view(), name='writer-list'),
    path('writer/create',WriterCreateView.as_view(),name='writer-create'),
    path('writer/edit/<int:pk>',WriterEditView.as_view(),name='writer-edit'),
    path('writer/delete/<int:pk>',WriterDeleteView.as_view(),name='writer-delete'),
    path('writer/detail/<int:pk>', WriterDetailView.as_view(), name='writer-detail'),

    path('publication/list', PublicationListView.as_view(), name='publication-list'),
    path('publication/detail/<int:pk>', PublicationDetailView.as_view(), name='publication-detail'),
    path('publication/create', PublicationCreateView.as_view(), name='publication-create'),
    path('publication/edit/<int:pk>',PublicationEditView.as_view(),name='publication-edit'),
    path('publication/delete/<int:pk>', PublicationDeleteView.as_view(), name='publication-delete'),

    path('subject/list', SubjectListView.as_view(), name='subject-list')
]