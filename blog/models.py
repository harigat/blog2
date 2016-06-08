from django.db import models
from django.utils import timezone

class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)	
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title
	#value of pk is automatically set in database
	
class Comment(models.Model):
	post=models.ForeignKey('Post',related_name='comments')
	author=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	approved_comment=models.BooleanField(default=False)
	
	def approve(self):
		self.approved_comment=True
		self.save()
	
	def __str__(self):
		return self.text
		
class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	message=models.TextField()
	created_date=models.DateTimeField()
	def create(self):
		self.created_date=timezone.now()
	def __str__(self):
		return self.message
	