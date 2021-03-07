# Generated by Django 3.0.8 on 2021-03-07 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_assigned_assessment'),
        ('assessments', '0003_question_question_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.UserProfile'),
        ),
    ]
