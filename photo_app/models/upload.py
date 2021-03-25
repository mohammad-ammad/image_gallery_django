from django.db import models
import datetime


class Upload(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(default=datetime.datetime.today)
    image = models.ImageField(upload_to='uploads/images', default='')



    @staticmethod
    def get_all_data_from_uploads():
        return Upload.objects.all()

    @staticmethod
    def get_img_details(pk):
        return Upload.objects.get(pk=pk)
