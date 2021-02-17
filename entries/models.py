from django.db import models

class Book(models.Model):
    book_title = models.CharField (max_length = 250)
    author = models.CharField (max_length = 250)
    publication_date = models.CharField (max_length = 25)
    plot_summary  = models.TextField ()

    def __str__(self):
        return self.book_title
        
    objects = models.Manager()
