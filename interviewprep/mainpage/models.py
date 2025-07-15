from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class InitialInput(models.Model):
    # interviewee name and background info
    vieweeName = models.CharField(max_length=100, verbose_name="Your Name")
    vieweeInfo = models.CharField(max_length=600, verbose_name="Some Info About You")
    
    # interviewee resume
    resume = models.FileField(upload_to="uploads/",
                              validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
                              verbose_name="Resume (PDF)")
    
    # position interviewing for
    position = models.CharField(max_length=100, verbose_name="Position You're Interviewing For")
    
    # info about company
    context = models.CharField(max_length = 600, verbose_name="Recruiting Company Name + Info")
    
    def __str__(self):
        return self.vieweeName


