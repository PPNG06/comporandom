from django.db import models

# Create your models here.
class Character(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    image_url=models.CharField(max_length=1000,blank=True, null=True)
    index=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
class Vehicle(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    image_url=models.CharField(max_length=1000,blank=True, null=True)
    index=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
class Tire(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    image_url=models.CharField(max_length=1000,blank=True, null=True)
    index=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
class Glider(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    image_url=models.CharField(max_length=1000,blank=True, null=True)
    index=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
class Compo(models.Model):
    char = models.ForeignKey(Character, on_delete=models.CASCADE,blank=True, null=True)
    veh = models.ForeignKey(Vehicle, on_delete=models.CASCADE,blank=True, null=True)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE,blank=True, null=True)
    glider = models.ForeignKey(Glider, on_delete=models.CASCADE,blank=True, null=True)
    index=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.char.name}-{self.veh.name}-{self.tire.name}-{self.glider.name}"
