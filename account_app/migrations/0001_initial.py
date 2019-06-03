# Generated by Django 2.1.4 on 2019-05-26 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created_at', models.DateField()),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('applinum', models.AutoField(primary_key=True, serialize=False)),
                ('appliname', models.CharField(max_length=40)),
                ('begintime', models.DateField()),
                ('endtime', models.DateField()),
                ('content', models.CharField(max_length=200)),
                ('state', models.IntegerField(choices=[(-1, '未通过'), (0, '待分配'), (1, '会签中'), (2, '审批中'), (3, '签订中'), (4, '签订完成')], default=0)),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('fieldnum', models.AutoField(primary_key=True, serialize=False)),
                ('fieldname', models.CharField(max_length=40)),
                ('category', models.CharField(default='', max_length=20)),
                ('addition', models.CharField(default='', max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('missionnum', models.IntegerField(choices=[(0, '分配'), (1, '会签'), (2, '审批'), (3, '签订')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('fun1', models.BooleanField(default=False)),
                ('fun2', models.BooleanField(default=False)),
                ('fun3', models.BooleanField(default=False)),
                ('fun4', models.BooleanField(default=False)),
                ('fun5', models.BooleanField(default=False)),
                ('fun6', models.BooleanField(default=False)),
                ('classfun', models.BooleanField(default=False)),
                ('sportfun', models.BooleanField(default=False)),
                ('gymfun', models.BooleanField(default=False)),
                ('firstfun', models.BooleanField(default=False)),
                ('secondfun', models.BooleanField(default=False)),
                ('thirdfun', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('applinum', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account_app.Application')),
                ('copinion1', models.CharField(default=None, max_length=100, null=True)),
                ('ctime1', models.DateTimeField(default=None, null=True)),
                ('copinion2', models.CharField(default=None, max_length=100, null=True)),
                ('ctime2', models.DateTimeField(default=None, null=True)),
                ('copinion3', models.CharField(default=None, max_length=100, null=True)),
                ('ctime3', models.DateTimeField(default=None, null=True)),
                ('call', models.IntegerField(default=3)),
                ('chas', models.IntegerField(default=0)),
                ('astate1', models.IntegerField(choices=[(0, '未审批'), (1, '拒绝'), (2, '通过')], default=0)),
                ('atime1', models.DateTimeField(default=None, null=True)),
                ('aopinion1', models.CharField(default=None, max_length=100, null=True)),
                ('astate2', models.IntegerField(choices=[(0, '未审批'), (1, '拒绝'), (2, '通过')], default=0)),
                ('atime2', models.DateTimeField(default=None, null=True)),
                ('aopinion2', models.CharField(default=None, max_length=100, null=True)),
                ('astate3', models.IntegerField(choices=[(0, '未审批'), (1, '拒绝'), (2, '通过')], default=0)),
                ('atime3', models.DateTimeField(default=None, null=True)),
                ('aopinion3', models.CharField(default=None, max_length=100, null=True)),
                ('aall', models.IntegerField(default=3)),
                ('ahas', models.IntegerField(default=0)),
                ('sinformation', models.CharField(default=None, max_length=100, null=True)),
                ('stime', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='applinum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account_app.Application'),
        ),
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='draft',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='fieldnum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account_app.Field'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account_app.Role'),
        ),
        migrations.AddField(
            model_name='administration',
            name='approval1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='a1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='administration',
            name='approval2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='a2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='administration',
            name='approval3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='a3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='administration',
            name='countersign1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='administration',
            name='countersign2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='administration',
            name='countersign3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='administration',
            name='sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
