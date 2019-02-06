from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)

### For future projects 

# Create the model above for application dependant on whats needed

# Add the Application to settings check settings.py for reference

# Add the application to admin with admin.sites.register(appname)

# Create a migration with python manage.py makemigration

# Migrate the application with python manage.py migrate