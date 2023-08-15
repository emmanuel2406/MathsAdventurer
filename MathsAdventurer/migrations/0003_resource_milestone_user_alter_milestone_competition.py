# Generated by Django 4.1.7 on 2023-06-14 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MathsAdventurer', '0002_competition_users_watching_milestone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('url', models.URLField()),
                ('difficulty', models.CharField(choices=[('Valley', 'introductory'), ('Slope', 'intermediate'), ('Summit', 'advanced')], default='Valley', max_length=30)),
                ('topic', models.CharField(choices=[('General Competition', 'Gen'), ('Algebra', 'Alg'), ('Combinatorics', 'Com'), ('Geometry', 'Geo'), ('Number Theory', 'Num')], default='General Competition', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_milestones', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='milestone',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_milestones', to='MathsAdventurer.competition'),
        ),
    ]