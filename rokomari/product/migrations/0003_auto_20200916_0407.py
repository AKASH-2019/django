# Generated by Django 3.0.7 on 2020-09-16 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='publication',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='publication'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='writer'),
        ),
    ]
