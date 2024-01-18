from django.urls import path
from .views import login_user, register_user, qanda, change, dashboard, signout, session,course,level,feedback,chart, rate, get_ratings_count
from .import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register),
    path('session/', session, name="session"),
    path('editView/<question>', views.editView),
    path('chart/', chart, name='chart'),
    path('courseView/<code>', views.courseView),
    path('levelView/<code>', views.levelView),
    path('dashboard/', dashboard, name="dashboard"),
    path('signout', signout, name="signout"),
    path('login_user/', login_user, name="login_user"),
    path('qanda/', qanda, name="qanda"),
    path('course/', course, name="course"),
    path('level/', level, name="level"),
    path('feedback/', feedback, name="feedback"),
    path('change/', change, name="change"),
    path('register_user/', register_user, name="register_user"),
    path("indexhom/", views.indexhom, name="indexhom"),
    path("get-value", views.getValue),
    path('rate/<int:year_level>/', rate, name='rate'),
    path('get_ratings_count/', get_ratings_count, name='get_ratings_count'),




]