from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
# Create your models here.
CHOICES=(
	("GEN" , "GEN" ),
	("OBC" , "OBC" ),
	("SC" , "SC" ),
	("ST" , "ST" ),
	("GENPWD" , "GENPWD" ),
	("OBCPWD" , "OBCPWD" ),
	("SCPWD" , "SCPWD" ),
	("STPWD" , "STPWD" ),
	)

CHOICES1=(
	("MALE","MALE"),
	("FEMALE","FEMALE"),
	("OTHER","OTHER"),
	)



class College(models.Model):
	name = models.CharField(max_length=100,null=False)
	def __str__(self):
		return self.name


class Branch(models.Model):
	name = models.CharField(max_length=100,null=False)
	college = models.ForeignKey(College,on_delete=models.CASCADE,null=False)
	capacity = models.IntegerField(default=50)
	preferences=models.CharField(max_length=1000,default="",null=True,blank=True)
	def setpreferences(self,x):
		self.preferences = ",".join(x)

	def getpreferences(self):
		return (self.preferences).split(',')

	def __str__(self):
		return self.college.name + "-" + self.name


class Candidate(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	rollnumber = models.CharField(max_length=15,null=False,unique=True)
	category = models.CharField(max_length=100,choices=CHOICES,null=False)
	gender = models.CharField(max_length=100,choices=CHOICES1,null=False)
	rank = models.IntegerField(null=False,unique=True)
	birthdate = models.DateField(null=False)
	email = models.EmailField(null=False)
	phone = PhoneField(null=False)
	preferences=models.CharField(max_length=1000,default="",null=True,blank=True)
	def setpreferences(self,x):
		self.preferences = ",".join(x)

	def getpreferences(self):
		return (self.preferences).split(',')

	final_seat=models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.rollnumber


