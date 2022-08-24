from django.db import models


class Application(models.Model):
    """
    Model that stores Application information.
    """
    
    name = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


class Configuration(models.Model):
    """
    Model that stores Configurations and history.
    """

    CONFIGURATION_TYPES = (
        ('meta', 'Metadata'),
        ('tech', 'Technical Data')
    )

    type_choice = models.CharField(
        max_length=4, 
        choices=CONFIGURATION_TYPES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    roles_set = models.JSONField(default=dict)
    history_log = models.JSONField(default=list)

    application = models.ForeignKey(
        Application, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{type_choice}-{application_name}'.format(
            type_choice=self.type_choice, 
            application_name=self.application.name
        )
    
    def __to_dict__(self):
        return {
            'type_choice': self.type_choice,
            'created_at': self.created_at.strftime('%m.%d.%Y, %H:%M:%S'),
            'application': self.application.pk
        }
