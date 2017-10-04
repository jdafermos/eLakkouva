from django.conf.urls import include, url
from .views import HomePageView, thePopupView, thePitsDatasetView, theBulbsDatasetView, theLeaksDatasetView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'theHomePageViewURL'),
    url(r'^PopupForm/$', thePopupView, name = 'thePopupViewURL'),
    url(r'^PitsData/$', thePitsDatasetView, name = 'thePitsDatasetViewURL'),
    url(r'^BulbsData/$', theBulbsDatasetView, name = 'theBulbsDatasetViewURL'),
    url(r'^LeaksData/$', theLeaksDatasetView, name = 'theLeaksDatasetViewURL'),
]