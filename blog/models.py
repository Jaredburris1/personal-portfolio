from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField()
	body = models.TextField(max_length=1500)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_better(self):
		return self.pub_date.strftime('%b %e %Y')


### For future projects 

# Create the model above for application dependant on whats needed

# Add the Application to settings check settings.py for reference

# Add the application to admin with admin.sites.register(appname)

# Create a migration with python manage.py makemigration

# Migrate the application with python manage.py migrate
