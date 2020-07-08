from rest_framework import routers
from django.conf.urls import url
from django.urls import path, include
from .api import BoardViewSet, LinkViewSet, NewsViewSet, PollViewSet, PollOptionViewSet, CommentViewSet, ImageViewSet, DocumentViewSet
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
router = routers.DefaultRouter()

#router.register('api/boards/<int:board_id>/images', ImageViewSet)
router.register('api/boards', BoardViewSet)
router.register('api/boards/<int:board_id>/links', LinkViewSet)
urlpatterns = [
    path('api/boards/<int:pk>/join', BoardViewSet.as_view({'get':'join'})),
    path('api/boards/<int:board_id>/links', LinkViewSet.as_view({'get':'list', 'post':'create'})),
    path('api/boards/<int:board_id>/links/<int:pk>', LinkViewSet.as_view({'delete':'destroy'})),
    path('api/boards/<int:board_id>/news', NewsViewSet.as_view({'get':'list', 'post':'create'})),
    path('api/boards/<int:board_id>/news/<int:pk>', NewsViewSet.as_view({'delete':'destroy'})),
    path('api/boards/<int:board_id>/polls', PollViewSet.as_view({'get':'list', 'post':'create'})),
    path('api/boards/<int:board_id>/polls/<int:pk>', PollViewSet.as_view({'delete':'destroy'})),
    path('api/polls/<int:poll_id>/poll-options/', PollOptionViewSet.as_view({'get':'list', 'post':'create'})),
    path('api/polls/<int:poll_id>/poll-options/<int:pk>', PollOptionViewSet.as_view({'delete':'destroy'})),
    path('api/news/<int:news_id>/comments', CommentViewSet.as_view({'get':'list', 'post':'create'})),
    path('api/news/<int:news_id>/comments/<int:pk>', CommentViewSet.as_view({'delete':'destroy'})),
    path('api/boards/<int:board_id>/images', ImageViewSet.as_view({'get':'list', 'post':'create'})),
    path('api/boards/<int:board_id>/images/<int:pk>', ImageViewSet.as_view({'delete':'destroy', 'get':'retrieve'})),
    path('api/boards/<int:board_id>/docs', DocumentViewSet.as_view({'get':'list', 'post':'create'})),
    path('api/boards/<int:board_id>/docs/<int:pk>', DocumentViewSet.as_view({'delete':'destroy', 'get':'retrieve'}))
    # path('api/images/uploads/<img_name>', ImageAPI.as_view())


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
