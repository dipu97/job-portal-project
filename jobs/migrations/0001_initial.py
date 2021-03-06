# Generated by Django 2.2.10 on 2020-12-23 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=25)),
                ('link', models.CharField(max_length=150)),
                ('cv', models.FileField(upload_to='')),
                ('cover', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=200)),
                ('nature', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=150)),
                ('job_type', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='photos/logo/%y/%m/%d')),
                ('experience', models.CharField(max_length=200)),
                ('expired_date', models.DateTimeField()),
                ('qualification', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('is_published', models.BooleanField()),
                ('vacency', models.DecimalField(decimal_places=0, max_digits=4)),
                ('published_date', models.DateTimeField()),
                ('update', models.DateTimeField(auto_now_add=True, null=True)),
                ('responsibilities', models.TextField()),
                ('benefit', models.TextField()),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Employee.Employee')),
            ],
            options={
                'ordering': ('-published_date',),
            },
        ),
    ]
