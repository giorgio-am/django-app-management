from django.db import models
from django.db import models
from django.utils.html import mark_safe, format_html


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


# class StaffAdmin(admin.ModelAdmin):
#
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(user=request.user)




class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clasificacin(models.Model):
    def __str__(self):
        template = f'{self.clasificación}'
        return template.format(self)

    id_clasificación = models.AutoField(primary_key=True)
    clasificación = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clasificación'


class Derpartamentos(models.Model):

    def __str__(self):
        template = f'{self.nombre_dpto}'
        return template.format(self)

    id_dpto = models.AutoField(primary_key=True)
    nombre_dpto = models.CharField(max_length=100, blank=True, null=True)
    subdirección = models.ForeignKey('Subdirecciones', models.DO_NOTHING, db_column='subdirección', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'derpartamentos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estados(models.Model):
    def __str__(self):
        template = f'{self.estado}'
        return template.format(self)

    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    descripcion_estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


# class FichasProcesos(models.Model):
#     nombre_proceso = models.CharField(max_length=100, blank=True, null=True)
#     alcance = models.CharField(max_length=100, blank=True, null=True)
#     dpto_responsable = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='dpto_responsable', blank=True, null=True)
#     dueño_proceso = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='dueño_proceso', blank=True, null=True)
#     cliente_proceso = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='cliente_proceso', blank=True, null=True)
#     proveedor_proceso = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='proveedor_proceso', blank=True, null=True)
#     kpi = models.ForeignKey('Kpi', models.DO_NOTHING, db_column='kpi', blank=True, null=True)
#     meta_indicador = models.ForeignKey('Kpi', models.DO_NOTHING, db_column='meta_indicador', blank=True, null=True)
#     controles = models.ForeignKey('Riesgos', models.DO_NOTHING, db_column='controles', blank=True, null=True)
#     riesgos = models.ForeignKey('Riesgos', models.DO_NOTHING, db_column='riesgos', blank=True, null=True)
#     flujo = models.CharField(max_length=100, blank=True, null=True)
#     subprocesos = models.ForeignKey('Subprocesos', models.DO_NOTHING, db_column='subprocesos', blank=True, null=True)
#     documento = models.CharField(max_length=100, blank=True, null=True)
#     estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='estado', blank=True, null=True)
#     madurez = models.ForeignKey('Madurez', models.DO_NOTHING, db_column='madurez')
#     clasificación_interna = models.ForeignKey(Clasificacin, models.DO_NOTHING, db_column='clasificación_interna', blank=True, null=True)
#     clasificación_general = models.ForeignKey(Clasificacin, models.DO_NOTHING, db_column='clasificación_general', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'fichas_procesos'


class Kpi(models.Model):

    def __str__(self):
        template = f'{self.nombre_kpi}'
        return template.format(self)

    id_kpi = models.AutoField(primary_key=True)
    nombre_kpi = models.CharField(max_length=100, blank=True, null=True)
    meta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    descripcion_meta = models.CharField(max_length=100, blank=True, null=True)
    periodicidad = models.ForeignKey('Periodicidad', models.DO_NOTHING, db_column='periodicidad', blank=True, null=True)
    proceso = models.CharField(max_length=100, blank=True, null=True)
    descripcion_indicador = models.CharField(max_length=100, blank=True, null=True)
    parametros = models.ForeignKey('Parametros', models.DO_NOTHING, db_column='parametros', blank=True, null=True)
    formula = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpi'


class Ley18834(models.Model):

    def __str__(self):
        template = f'{self.establecimiento}, {self.ano}, {self.indicador}, {self.trimestre}'
        return template.format(self)



    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    trimestre = models.IntegerField(db_column='Trimestre')  # Field name made lowercase.
    establecimiento = models.CharField(db_column='Establecimiento', max_length=100)  # Field name made lowercase.
    indicador = models.CharField(db_column='Indicador', max_length=100)  # Field name made lowercase.
    meta = models.DecimalField(db_column='Meta', max_digits=65535, decimal_places=2, blank=False, null=True)  # Field name made lowercase.
    numerador = models.DecimalField(db_column='Numerador', max_digits=65535, decimal_places=2, blank=False, null=True)  # Field name made lowercase.
    denominador = models.DecimalField(db_column='Denominador', max_digits=65535, decimal_places=2, blank=False, null=True)  # Field name made lowercase.
    resultado = models.CharField(db_column='Resultado', max_length=100, blank=False, null=True)  # Field name made lowercase.
    cumplimiento = models.CharField(db_column='Cumplimiento', max_length=100, blank=False, null=True)  # Field name made lowercase.
    ponderador = models.CharField(db_column='Ponderador', max_length=100, blank=False, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ley_18834'
        unique_together = ('ano', 'trimestre', 'establecimiento', 'indicador')


class Madurez(models.Model):
    def __str__(self):
        template = f'{self.grado_madurez}'
        return template.format(self)

    id_madurez = models.AutoField(primary_key=True)
    grado_madurez = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'madurez'


class Parametros(models.Model):
    id_parametro = models.AutoField(primary_key=True)
    id_kpi = models.IntegerField()
    proceso = models.CharField(max_length=100, blank=True, null=True)
    valor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    periodo = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros'


class Periodicidad(models.Model):
    id_periodicidad = models.AutoField(primary_key=True)
    periodicidad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodicidad'


class RegistroResultados(models.Model):
    id_kpi = models.ForeignKey(Kpi, models.DO_NOTHING, db_column='id_kpi')
    nombre_kpi = models.CharField(max_length=100, blank=True, null=True)
    periodicidad = models.CharField(max_length=100, blank=True, null=True)
    periodo = models.CharField(max_length=100, blank=True, null=True)
    resultado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    meta = models.CharField(max_length=100, blank=True, null=True)
    cumplimiento = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_resultados'


class Riesgos(models.Model):
    id_riesgo = models.AutoField(primary_key=True)
    nombre_riesgo = models.CharField(max_length=100, blank=True, null=True)
    descripcion_riesgo = models.CharField(max_length=100, blank=True, null=True)
    periodo = models.CharField(max_length=100, blank=True, null=True)
    controles = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='departamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riesgos'


class Subdirecciones(models.Model):

    def __str__(self):
        template = f'{self.nombre_subdireccion}'
        return template.format(self)

    id_subdireccion = models.AutoField(primary_key=True)
    nombre_subdireccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subdirecciones'

class Subprocesos(models.Model):
    id_subproceso = models.AutoField(primary_key=True)
    nombre_subproceso = models.CharField(max_length=100, blank=True, null=True)
    proceso_padre = models.ForeignKey('FichasProcesos', models.DO_NOTHING, db_column='proceso_padre', blank=True, null=True, related_name='+')
    flujo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subprocesos'

class Macroprocesos(models.Model):
    id_macroproceso = models.AutoField(primary_key=True)
    nombre_macroproceso = models.CharField(max_length=100, blank=True, null=True)
    procesos_hijo = models.ForeignKey('FichasProcesos', models.DO_NOTHING, db_column='proceso_padre', blank=True, null=True, related_name='+')
    flujo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'macroprocesos'


# Create your models here.
class FichasProcesos(models.Model):

    def __str__(self):
        template = f'{self.nombre_proceso}'
        return template.format(self)


    def flujo_preview(self):
        return format_html('<a href="{0}"><img src="{0}" width = "120" height = "120"></a>', self.flujo.url)
    flujo_preview.allow_tags = True
    flujo_preview.short_description = 'y-Image'


    nombre_proceso = models.CharField(max_length=100, blank=True, null=True)
    alcance = models.CharField(max_length=100, blank=True, null=True)
    dpto_responsable = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='dpto_responsable', blank=True, null=True, related_name='+')
    dueño_proceso = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='dueño_proceso', blank=True, null=True, related_name='+')
    cliente_proceso = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='cliente_proceso', blank=True, null=True, related_name='+')
    proveedor_proceso = models.ForeignKey(Derpartamentos, models.DO_NOTHING, db_column='proveedor_proceso', blank=True, null=True, related_name='+')
    kpi = models.ForeignKey('Kpi', models.DO_NOTHING, db_column='kpi', blank=True, null=True, related_name='+')
    meta_indicador = models.ForeignKey('Kpi', models.DO_NOTHING, db_column='meta_indicador', blank=True, null=True, related_name='+')
    controles = models.ForeignKey('Riesgos', models.DO_NOTHING, db_column='controles', blank=True, null=True)
    riesgos = models.ForeignKey('Riesgos', models.DO_NOTHING, db_column='riesgos', blank=True, null=True, related_name='+')
    flujo = models.ImageField(upload_to='staticfiles', null=True, blank=True)
    subprocesos = models.ManyToManyField('Subprocesos', blank=True, null=True, related_name='+')
    documento = models.CharField(max_length=100, blank=True, null=True)
    estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='estado', blank=True, null=True)
    madurez = models.ForeignKey('Madurez', models.DO_NOTHING, db_column='madurez', default=1)
    clasificación_interna = models.ForeignKey(Clasificacin, models.DO_NOTHING, db_column='clasificación_interna', blank=True, null=True, related_name='+')
    clasificación_general = models.ForeignKey(Clasificacin, models.DO_NOTHING, db_column='clasificación_general', blank=True, null=True, related_name='+')
    subdirección = models.ForeignKey('Subdirecciones', models.DO_NOTHING, db_column='subdirección', blank=True, null=True)
    macroproceso_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='macroproceso_padre', blank=True, null=True, related_name='hijos')



    class Meta:
        managed = True
        db_table = 'fichas_procesos'


