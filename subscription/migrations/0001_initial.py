# Generated by Django 5.1.5 on 2025-01-31 09:32

import django.db.models.deletion

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Subs",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("start_date", models.DateTimeField(auto_now_add=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                ("next_bill_date", models.DateTimeField(blank=True, null=True)),
                ("remaining_bill_date", models.DurationField(blank=True, null=True)),
                ("auto_renew", models.BooleanField(default=False, null=True)),
                (
                    "cancelled_reason",
                    models.CharField(
                        choices=[
                            ("expensive", "가격이 비싸서"),
                            ("quality", "퀄리티가 마음에 들지 않아서"),
                            ("slow_communication", "소통이 느려서"),
                            ("hire_full_time", "정직원을 구하는 것이 더 편해서"),
                            ("budget_cut", "회사 예산이 줄어들어서"),
                            ("other", "기타"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "other_reason",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="기타 사유 (상세입력)",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubHistories",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("change_date", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("renewal", "갱신"),
                            ("cancel", "취소"),
                            ("pause", "정지"),
                            ("restart", "재개"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sub",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="subscription.subs",
                    ),
                ),
            ],
        ),
    ]
