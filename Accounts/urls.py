from django.urls import path

from Accounts.views import (
    CookList,
    CookDetail,
    CookCreate,
    CookDelete,
    CookUpdate,
)

urlpatterns = [
    path("cook/", CookList.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetail.as_view(), name="cook-detail"),
    path("sign-up/", CookCreate.as_view(), name="cook-create"),
    path("cook/delete/<int:pk>/", CookDelete.as_view(), name="cook-delete"),
    path("cook/update/<int:pk>/", CookUpdate.as_view(), name="cook-update"),
]
