# Generated by Django 4.0.1 on 2022-01-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nom')),
                ('code', models.CharField(max_length=4, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Région',
                'verbose_name_plural': 'Régions',
            },
        ),
    ]
