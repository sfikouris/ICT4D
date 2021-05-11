from django.db import models

cercles = [("Sikasso","Sikasso"),
           ("Koutiala","Koutiala"),
           ("Bougouni","Bougouni"),
           ("Kadiolo","Kadiolo",),
           ("Kolondiéba","Kolondiéba"),
           ("Yanfolila","Yanfolila"),
           ("Yorosso","Yorosso")]
trees = [("Pterocarpus erinaceus","Pterocarpus erinaceus"),
         ("Terminalia habeensis","Terminalia habeensis"),
         ("Afzelia Africana","Afzelia Africana"),
         ("Khaya senegalensis","Khaya senegalensis"),
         ("Dalbergia melanoxylon","Dalbergia melanoxylon"),
         ("Unknown","Unknown")]
languages= [("en","english"),("br","bambara"),("fr","france")]


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
    rec_commune = models.FileField(upload_to='commune/',null=True)
    rec_location  = models.FileField(upload_to='location/',null=True)
    rec_name = models.FileField(upload_to='name/',null=True)
    cercle_num = models.CharField(max_length=30, null=True, choices=cercles)
    tree_num  = models.CharField(max_length=30, null=True, choices=trees)
    tree_count = models.IntegerField()
    chosen_language = models.CharField(max_length=30, null=True, choices=languages)
    phone = models.CharField(max_length=30, null=True)
    time = models.DateTimeField(auto_now_add=True)
    src_commune = models.CharField(max_length=150, null=True)
    src_location = models.CharField(max_length=150, null=True)
    src_name  = models.CharField(max_length=150, null=True)

