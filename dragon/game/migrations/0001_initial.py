# Generated by Django 2.2.1 on 2019-05-10 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalNum', models.IntegerField()),
                ('answerNum', models.IntegerField()),
            ],
        ),
    ]