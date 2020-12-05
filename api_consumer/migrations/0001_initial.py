
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LaunchesSpaceX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_name', models.TextField()),
                ('launch_success', models.BooleanField(default=True)),
                ('upcoming', models.BooleanField(default=False)),
                ('launch_site', models.TextField()),
                ('rocket_name', models.TextField()),
                ('yt_video_link', models.CharField(max_length=25)),
            ],
        ),
    ]
