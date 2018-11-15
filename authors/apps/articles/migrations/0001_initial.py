# Generated by Django 2.1.2 on 2018-11-15 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favorited', models.BooleanField(default=False)),
                ('favorites_count', models.IntegerField(default=0)),
                ('image_url', models.URLField()),
                ('audio_url', models.URLField(blank=True, null=True)),
                ('read_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LikeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_status', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_id', to='articles.Article')),
            ],
        ),
    ]
