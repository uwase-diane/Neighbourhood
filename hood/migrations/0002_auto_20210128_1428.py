# Generated by Django 3.1.5 on 2021-01-28 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='estate',
            new_name='neighbourhood',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='Neighbourhood',
            new_name='hood_location',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='Neighbourhood_location',
            new_name='hood_name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='estate',
            new_name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='business',
            name='image',
        ),
        migrations.RemoveField(
            model_name='business',
            name='project',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.profile'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='police_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(default='default.jpg', upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
