# Generated by Django 4.2.6 on 2023-10-27 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField(default='none')),
                ('fin_prdt_nm', models.TextField(default='none')),
                ('etc_note', models.TextField(default='none')),
                ('join_deny', models.IntegerField(default=-1)),
                ('join_member', models.TextField(default='none')),
                ('join_way', models.TextField(default='none')),
                ('spcl_cnd', models.TextField(default='none')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(default='none')),
                ('intr_rate_type_nm', models.CharField(default='none', max_length=100)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('save_trm', models.IntegerField(default=-1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='finlife.depositproducts')),
            ],
        ),
    ]