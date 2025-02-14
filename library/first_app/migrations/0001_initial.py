# Generated by Django 4.2.10 on 2024-02-25 15:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('publishing_year', models.DateField()),
                ('cipher', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('education', models.CharField(choices=[('0', 'pre-elementary'), ('1', 'elementary'), ('2', 'middle'), ('3', 'secondary'), ('4', 'professional'), ('5', 'bachelor'), ('6', 'master')], default='0', max_length=1)),
                ('if_phd', models.BooleanField()),
                ('library_card_number', models.CharField(max_length=10)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.book')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(default=datetime.datetime(2024, 2, 25, 18, 41, 29, 297133))),
                ('date_returned', models.DateField(blank=True, default=None, null=True)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.copy')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.reader')),
            ],
        ),
    ]
