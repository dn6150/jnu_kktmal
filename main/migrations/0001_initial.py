# Generated by Django 2.0.10 on 2019-02-09 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_name', models.CharField(
                    max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.TextField(null=True)),
                ('bot_message', models.TextField(null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('delay', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShiritalkMatch',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ShiritalkPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
                ('last_played', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(default=0)),
                ('match', models.ForeignKey(blank=True, null=True,
                                            on_delete=django.db.models.deletion.SET_NULL, to='main.ShiritalkMatch')),
            ],
        ),
        migrations.CreateModel(
            name='ShiritalkWord',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('match', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.ShiritalkMatch')),
                ('player', models.ForeignKey(blank=True, null=True,
                                             on_delete=django.db.models.deletion.SET_NULL, to='main.ShiritalkPlayer')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(
                    default=None, max_length=30, null=True)),
                ('user_key', models.CharField(
                    max_length=30, primary_key=True, serialize=False)),
                ('mail_check', models.BooleanField(default=False)),
                ('state', models.CharField(default='home', max_length=20)),
                ('group', models.ForeignKey(default=None, null=True,
                                            on_delete=django.db.models.deletion.CASCADE, to='main.Group')),
            ],
        ),
        migrations.AddField(
            model_name='shiritalkplayer',
            name='user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='shiritalkmatch',
            name='last_word',
            field=models.OneToOneField(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ShiritalkWord'),
        ),
        migrations.AddField(
            model_name='mail',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='mail_set_receiver', to='main.User'),
        ),
        migrations.AddField(
            model_name='mail',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='mail_set_sender', to='main.User'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
