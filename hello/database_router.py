from django.conf import settings
from  settings import DATABASE_APPS_MAPPING
DATABASE_MAPPING = DATABASE_APPS_MAPPING
class movieDB:

    def db_for_read(self, model, **hints):

        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):

        """
        Allow relations if a model in the auth app is involved.
        """
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
           if db_obj1 == db_obj2:
               return True
           else:
               return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        print db, app_label, model_name, hints

        if db in DATABASE_MAPPING.values():

            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:

            return False
        return None


