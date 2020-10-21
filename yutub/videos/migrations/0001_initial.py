# Generated by Django 3.1.2 on 2020-10-21 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('media', models.FileField(upload_to='videos/media_upload')),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]