from django.urls import path
from . import views

urlpatterns = [
    path('start-session/', views.start_session, name='start_session'),
    path('stop-session/', views.stop_session, name='stop_session'),
    path('control/', views.session_control_page, name='session_control'),
    path('final-submit/', views.final_submit_attendance, name='final_submit_attendance'),
]
