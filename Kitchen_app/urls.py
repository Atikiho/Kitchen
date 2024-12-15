from django.urls import path

from Kitchen_app.views import (
    Index,
    DishList,
    DishTypeList,
    DishDetail,
    DishCreate,
    DishDelete,
    DishTypeCreate,
    DishTypeDelete,
    DishUpdate,
    DishTypeUpdate,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dish/", DishList.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetail.as_view(), name="dish-detail"),
    path("dish-create/", DishCreate.as_view(), name="dish-create"),
    path("dish-update/<int:pk>/", DishUpdate.as_view(), name="dish-update"),
    path("dish-delete/<int:pk>", DishDelete.as_view(), name="dish-delete"),
    path("dish-type/", DishTypeList.as_view(), name="dish-type-list"),
    path(
        "dish-type-create/",
        DishTypeCreate.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-type-update/<int:pk>/",
        DishTypeUpdate.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-type-delete/<int:pk>/",
        DishTypeDelete.as_view(),
        name="dish-type-delete"
    ),
]
