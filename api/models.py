from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name ,tc and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email,  given email, name ,tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            tc=tc,
            name=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def has_module_perms(app_label):
        return True


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        default=None,
        blank=True,
        null=True,
        unique=True
    )

    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['name', 'tc']
  
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class inv(models.Model):
    inv_state=models.IntegerField(null=True,blank=True)
    deleted =models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    uid        = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.deleted
   
    
class bank_details(models.Model):
    account_holder=models.CharField(max_length=100)
    deleted =models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    uid        = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=15)
    account_number = models.CharField(max_length=25)
    branch_address =models.CharField(max_length=100)
    REQUIRED_FIELDS=['uid']
    def __str__(self):
        return self.account_holder