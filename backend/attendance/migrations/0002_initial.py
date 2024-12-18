# Generated by Django 5.0.4 on 2024-10-27 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attendance', '0001_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='rooms.room'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('user', 'lesson')},
        ),
    ]
