from django.views.generic import TemplateView

class HomeView(TemplateView):
				template_name = "home.html"
				
class AboutView(TemplateView):
				template_name = "about.html"
				
class EducationView(TemplateView):
				template_name = "education.html"		
				
class ProjectView(TemplateView):
				template_name = "project.html"

class ContactView(TemplateView):
				template_name = "contact.html"


