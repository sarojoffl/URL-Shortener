from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import string, random
import qrcode
from io import BytesIO
from django.core.files import File

BASE62 = string.ascii_letters + string.digits

def generate_short_code(length=6):
    return ''.join(random.choices(BASE62, k=length))

class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            code = generate_short_code()
            # Ensure uniqueness
            while ShortURL.objects.filter(short_code=code).exists():
                code = generate_short_code()
            self.short_code = code
        super().save(*args, **kwargs)

        # Generate QR code if not exists
        if not self.qr_code:
            qr_img = qrcode.make(f"{self.get_full_short_url()}")
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            self.qr_code.save(f'{self.short_code}.png', File(buffer), save=False)
            super().save(*args, **kwargs)

    def get_full_short_url(self):
        return f"http://127.0.0.1:8000/{self.short_code}"

    def is_expired(self):
        return self.expires_at and timezone.now() > self.expires_at

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"
