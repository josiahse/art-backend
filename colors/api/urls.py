from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.colors import ColorsView

urlpatterns = [
  path('sign-up/', SignUp.as_view(), name="sign-up"),
  path('sign-in/', SignIn.as_view(), name="sign-in"),
  path('sign-out/', SignOut.as_view(), name="sign-out"),
  path('change-pw/', ChangePassword.as_view(), name="change-pw"),
  path('colors/<int:pk>/', ColorsView.as_view(), name="colors"),
  # path('color/<int:pk>/', ColorView.as_view(), name="color"),
]
