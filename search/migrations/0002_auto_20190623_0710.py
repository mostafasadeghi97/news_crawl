# Generated by Django 2.2.1 on 2019-06-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='docfrequency',
            name='num_docs',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='docfrequency',
            name='term',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='termfrequency',
            name='frequency',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='termfrequency',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='termfrequency',
            name='term',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
