from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
###### class which helps creating custom registration instead of default django`s
class MyAccountManager(BaseUserManager):
    def create_user(self, email, password, access_to_data, first_name, last_name ):
        user = self.model(
            email=self.normalize_email(email),
            access_to_data=True,
            first_name = self.first_name,
            last_name = self.last_name,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, access_to_data, first_name, last_name ):
        user = self.create_user(
            email,
            password=password,
            access_to_data=True,
            first_name = self.first_name,
            last_name = self.last_name,
            )
        user.is_staff = True
        user.access_to_data = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class CustomUser(AbstractBaseUser):
    RANKS = (("Початківець","Початківець"),("Професіонал","Професіонал"))
    first_name = models.CharField("first_name", max_length=50, blank=True)
    last_name = models.CharField("last_name", max_length=50, blank=True)
    email = models.CharField("email", max_length=250, unique=True)
    # date_joined = models.DateField('date_creat',auto_now_add=True, null=True)
    month_joined = models.CharField('month_joined',max_length=30,blank=True)
    day_joined = models.IntegerField('day_joined',blank=True,default=0)
    year_joined = models.IntegerField('year_joined',blank=True,default=0)
    access_to_data = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
   
    ###### set up username in db af for example email
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['access_to_data', 'password',"first_name","last_name"]
    objects = MyAccountManager()

######      Needs to represent obj name in admin in stead of default names
################
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


