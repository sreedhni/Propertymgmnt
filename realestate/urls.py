from django.urls import path
from realestate import views

urlpatterns = [
    path("register",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("index",views.IndexView.as_view(),name="index"),
    path("property/add/",views.PropertyCreateView.as_view(),name="property-add"),
    path("property/",views.PropertyListView.as_view(),name="property-all"),
    path("property/<int:pk>/",views.PropertyDetailView.as_view(),name="property-detail"),
    path("property/<int:pk>/unit/",views.UnitAddView.as_view(),name="unit-add"),
    path("lease/",views.LeaseView.as_view(),name="lease-all"),
    path("tenant/all/",views.TenantView.as_view(),name="tenant-all"),
    path("tenant/<int:pk>/",views.TenantDetailView.as_view(),name="tenant-detail"),

    path("tenant/<int:pk>/lease",views.LeaseDetailView.as_view(),name="lease-detail"),
     path("user/tenant",views.TenantCreateView.as_view(),name="tenant-add"),
    path("user/property/",views.UPropertyListView.as_view(),name="property-list"),
    path("user/unit/<int:pk>/lease",views.LeaseAddView.as_view(),name="lease-add"),
    path("logout",views.sign_out_view,name="signout"),
    path("",views.HomeView.as_view(),name="home")



]
