# Generated by Django 3.1.6 on 2021-02-16 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companies',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=300, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='employers',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.companies')),
            ],
        ),
        migrations.CreateModel(
            name='employer_profile',
            fields=[
                ('emp_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employers')),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'others')], max_length=10)),
                ('address', models.CharField(blank=True, max_length=600)),
                ('mobile_no', models.CharField(blank=True, max_length=13)),
                ('joining_date', models.DateField()),
                ('company_id', models.CharField(max_length=10, null=True)),
                ('project_id', models.CharField(max_length=10)),
                ('department_id', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='company_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=600)),
                ('established_year', models.CharField(max_length=4)),
                ('ceo', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=13)),
                ('gst_no', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('company_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.companies')),
            ],
        ),
    ]
