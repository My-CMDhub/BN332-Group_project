# Generated by Django 4.2 on 2025-04-10 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='actual_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='archived_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='dependencies',
            field=models.ManyToManyField(blank=True, related_name='dependent_tasks', to='tasks.task'),
        ),
        migrations.AddField(
            model_name='task',
            name='estimated_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='parent_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtasks', to='tasks.task'),
        ),
        migrations.AddField(
            model_name='task',
            name='position',
            field=models.PositiveIntegerField(default=0, help_text='Position for drag & drop prioritization'),
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, help_text='Duration in hours:minutes:seconds', null=True)),
                ('is_billable', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supabase_id', models.CharField(blank=True, max_length=255, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_entries', to='tasks.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Time Entry',
                'verbose_name_plural': 'Time Entries',
                'ordering': ['-start_time'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supabase_id', models.CharField(blank=True, max_length=255, null=True)),
                ('is_synced', models.BooleanField(default=False)),
                ('last_synced_at', models.DateTimeField(blank=True, null=True)),
                ('members', models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('field_type', models.CharField(choices=[('TEXT', 'Text'), ('NUMBER', 'Number'), ('DATE', 'Date'), ('BOOLEAN', 'Boolean'), ('DROPDOWN', 'Dropdown')], max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('default_value', models.JSONField(blank=True, null=True)),
                ('options', models.JSONField(blank=True, help_text='Options for dropdown fields', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projects', models.ManyToManyField(blank=True, related_name='custom_fields', to='tasks.project')),
            ],
            options={
                'verbose_name': 'Custom Field',
                'verbose_name_plural': 'Custom Fields',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.project'),
        ),
        migrations.CreateModel(
            name='TaskVersion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('version_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(max_length=20)),
                ('priority', models.CharField(max_length=10)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data_snapshot', models.JSONField(help_text='Complete snapshot of task data at this version')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='tasks.task')),
            ],
            options={
                'verbose_name': 'Task Version',
                'verbose_name_plural': 'Task Versions',
                'ordering': ['-version_number'],
                'unique_together': {('task', 'version_number')},
            },
        ),
        migrations.CreateModel(
            name='CustomFieldValue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='tasks.customfield')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_field_values', to='tasks.task')),
            ],
            options={
                'verbose_name': 'Custom Field Value',
                'verbose_name_plural': 'Custom Field Values',
                'unique_together': {('task', 'field')},
            },
        ),
    ]
