# Generated by Django 4.0.4 on 2022-05-21 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clasificacin',
            fields=[
                ('id_clasificación', models.AutoField(primary_key=True, serialize=False)),
                ('clasificación', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'clasificación',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Derpartamentos',
            fields=[
                ('id_dpto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_dpto', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'derpartamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_estado', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'estados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kpi',
            fields=[
                ('id_kpi', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_kpi', models.CharField(blank=True, max_length=100, null=True)),
                ('meta', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('descripcion_meta', models.CharField(blank=True, max_length=100, null=True)),
                ('proceso', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_indicador', models.CharField(blank=True, max_length=100, null=True)),
                ('formula', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'kpi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ley18834',
            fields=[
                ('ano', models.IntegerField(db_column='Ano', primary_key=True, serialize=False)),
                ('trimestre', models.IntegerField(db_column='Trimestre')),
                ('establecimiento', models.CharField(db_column='Establecimiento', max_length=100)),
                ('indicador', models.CharField(db_column='Indicador', max_length=100)),
                ('meta', models.DecimalField(blank=True, db_column='Meta', decimal_places=65535, max_digits=65535, null=True)),
                ('numerador', models.DecimalField(blank=True, db_column='Numerador', decimal_places=65535, max_digits=65535, null=True)),
                ('denominador', models.DecimalField(blank=True, db_column='Denominador', decimal_places=65535, max_digits=65535, null=True)),
                ('resultado', models.CharField(blank=True, db_column='Resultado', max_length=100, null=True)),
                ('cumplimiento', models.CharField(blank=True, db_column='Cumplimiento', max_length=100, null=True)),
                ('ponderador', models.CharField(blank=True, db_column='Ponderador', max_length=100, null=True)),
            ],
            options={
                'db_table': 'ley_18834',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Madurez',
            fields=[
                ('id_madurez', models.AutoField(primary_key=True, serialize=False)),
                ('grado_madurez', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'madurez',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id_parametro', models.AutoField(primary_key=True, serialize=False)),
                ('id_kpi', models.IntegerField()),
                ('proceso', models.CharField(blank=True, max_length=100, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('periodo', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'parametros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periodicidad',
            fields=[
                ('id_periodicidad', models.AutoField(primary_key=True, serialize=False)),
                ('periodicidad', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'periodicidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistroResultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_kpi', models.CharField(blank=True, max_length=100, null=True)),
                ('periodicidad', models.CharField(blank=True, max_length=100, null=True)),
                ('periodo', models.CharField(blank=True, max_length=100, null=True)),
                ('resultado', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('meta', models.CharField(blank=True, max_length=100, null=True)),
                ('cumplimiento', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'registro_resultados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Riesgos',
            fields=[
                ('id_riesgo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_riesgo', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_riesgo', models.CharField(blank=True, max_length=100, null=True)),
                ('periodo', models.CharField(blank=True, max_length=100, null=True)),
                ('controles', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'riesgos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subdirecciones',
            fields=[
                ('id_subdireccion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_subdireccion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'subdirecciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subprocesos',
            fields=[
                ('id_subproceso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_subproceso', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_proceso', models.CharField(blank=True, max_length=100, null=True)),
                ('flujo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'subprocesos',
                'managed': False,
            },
        ),
    ]
