from django.db import models

# Create your models here.
class Student(models.Model):
	prenom = models.CharField(max_length=20)
	nom = models.CharField(max_length=20)
	date_naissance = models.DateField()	

	def __str__(self):
		return self.prenom

	def __repr__(self):
		return "<Student {}>".format(self.prenom)

class Note(models.Model):
	student = models.ForeignKey(Student , on_delete=models.CASCADE)
	matiere = models.CharField(max_length=20)
	note = models.TextField(default=0)
	coefficient = models.IntegerField(default=0)

	def __str__(self):
		return self.matiere

	def __repr__(self):
		return "<Note {}>".format(self.matiere)