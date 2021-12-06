# Generated by Django 3.2.9 on 2021-12-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='produits',
            name='picture_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produits',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
