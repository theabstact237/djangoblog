from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

class ProfilesConfig(AppConfig):
    name = 'profiles'
 
    def ready(self):
        import profiles.signals