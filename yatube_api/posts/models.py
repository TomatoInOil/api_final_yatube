from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель сообществ."""

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель постов."""

    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    image = models.ImageField(
        upload_to="posts/", null=True, blank=True, verbose_name="Картинка"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name="Сообщество",
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.text[: settings.POST_STR_LENGTH]


class Comment(models.Model):
    """Модель комментариев."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Комментатор",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
    )
    text = models.TextField(verbose_name="Текст")
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.text[: settings.COMMENT_STR_LENGTH]


class Follow(models.Model):
    """Модель подписок."""

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Автор",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Верный читатель",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"],
                name="excluding_duplicate_subscriptions",
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F("following")),
                name="cannot_subscribe_to_myself",
            ),
        ]

    def __str__(self):
        return f"{self.user} subscribed> {self.following}"
