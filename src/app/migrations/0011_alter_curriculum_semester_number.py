# Generated by Django 3.2.9 on 2022-11-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_auto_20220419_1359"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curriculum",
            name="semester_number",
            field=models.JSONField(default=list, verbose_name="семестр"),
        ),
    ]