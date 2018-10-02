from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
from django import forms


class UserManager(BaseUserManager):
    def create_user(self,email,full_name,password,is_active=True,is_admin=False, is_staff=False):
        if not email:
            raise ValueError("users must enter an email address")
        if not full_name:
            raise ValueError("full name must be enter")
        if not password:
            raise ValueError("users must have a password")

        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using = self._db)
        return user_obj

    def create_superuser(self,email,full_name,password):
        user = self.create_user(
            email,
            full_name,
            password= password,
            is_admin= True, 
            is_staff= True,
        )
        return user
    def create_staffuser(self,email,full_name,password):
        user = self.create_user(
            email,
            full_name,
            password= password,
            is_staff= True, 
        )
        return user
class User(AbstractBaseUser):
    StuComp_list = (('Company','Company'),('Tanent','Tanent'),)
    username = models.CharField(max_length = 255)
    full_name = models.CharField(max_length = 255,blank=True , null=True)
    email    = models.EmailField(max_length = 255, unique = True,default = "")
    mobile   = models.IntegerField(max_length = 255,blank=True , null=True)
    student_company =models.CharField(max_length=20, choices=StuComp_list) 
    active   = models.BooleanField(default=True)
    staff   = models.BooleanField(default=False)
    admin   = models.BooleanField(default=False)
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    password = models.CharField(max_length=255)
    password1 = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name','password']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
        
class Subscribers(models.Model):
    Email = models.EmailField(max_length = 255)

    def __str__(self):
        return self.Email