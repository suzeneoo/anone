from django.db import models
from user.models import User

# 게시판

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 본 유저가 탈퇴하면 유저의 글도 함께 삭제 -> cascade
    # 본 유저가 탈퇴해도 본 유저의 이름은 사라지지만 글은 삭제 안 되게 할래 -> SET_NULL, null=True
    title = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(null=True)

    class Mete:
        db_table="post"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 글이 삭제되면 댓글도 같이 삭제 
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comment"