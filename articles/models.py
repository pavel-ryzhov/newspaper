from django.db.models import Model, CharField, DateTimeField, TextField, ForeignKey, CASCADE
from django.conf import settings
from django.urls import reverse

class Article(Model):
    title = CharField(max_length=255)
    body = TextField()
    date = DateTimeField(auto_now_add=True)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk})

class Comment(Model):
    article = ForeignKey(Article, on_delete=CASCADE, related_name='comments')
    comment = CharField(max_length=140)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    def __str__(self):
        return self.comment
    @staticmethod
    def get_absolute_url():
        return reverse('articles')