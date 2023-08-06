# Generated by Django 2.0.10 on 2020-08-20 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=None, max_length=30, null=True, validators=[
                                   django.core.validators.RegexValidator('^[0-9a-zA-Zㄱ-ㅣ가-힣]*$', '한글과 영숫자만 허용됩니다.')]),
        ),
    ]
