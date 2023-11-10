# Generated by Django 4.1.2 on 2023-11-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apaterno_usuario',
            field=models.CharField(default=1, max_length=25, verbose_name='Apellido Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='pnombre_usuario',
            field=models.CharField(default=1, max_length=25, verbose_name='Primer Nombre'),
            preserve_default=False,
        ),
    ]
