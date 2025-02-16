from django.db import models

class GameApp(models.Model):
    name = models.CharField("Game Name", max_length=200)
    mobile_friendly = models.BooleanField("Mobile Friendly")
    image = models.ImageField("Header image", upload_to="images/")
    url = models.CharField("URL", max_length=200)

    def __str__(self):
        return self.name