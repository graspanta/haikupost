# Generated by Django 3.2 on 2022-04-14 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    replaces = [('haikus', '0001_initial'), ('haikus', '0002_review'), ('haikus', '0003_haiku_image'), ('haikus', '0004_auto_20220409_0048'), ('haikus', '0005_rename_discription_haiku_description'), ('haikus', '0006_alter_haiku_description'), ('haikus', '0007_alter_haiku_description'), ('haikus', '0008_alter_haiku_description'), ('haikus', '0009_alter_haiku_date'), ('haikus', '0010_alter_haiku_date'), ('haikus', '0011_alter_haiku_date'), ('haikus', '0012_alter_haiku_date'), ('haikus', '0013_alter_haiku_date'), ('haikus', '0014_alter_haiku_description'), ('haikus', '0015_alter_haiku_date'), ('haikus', '0016_auto_20220409_0302'), ('haikus', '0017_alter_haiku_options'), ('haikus', '0018_alter_haiku_options'), ('haikus', '0019_alter_haiku_author'), ('haikus', '0020_alter_haiku_author'), ('haikus', '0021_alter_haiku_author'), ('haikus', '0022_alter_haiku_author'), ('haikus', '0023_alter_haiku_author'), ('haikus', '0024_alter_haiku_author'), ('haikus', '0025_auto_20220410_0309')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Haiku',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('poem', models.CharField(max_length=200, verbose_name='はいく')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='イメージ')),
                ('description', models.TextField(blank=True, verbose_name='せつめい')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('haiku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='haikus.haiku')),
            ],
        ),
    ]
