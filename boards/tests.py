from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home, project
from .models import Project
# Create your tests here.

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('project', kwargs={'pk': self.project.pk})
        self.assertContains(self.response, 'href="{0}"'.format(project_url))

class ProjectTests(TestCase):
    def setUp(self):
        Project.objects.create(name='Django', description='Django board.')

    def test_project_view_success_status_code(self):
        url = reverse('project', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_project_view_not_found_status_code(self):
        url = reverse('project', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_project_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, project)
