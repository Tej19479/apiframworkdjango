from django.urls import path, include

from api.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordRestEmailView, UserPasswordRestView, Sendmail, AddBankDetials, Imageupload, planview,Transcatin_intiatie

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('userprofile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-rest-password-email/', SendPasswordRestEmailView.as_view(),
         name='send-rest-password-email'),
    path('send/', Sendmail.as_view(), name='send'),
    path('addbankdetails/', AddBankDetials.as_view(), name='addbankdetails'),
    path('imageupload/', Imageupload.as_view(), name='upload'),
    path('plandetails/<int:inv_id>', planview.as_view(), name='plandisplay'),
    path('trnscation_intiate/', Transcatin_intiatie.as_view(),
         name='trnscation_intiate'),







]
