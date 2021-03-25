from django.db import models

class Useraccount(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def user_register(self):
        self.save()

    def isExit(self):
        if Useraccount.objects.filter(email=self.email):
            return True
        else:
            return False

    @staticmethod
    def get_user_email(email):
        try:
            return Useraccount.objects.get(email=email)
        except:
            return False