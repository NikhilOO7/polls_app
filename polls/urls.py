from django.urls import include, path
# from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetails, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetails.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('users/', UserCreate.as_view(), name='create_user'),
    path('login/', views.obtain_auth_token, name='login')
]
urlpatterns += router.urls