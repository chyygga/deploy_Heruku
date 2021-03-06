# Generated by Django 4.0.4 on 2022-05-13 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU_Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GPU_Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('mail', models.EmailField(max_length=255, unique=True, verbose_name='Ваша эл. почта')),
                ('phone', models.IntegerField(unique=True, verbose_name='Номер тел.')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('agree', models.BooleanField(default=True, verbose_name='Подтвердить условия')),
                ('CPU_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='info.cpu_vendors', verbose_name='Производитель ЦП')),
                ('GPU_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='info.gpu_vendors', verbose_name='Производитель ГПУ')),
            ],
        ),
    ]
