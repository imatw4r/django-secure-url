# Generated by Django 3.1.3 on 2020-11-23 01:34

from django.db import migrations, models
import django.db.models.deletion
import secure_resource.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecureElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.URLField(max_length=128, null=True)),
                ('source_file', models.FileField(null=True, upload_to=secure_resource.models.get_file_path)),
                ('password', models.CharField(default=secure_resource.models.generate_password, max_length=128)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElementRedirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires_at', models.DateTimeField(default=secure_resource.models.set_expiration_date)),
                ('redirect_type', models.CharField(choices=[('FILE', 'File'), ('URL', 'Url')], max_length=5)),
                ('visited', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('element', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='redirect', to='secure_resource.secureelement')),
            ],
        ),
    ]
