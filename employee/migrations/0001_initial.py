# Generated by Django 4.2 on 2023-05-05 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('hire_data', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departament.departament')),
            ],
        ),
    ]
