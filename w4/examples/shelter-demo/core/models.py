from django.db import models

# Create your models here.


class Dog(models.Model):
    PUPPY = 'PU'
    YOUNG = 'YG'
    ADULT = 'AD'
    SENIOR = 'SR'

    AGE_CHOICES = (
        (PUPPY, 'Puppy'),
        (YOUNG, 'Young'),
        (ADULT, 'Adult'),
        (SENIOR, 'Senior'),
    )

    TINY = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )

    EASYGOING = 1
    PLAYFUL = 3
    ENERGETIC = 5

    ENERGY_LEVEL_CHOICES = (
        (EASYGOING, 'Easygoing'),
        (PLAYFUL, 'Playful'),
        (ENERGETIC, 'Energetic'),
    )

    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    energy_level = models.PositiveIntegerField(choices=ENERGY_LEVEL_CHOICES)
    picture = models.ImageField(upload_to='dogs/', null=True)
    good_with_kids = models.BooleanField(
        verbose_name="Good with kids", default=False)
    good_with_dogs = models.BooleanField(
        verbose_name="Good with other dogs", default=False)
    good_with_cats = models.BooleanField(
        verbose_name="Good with cats", default=False)

    def get_traits(self):
        traits = []
        traits.append(self.get_age_display())
        traits.append(self.get_size_display())
        traits.append(self.get_energy_level_display())
        if self.good_with_kids:
            traits.append("Good with kids")
        if self.good_with_dogs:
            traits.append("Good with other dogs")
        if self.good_with_cats:
            traits.append("Good with cats")

        return traits

    def __str__(self):
        return self.name
