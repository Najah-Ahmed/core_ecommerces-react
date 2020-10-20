from django.db import migrations
from api.users.models import CustomUser


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        user = CustomUser(name="",
                          email="",
                          is_staff=True,
                          is_superuser=True,
                          gender="female",
                          phone="5666666")
        user.set_password("")
        user.save()

    dependencies = []
    operations = [
        migrations.RunPython(seed_data,)
    ]
