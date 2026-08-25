import pymysql

pymysql.install_as_MySQLdb()

# Full compatibility patch for XAMPP MariaDB 10.4.32 with Django 6.1
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.backends.mysql.features import DatabaseFeatures

BaseDatabaseWrapper.check_database_version_supported = lambda self: None

DatabaseFeatures.is_mariadb_10_5 = False
DatabaseFeatures.has_native_uuid_field = False
DatabaseFeatures.can_return_columns_from_insert = False
DatabaseFeatures.can_return_rows_from_bulk_insert = False
DatabaseFeatures.supports_comments = False
DatabaseFeatures.supports_comments_inline = False
DatabaseFeatures.supports_rename_column = False

def _forced_rename_field_sql(self, table, old_field, new_field, new_type):
    return "ALTER TABLE %s CHANGE %s %s %s" % (
        self.quote_name(table),
        self.quote_name(old_field.column),
        self.quote_name(new_field.column),
        new_type,
    )

BaseDatabaseSchemaEditor._rename_field_sql = _forced_rename_field_sql
