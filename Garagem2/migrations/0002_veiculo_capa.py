# Generated by Django 4.2.4 on 2023-08-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('Garagem2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='capa',
            field=models.ManyToManyField(related_name='+', to='uploader.image'),
        ),
    ]
