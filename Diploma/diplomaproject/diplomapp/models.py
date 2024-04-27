from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator #, RegexValidator
from django.contrib.auth import get_user_model

GENDER_CHOICE = (
    ("M", "Мужчина"),
    ("F", "Женщина"),
)
class User(AbstractUser):
    pass


User = get_user_model()

# phone_number_regex = RegexValidator(regex=r"^[0-9](?:[ -]?[0-9]){0,14}$")


class SpecialistProfile(models.Model):
    """ Описание класса специалист"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField("Имя", max_length=50, blank=False, default="Name")
    lastname = models.CharField("Фамилия", max_length=50, blank=False, default="Surname")
    patronimic = models.CharField("Отчество", max_length=128, null=True, default="Patronimic")
    phonenumber = models.CharField("Номер телефона", max_length=16, blank=False, default=1)
    about = models.TextField("О себе", max_length=300, blank=False, default="About")
    age = models.IntegerField("Возраст", blank=False, default=18)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=50, blank=False)
    registered = models.DateTimeField('Registered', auto_now_add=True)
    avatar = models.ImageField("Аватар", default=None, blank=False,
                               validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=2)
    reviews = models.TextField("Отзывы", max_length=300, default="Reviews")
    diplomas = models.ImageField("Дипломы", default=None)
    city = models.CharField("Город", max_length=128, blank=False, default="City")

    def save(self):
        super().save()

        avatar = Image.open(self.avatar.path)

        if avatar.height > 300 or avatar.width > 300:
            output_size = (300, 300)
            avatar.thumbnail(output_size)
            avatar.save(self.avatar.path)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = [
            "registered", "rating", "age", "city"
        ]


    # @receiver(post_save, sender=User)
    # def create_or_update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         instance.profile = SpecialistProfile.objects.create(user=instance)
    #     instance.profile.save()


class Diploma(models.Model):
    """ Расширение для класса специалист для прикрепления файла с фото дипломов"""
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE)
    diploma_upload = models.ImageField(upload_to="images/")
    diploma_name = models.TextField("Diploma_name", max_length=300)


class Customer(models.Model):
    """ Модель для заявки на исполнение задачи"""
    name = models.CharField("Имя", max_length=50, blank=False)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=50, blank=False)
    phone_number = models.CharField(max_length=16, unique=True)
    text = models.TextField("Запрос", blank=False)

    class Meta:
        db_table = "customer"
        verbose_name = "Форма запроса"
        verbose_name_plural = "Формы запроса"
