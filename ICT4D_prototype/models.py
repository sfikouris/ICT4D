from django.db import models

cercles = ["Sikasso","Koutiala","Bougouni","Kadiolo","Kolondiéba","Yanfolila","Yorosso"]
trees = ["Pterocarpus erinaceus","Terminalia habeensis","Afzelia Africana","Khaya senegalensis","Dalbergia melanoxylon", "Unknown"]
languages= ["en", "br", "fr"]


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    voice = models.FileField(upload_to='voicexml/')

class treeaid(models.Model):
    cercle = models.CharField(max_length=100)
    tree = models.CharField(max_length=100)
    tree_count = models.IntegerField()
    phone_number = models.CharField(max_length=30)

class Document(models.Model):
    rec_commune = models.FileField(upload_to='media/',null=True)
    rec_location  = models.FileField(upload_to='media/',null=True)
    rec_name = models.FileField(upload_to='media/',null=True)
    cercle_num = models.CharField(max_length=30, null=True, choices=cercles)
    tree_num  = models.CharField(max_length=30, null=True, choices=trees)
    tree_count = models.IntegerField()
    chosen_language = models.CharField(max_length=30, null=True, choices=languages)
    phone = models.CharField(max_length=30, null=True)

