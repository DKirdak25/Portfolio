from django.urls import path
from .views import HomeView,AboutView,EducationView,ExperienceView,ProjectView,ContactView

urlpatterns = [
     path('', HomeView.as_view(), name="home"),
     path('about/', AboutView.as_view(), name="about"),
     path('education/', EducationView.as_view(), name="education"),
     path('experience/', ExperienceView.as_view(), name="experience"),
     path('project/', ProjectView.as_view(), name="project"),
     path('contact/', ContactView.as_view(), name="contact"),
]




