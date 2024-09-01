from django.db import models

# Create your models here.
class Memo(models.Model) :
    text = models.CharField(max_length = 200)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
#정확히는 장고내에서 Memo라는 이름으로 생성되지는 않는다