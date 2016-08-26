# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-23 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0020_thumbnail_move4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorentriesplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_blog_authorentriesplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='genericblogplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_blog_genericblogplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='latestpostsplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_blog_latestpostsplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image_full',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_full', to='filer.ThumbnailOption', verbose_name='main image full'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image_thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_thumbnail', to='filer.ThumbnailOption', verbose_name='main image thumbnail'),
        ),
    ]