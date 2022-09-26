from django.apps import AppConfig


class JwtauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jwtAuth'
    
    def ready(self) -> None:
        import jwtAuth.signals
