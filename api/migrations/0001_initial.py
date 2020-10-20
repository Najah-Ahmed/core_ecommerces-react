from django.db import migrations
from api.users.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="njh_admin",
                          email="najah_admin@app.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="777778",
                          gender="female"
                          )
        user.set_password("njh123")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
