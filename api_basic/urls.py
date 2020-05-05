from django.urls import path,include
# from .views import article_list,article_detail,ArticleList,ArticleDetail,GenericAPIView,ArticleViewSet,ArticleGenericViewSet,ArticleModelViewSet
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet,ArticleTypeViewSet,AuthorViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
# router.register('generic', ArticleGenericViewSet, basename='generic')
# router.register('model', ArticleModelViewSet, basename='model')
router.register('article_type',ArticleTypeViewSet,basename='article_type')
router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    path('viewset/',include(router.urls)),
    # path('viewset//<int:pk>/',include(router.urls)),
    # # path('article/', article_list),
    # path('article/', ArticleList.as_view()),
    # # path('detail/<int:pk>', article_detail),
    # path('detail/<int:pk>/', ArticleDetail.as_view()),
    # path('generic/article/<int:id>/', GenericAPIView.as_view()),
]