from django.urls import path

from Kitchen_app.views import (
    index,
    CookList,
    CookCreate,
    DishList,
    DishTypeList,
    CookDetail,
    CookDelete,
    DishDetail,
    DishCreate,
    DishDelete,
    DishTypeCreate,
    DishTypeDelete,
    CookUpdate,
    DishUpdate,
    DishTypeUpdate,
)

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookList.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetail.as_view(), name="cook-detail"),
    path("sign-up/", CookCreate.as_view(), name="cook-create"),
    path("cook/delete/<int:pk>/", CookDelete.as_view(), name="cook-delete"),
    path("cook/update/<int:pk>/", CookUpdate.as_view(), name="cook-update"),
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
