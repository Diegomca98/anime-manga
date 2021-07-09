from django.db import models


class Item(models.Model):
    """ Item model for manga and anime """

    PENDING = 'P'
    PROGRESS = 'IP'
    FINISHED = 'F'
    DATE = 'UD'
    PERSONAL_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
        (DATE, 'Up to Date'),
    ]
    title = models.CharField(max_length=500, verbose_name="Name", unique=True)
    description = models.TextField(verbose_name="Description")
    is_manga = models.BooleanField(default=True, verbose_name="Manga?")
    is_anime = models.BooleanField(default=False, verbose_name="Anime?")
    created_by = models.CharField(verbose_name="Creator", max_length=500)
    animation_studio = models.CharField(verbose_name="Animation Studio", max_length=500)
    status = models.BooleanField(verbose_name="Completely Published?", default=False)
    episodes = models.IntegerField(verbose_name="Total Episodes or Volumes", default=13)
    personal_status = models.CharField(
        max_length=2,
        choices=PERSONAL_STATUS_CHOICES,
        default=PENDING,
        verbose_name="Personal Status"
    )
    
    

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.title