# Generated by Django 4.2 on 2025-04-03 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_locked_until',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='failed_login_attempts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mfa_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='recovery_codes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='requires_password_change',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='supabase_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.CharField(max_length=255)),
                ('device', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='session',
            index=models.Index(fields=['user', 'expires_at'], name='auth_app_se_user_id_11f1a2_idx'),
        ),
    ]
