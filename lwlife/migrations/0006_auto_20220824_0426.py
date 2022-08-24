# Generated by Django 3.2.9 on 2022-08-23 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lwlife', '0005_alter_answer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='lwlife.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
