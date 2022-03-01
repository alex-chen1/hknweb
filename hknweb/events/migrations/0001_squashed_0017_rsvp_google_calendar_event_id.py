# Generated by Django 2.2.8 on 2022-02-28 20:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import markdownx.models


class Migration(migrations.Migration):

    replaces = [('events', '0001_initial'), ('events', '0002_auto_20171128_0556'), ('events', '0003_auto_20190213_0455'), ('events', '0004_auto_20190220_0617'), ('events', '0005_auto_20190220_0713'), ('events', '0006_event_rsvps'), ('events', '0007_auto_20190224_0149'), ('events', '0008_auto_20190227_0412'), ('events', '0009_rsvp_created_at'), ('events', '0010_auto_20190920_2346'), ('events', '0011_auto_20190921_0220'), ('events', '0012_remove_event_rsvps'), ('events', '0013_auto_20191008_2053'), ('events', '0014_eventtype_color'), ('events', '0015_auto_20201012_1603'), ('events', '0016_auto_20220227_2338'), ('events', '0017_rsvp_google_calendar_event_id')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hknweb', '0005_delete_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('color', models.CharField(default='#0072c1', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', markdownx.models.MarkdownxField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('rsvp_limit', models.PositiveIntegerField(blank=True, null=True)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventType')),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 9, 20, 23, 46, 7, 312109, tzinfo=utc))),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('access_level', models.IntegerField(choices=[(0, 'internal'), (1, 'candidate'), (2, 'external')], default=0)),
                ('google_calendar_event_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleCalendarCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'GoogleCalendarCredentials',
            },
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('comment', models.TextField(blank=True, default='')),
                ('confirmed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="rsvp'd by")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='rsvp time')),
                ('google_calendar_event_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]