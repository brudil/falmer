# Generated by Django 2.0.5 on 2018-06-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0016_auto_20180621_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='icon',
            field=models.CharField(choices=[('community', 'LeafCommunity'), ('development', 'LeafDevelopment'), ('social', 'LeafSocial'), ('student-voice', 'LeafStudentVoice'), ('team-sussex', 'LeafTeamSussex')], default='community', max_length=24),
        ),
    ]