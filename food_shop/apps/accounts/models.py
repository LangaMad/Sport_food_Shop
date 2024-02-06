from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)



class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self) -> str:
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self) -> None:
        link: str = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link: str = f'{settings.DOMAIN_NAME}{link}'
        subject: str = f'Confirmation of the account for {self.user.username}'
        message: str = f'To confirm the account {self.user.email} follow this link {verification_link}'

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.user.email],
                fail_silently=False,
            )
        except SMTPException as e:
            print(f"!!!---Error sending email: {e}---!!!")

    def is_expired(self) -> bool:
        return True if now() >= self.expiration_time else False