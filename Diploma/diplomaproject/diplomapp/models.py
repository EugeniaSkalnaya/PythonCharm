from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model


GENDER_CHOICE = (
    ("M", "Мужчина"),
    ("F", "Женщина"),
)

User = get_user_model()


class Profile(models.Model):
    """ Описание класса профиля специалистя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField("Имя", max_length=50, blank=False, default="Name")
    lastname = models.CharField("Фамилия", max_length=50, blank=False, default="Surname")
    patronimic = models.CharField("Отчество", max_length=128, null=True, default="Patronimic")
    phonenumber = models.CharField("Номер телефона", max_length=16, blank=False, default=1)
    about = models.TextField("О себе", max_length=300, blank=False, default="About")
    age = models.IntegerField("Возраст", blank=False, default=18)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=50, blank=False)
    registered = models.DateTimeField('Registered', auto_now_add=True)
    avatar = models.ImageField("Аватар", default=None, upload_to="images/", blank=False,
                               validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=2)
    reviews = models.TextField("Отзывы", max_length=300, default="Reviews")
    city = models.CharField("Город", max_length=128, blank=False, default="City")


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = [
            "registered", "rating", "age", "city"
        ]


# оставила в комментариях, так как при иногда требуется сохранять запрос в базе данных
# class Customer(models.Model):
#     """ Модель для заявки на исполнение задачи"""
#     name = models.CharField("Имя", max_length=50, blank=False)
#     gender = models.CharField(choices=GENDER_CHOICE, max_length=50, blank=False)
#     phone_number = models.CharField(max_length=16, unique=True)
#     text = models.TextField("Запрос", blank=False)
#
#     class Meta:
#         db_table = "customer"
#         verbose_name = "Форма запроса"
#         verbose_name_plural = "Формы запроса"
