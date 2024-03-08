from django.urls import path

from .views import (
EmployerCreate,
EmployerView,
JobAppCreate,
JobAppUpdate,
JobAppView,
JobsCreate,
JobsUpdate,
JobsView,
JobsViewFilter,
JobsViewFilterEmp,
ProfileNameUpdate,
ProfileUpdate,
SeekerCreate,
SeekerView,
ViewProfile
)

urlpatterns = [

    path('getjobs/', JobsView.as_view(),),
    path('getemps/', EmployerView.as_view(),),
    path('getseekers/', SeekerView.as_view(),),
    path('getmyjobs/<str:emp_id>/', JobsViewFilterEmp.as_view()),

    path('getjobs/<str:location>/', JobsViewFilter.as_view()),
    path('getmyapps/<str:seeker_id>/', JobAppView.as_view()),
    path('profile/<str:seeker_id>/', ViewProfile.as_view()),

    path('employer/create/', EmployerCreate.as_view(),),
    path('seeker/create/', SeekerCreate.as_view(),),
    path('jobapp/create/', JobAppCreate.as_view(),),
    path('jobs/create/', JobsCreate.as_view(),),

    path('jobs/update/<int:job_id>/', JobsUpdate.as_view()),
    path('jobapp/update/<int:app_id>/', JobAppUpdate.as_view(),),
    path('profile/update/<int:seeker_id>/', ProfileUpdate.as_view()),
    path('profile/updates/<int:seeker_id>/', ProfileNameUpdate.as_view()),

]
