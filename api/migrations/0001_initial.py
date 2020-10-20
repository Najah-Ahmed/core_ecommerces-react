from django.db import migrations
from api.users.models import CustomUser


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        user = CustomUser(name="najah_admin",
                          email="najah_admin@app.co",
                          is_staff=True,
                          is_superuser=True,
                          gender="female",
                          phone="5666666")
        user.set_password("njh123")
        user.save()

    dependencies = []
    operations = [
        migrations.RunPython(seed_data,)
    ]
