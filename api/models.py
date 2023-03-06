from django.db import models
from datetime import datetime    
from django.utils import timezone

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None,city=None,pin_code=None,PAN=None,aadhaar_number=None,dob=None,
                   address=None,mobile=None):
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
    id=models.BigIntegerField(primary_key=True)
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
    

class cnd(models.Model):
    cnd_name =models.CharField(max_length=200)
    cnd_code=models.CharField(max_length=256)
    is_active =models.IntegerField(null=True,blank=True)
    cnd_group =models.CharField(max_length=200,null=True,blank=True)
    deleted =models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    cnd_parent_id =models.CharField(max_length=100,null=True,blank=True)
    rate=models.DecimalField(null=True,blank=True, decimal_places=2 , max_digits=10)
    max_proposal=models.DecimalField(null=True,blank=True, decimal_places=2 , max_digits=10)
    min_proposal=models.DecimalField(null=True,blank=True, decimal_places=2 , max_digits=10)
    description=models.TextField(null=True,blank=True)
    def __str__(self):
     return self.cnd_name
 
class user_verification(models.Model):
    uid = models.IntegerField(null=True,blank=True)
    verification_type=models.CharField(max_length=100,null=True,blank=True)
    deleted =models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    
    def __str__(self):
     return '%s %s' % (self.uid, self.verification_type)

class user_details(models.Model):
    # uid , fname,lname,dob,address,city,mobile,PAN, addhar number
    uid = models.IntegerField(null=True,blank=True)
    name =models.CharField(max_length=75,null=True,blank=True)
    deleted =models.CharField(max_length=5)
    dob    = models.CharField(max_length=75,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city  =   models.CharField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=100,null=True,blank=True)
    pin_code=models.IntegerField(null=True,blank=True)
    PAN    = models.CharField(max_length=100,null=True,blank=True)
    aadhaar_number= models.CharField(max_length=20,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
class docstore(models.Model):
    uid = models.IntegerField(null=True,blank=True)
    verification_type=models.CharField(max_length=100,null=True,blank=True)
    store_data_image=models.TextField(null=True,blank=True)
    pimage =models.ImageField( upload_to='pimages',null=True,blank=True)
    deleted =models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    
    def __str__(self):
        return self.verification_type
    
class b2b_product_investment_utr_details(models.Model):
      uid = models.IntegerField(null=True,blank=True)
      investment_id=models.BigIntegerField(null=True,blank=True)
      plan_id=models.BigIntegerField(null=True,blank=True)
      pool_id=models.BigIntegerField(null=True,blank=True)
      amount=models.DecimalField(null=True,blank=True, decimal_places=2 , max_digits=10)
      schema_id=models.CharField(max_length=256,null=True,blank=True)
      utr_no=models.CharField(max_length=256,null=True,blank=True)
      txn_id=models.BigIntegerField(null=True,blank=True)
      reconcile=models.CharField(max_length=2,null=True,blank=True)
      escrow_status=models.CharField(max_length=2,null=True,blank=True)
      deleted=models.CharField(max_length=2,null=True,blank=True)
      models.DateTimeField(auto_created=True,auto_now=True)
      created_by=models.IntegerField(null=True,blank=True)
      source=models.CharField(max_length=225,null=True,blank=True)
      callback_url=models.CharField(max_length=225,null=True,blank=True)
      updated=models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True,default=0)
      updated_by=models.IntegerField(null=True,blank=True)
      txn_status=models.IntegerField(null=True,blank=True)
      txn_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
      bank_ref_id=models.CharField(max_length=225,null=True,blank=True)
      utr_post_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
      utr_share_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
      is_funding_started=models.CharField(max_length=2,null=True,blank=True)
      pg_type=models.CharField(max_length=50,null=True,blank=True)
      payment_mode=models.CharField(max_length=50,null=True,blank=True)
      recharge_ref_id=models.IntegerField(null=True,blank=True)
      pool_loan_id=models.BigIntegerField(null=True,blank=True)
      proposal_id=models.IntegerField(null=True,blank=True)
      actual_utr_amount_credit_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
      pt_ref_id=models.CharField(max_length=50,null=True,blank=True)
      
      def __str__(self):
            return self.schema_id
        
class b2b_product_investment_utr_detail(models.Model):
      uid = models.IntegerField(null=True,blank=True)
      investment_id=models.BigIntegerField(null=True,blank=True)
      plan_id=models.BigIntegerField(null=True,blank=True)
      pool_id=models.BigIntegerField(null=True,blank=True)
      amount=models.DecimalField(null=True,blank=True, decimal_places=2 , max_digits=10)
      schema_id=models.CharField(max_length=256,null=True,blank=True)
      utr_no=models.CharField(max_length=256,null=True,blank=True)
      txn_id=models.BigIntegerField(null=True,blank=True)
      reconcile=models.CharField(max_length=3,default="N",null=True)
      escrow_status=models.CharField(max_length=2,null=True,blank=True)
      deleted=models.CharField(max_length=2,default="N",null=True)
      created = models.DateTimeField(default=timezone.now)      
      created_by=models.IntegerField(null=True,blank=True)
      source=models.CharField(max_length=225,null=True,blank=True)
      callback_url=models.CharField(max_length=225,null=True,blank=True)
      updated=models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True,default=0)
      updated_by=models.IntegerField(null=True,blank=True)
      txn_status=models.IntegerField(null=True,blank=True)
      txn_date=models.DateTimeField(default=timezone.now,null=True,blank=True)
      bank_ref_id=models.CharField(max_length=225,null=True,blank=True)
      utr_post_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
      utr_share_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
      is_funding_started=models.CharField(max_length=2,null=True,blank=True)
      pg_type=models.CharField(max_length=50,null=True,blank=True)
      payment_mode=models.CharField(max_length=50,null=True,blank=True)
      recharge_ref_id=models.IntegerField(null=True,blank=True)
      pool_loan_id=models.BigIntegerField(null=True,blank=True)
      proposal_id=models.IntegerField(null=True,blank=True)
      actual_utr_amount_credit_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
      pt_ref_id=models.CharField(max_length=50,null=True,blank=True)
      
      def __str__(self):
            return self.schema_id
      
      
      
      

    