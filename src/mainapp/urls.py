from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("catalog/", views.CatalogPageView.as_view(), name="catalog"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("in_progress/", views.InProgressPageView.as_view(), name="in_progress"),
    path("course1/", views.Course1PageView.as_view(), name="course1"),
    path("lesson1_1/", views.Lesson1_1PageView.as_view(), name="lesson1_1"),
    path("courses_category/", views.Courses_categoryPageView.as_view(), name="courses_category"),
]
