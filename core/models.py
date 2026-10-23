from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import F, Q


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


class UserSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settings",
    )
    font_size = models.PositiveSmallIntegerField(default=18)
    line_spacing = models.FloatField(default=1.5)
    theme = models.CharField(
        max_length=10,
        choices=[("light", "Light"), ("dark", "Dark"), ("sepia", "Sepia")],
        default="light",
    )
    bionic_reading = models.BooleanField(default=False)
    focus_mode = models.BooleanField(default=False)
    sound = models.CharField(
        max_length=20,
        choices=[
            ("off", "Off"),
            ("rain", "Rain"),
            ("cafe", "Cafe"),
            ("white_noise", "White noise"),
        ],
        default="off",
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(font_size__gte=12, font_size__lte=32),
                name="usersettings_font_size_range",
            ),
            models.CheckConstraint(
                condition=Q(line_spacing__gte=1.0, line_spacing__lte=3.0),
                name="usersettings_line_spacing_range",
            ),
            models.CheckConstraint(
                condition=Q(theme__in=["light", "dark", "sepia"]),
                name="usersettings_theme_valid",
            ),
            models.CheckConstraint(
                condition=Q(sound__in=["off", "rain", "cafe", "white_noise"]),
                name="usersettings_sound_valid",
            ),
        ]

    def __str__(self):
        return f"Settings for {self.user.email}"


hex_color_validator = RegexValidator(
    regex=r"^#[0-9A-Fa-f]{6}$",
    message="Color must be a hex code like #FF8800.",
)


class Collection(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collections",
    )
    name = models.CharField(max_length=100)
    color = models.CharField(
        max_length=7,
        validators=[hex_color_validator],
        default="#FFD166",
    )

    def __str__(self):
        return f"{self.name} ({self.user.email})"


class Lesson(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Panel(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="panels",
    )
    order = models.PositiveIntegerField()
    text = models.TextField()

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["lesson", "order"],
                name="panel_unique_order_per_lesson",
            ),
        ]

    def __str__(self):
        return f"{self.lesson.title} - panel {self.order}"


class Pin(models.Model):
    panel = models.ForeignKey(
        Panel,
        on_delete=models.CASCADE,
        related_name="pins",
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="pins",
    )
    start_offset = models.PositiveIntegerField()
    end_offset = models.PositiveIntegerField()
    text_snippet = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        constraints = [
            models.CheckConstraint(
                condition=Q(end_offset__gt=F("start_offset")),
                name="pin_end_after_start",
            ),
        ]

    def __str__(self):
        return f"Pin: {self.text_snippet[:30]}"