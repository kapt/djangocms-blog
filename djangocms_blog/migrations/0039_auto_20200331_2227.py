# Generated by Django 2.2.11 on 2020-03-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0038_post_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategorytranslation',
            name='name',
            field=models.CharField(max_length=752, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='blogcategorytranslation',
            name='slug',
            field=models.SlugField(blank=True, max_length=752, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=752, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='title',
            field=models.CharField(max_length=752, verbose_name='title'),
        ),
    ]