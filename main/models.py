from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    email = models.EmailField("Электронная почта", unique=True)
    height = models.PositiveIntegerField("Рост (см)", null=True, blank=True)
    weight = models.PositiveIntegerField("Вес (кг)", null=True, blank=True)
    rating = models.IntegerField("Рейтинг", default=0)
    is_in_roster = models.BooleanField("В основном составе", default=False)
    avatar = models.ImageField("Фото игрока", upload_to='players/', null=True, blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    jersey_number = models.PositiveIntegerField("Игровой номер", null=True, blank=True)

    POSITIONS = [
        ('PG', 'Разыгрывающий'),
        ('SG', 'Атакующий защитник'),
        ('SF', 'Легкий форвард'),
        ('PF', 'Мощный форвард'),
        ('C', 'Центровой'),
        ('A', 'Игрок'),
    ]
    position = models.CharField("Позиция", max_length=2, choices=POSITIONS, default='A')

    USERNAME_FIELD = 'email'  # Теперь логинимся по почте
    REQUIRED_FIELDS = ['username']  # Остается обязательным для создания через терминал

    def __str__(self):
        return self.email
    
    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return "--"