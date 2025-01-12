from datetime import datetime, timezone

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.shortcuts import render
from django.utils.crypto import get_random_string

from common.tasks import send_email

from .models import PendingUser, User

def register(request: HttpRequest):
    if request.method == "POST":
        email: str = request.POST["email"]
        password: str = request.POST["password"]
        cleaned_email = email.lower()

        if User.objects.filter(email=cleaned_email).exists():
            messages.error(request, "Email exists on the platform")
            return redirect("register")

        else:
            verification_code = get_random_string(10)
            PendingUser.objects.update_or_create(
                email=cleaned_email,
                defaults={
                    "password": make_password(password),
                    "verification_code": verification_code,
                    "created_at": datetime.now(timezone.utc),
                },
            )
            send_email(
                "Verify Your Account",
                [cleaned_email],
                "emails/email_verification_template.html",
                context={"code": verification_code},
            )
            messages.success(request, f"Verification code sent to {cleaned_email}")
            return render(
                request, "verify_account.html", context={"email": cleaned_email}
            )

    else:
        return render(request, "register.html")