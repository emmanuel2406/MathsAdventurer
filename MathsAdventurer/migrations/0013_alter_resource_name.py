# Generated by Django 4.1.7 on 2023-06-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MathsAdventurer', '0012_alter_event_written'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
