# accounts/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """Manager for custom user model."""
    
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user."""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(email, password, **extra_fields)


class LogisticUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model that replaces the default User model."""
    class usertype(models.TextChoices):
        driver = "driver"
        admin = "admin"
    
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(choices=usertype, default=usertype.admin, max_length=150)
    liscence = models.ImageField(upload_to='driver_photos/', blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='logisticuser_set',  # Use a unique related_name
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='logisticuser_set',  # Use a unique related_name
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email



    
    
class CreditPoint(models.Model):
    class detail_status(models.TextChoices):
        credited = 'credited'
        debited = 'debited'
    user = models.ForeignKey(LogisticUser, related_name="logistic_user", on_delete=models.CASCADE)
    c_value = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=detail_status, default=detail_status.credited)
    
    
    
class DriverCreditSum(models.Model):
    class credit_status(models.TextChoices):
        assigned = 'assigned'
        redeemed = 'redeemed'
    sum = models.IntegerField()
    status = models.CharField(max_length=20, choices=credit_status, default=credit_status.assigned)
    create_at = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField()
    user = models.ForeignKey(LogisticUser, related_name="credit_user", on_delete=models.CASCADE)
    
    

    

class Status(models.Model):
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    order = models.IntegerField(default=1)

class TripAction(models.Model):
    class Action(models.TextChoices):
        accept = 'accept'
        reject = 'reject'
    
    driver = models.ForeignKey(LogisticUser, on_delete=models.CASCADE)
    trip= models.ForeignKey('Trip.Trip', on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=Action, default=Action.accept)