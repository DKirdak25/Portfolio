from django.test import TestCase
from django.urls import reverse, resolve

# Import your class-based views
from .views import (
    HomeView,
    AboutView,
    EducationView,
    ExperienceView,
    ProjectView,
    ContactView,
)


class PortfolioPagesTests(TestCase):
    """Test all static pages of the portfolio website."""

    def setUp(self):
        # Define pages, their URL names, templates, and view classes
        self.pages = [
            {
                "name": "home",
                "template": "home.html",
                "view": HomeView,
            },
            {
                "name": "about",
                "template": "about.html",
                "view": AboutView,
            },
            {
                "name": "education",
                "template": "education.html",
                "view": EducationView,
            },
            {
                "name": "experience",
                "template": "experience.html",
                "view": ExperienceView,
            },
            {
                "name": "project",
                "template": "project.html",
                "view": ProjectView,
            },
            {
                "name": "contact",
                "template": "contact.html",
                "view": ContactView,
            },
        ]

    def test_all_pages_status_code_200(self):
        """Each page should return HTTP 200 OK"""
        for page in self.pages:
            with self.subTest(page=page["name"]):
                response = self.client.get(reverse(page["name"]))
                self.assertEqual(response.status_code, 200)

    def test_all_pages_use_correct_template(self):
        """Each page should use its correct HTML template"""
        for page in self.pages:
            with self.subTest(page=page["name"]):
                response = self.client.get(reverse(page["name"]))
                self.assertTemplateUsed(response, page["template"])

    def test_all_urls_resolve_to_correct_view(self):
        """Each URL name should map to the correct view class"""
        for page in self.pages:
            with self.subTest(page=page["name"]):
                resolver = resolve(reverse(page["name"]))
                self.assertEqual(resolver.func.view_class, page["view"])

    def test_base_template_included(self):
        """base.html should be used in all templates"""
        for page in self.pages:
            with self.subTest(page=page["name"]):
                response = self.client.get(reverse(page["name"]))
                self.assertTemplateUsed(response, "base.html")
