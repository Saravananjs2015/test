# Generated by Django 2.2.4 on 2019-08-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fintab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('midname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('companyname', models.CharField(max_length=100)),
                ('cityname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('psw', models.CharField(max_length=100)),
                ('pswrpt', models.CharField(max_length=100)),
                ('crd', models.CharField(max_length=25)),
                ('protype', models.CharField(default='InvestPro', max_length=25)),
                ('member', models.CharField(default='August 2019', max_length=25)),
            ],
        ),
    ]