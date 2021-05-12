from django.db import models

#these are used in the choices parameters
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

#the treeaid model that stores web recorded tree reportings
class treeaid_databese(models.Model):
    cercle = models.CharField(max_length=100)
    tree = models.CharField(max_length=100)
    tree_count = models.IntegerField()
    phone_number = models.CharField(max_length=30)

#the Document model that stores vxml entries
class Document(models.Model):
    rec_commune = models.FileField(upload_to='media/',null=True)
    rec_location  = models.FileField(upload_to='media/',null=True)
    rec_name = models.FileField(upload_to='media/',null=True)
    cercle_num = models.CharField(max_length=30, null=True, choices=cercles)
    tree_num  = models.CharField(max_length=30, null=True, choices=trees)
    tree_count = models.IntegerField()
    chosen_language = models.CharField(max_length=30, null=True, choices=languages)
    phone = models.CharField(max_length=30, null=True)
    #src_commune = models.CharField(max_length=100, null=True)

