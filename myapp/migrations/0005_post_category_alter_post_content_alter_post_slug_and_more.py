# Generated by Django 4.0.4 on 2022-05-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack')], default='Frontend', max_length=9),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.SlugField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=9),
        ),
    ]