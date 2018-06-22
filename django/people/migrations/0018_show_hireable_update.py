# Generated by Django 2.0.6 on 2018-06-22 09:54

from django.db import migrations


class Migration(migrations.Migration):


    def hireable_update(apps, schema_editor):
        People = apps.get_model('people', 'Person')
        for p in People.objects.all():
            if p.hireable and p.show_hireable :
                p.hireable = True
            else:
                p.hireable = False
            p.save()

    dependencies = [
        ('people', '0017_auto_20180622_1009'),
    ]

    operations = [
        migrations.RunPython(hireable_update)
    ]
