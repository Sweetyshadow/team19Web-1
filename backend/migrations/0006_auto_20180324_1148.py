# Generated by Django 2.0.3 on 2018-03-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20180323_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='dockerserver',
            name='team1',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dockerserver',
            name='team2',
            field=models.IntegerField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='teaminfo',
            name='score',
            field=models.CharField(default='[{"score":50}]', max_length=8000),
        ),
    ]
