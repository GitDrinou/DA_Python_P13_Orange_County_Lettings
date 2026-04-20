from django.db import migrations


def copy_profile_data(apps, schema_editor):
    """
    Copy data from the source application's Profile model into
    the new Profile model of the `profiles` application.
    This migration uses Django historical models obtained via
    `apps.get_model(...)`, which is the recommended approach for data
    migrations.
    Args:
        apps: django.apps.registry.Apps, historical app registry provided by
        Django migrations.
        schema_editor: BaseDatabaseSchemaEditor, schema editor used by the
        migration system.
    """
    source_profile_model = apps.get_model("oc_lettings_site", "Profile")
    target_profile_model = apps.get_model("profiles", "Profile")

    database = schema_editor.connection.alias

    for source_profile in source_profile_model.objects.using(database).all():
        target_profile = target_profile_model.objects.using(database).create(
            user_id=source_profile.user_id,
            favorite_city=source_profile.favorite_city,
        )


def reverse_copy_profile_data(apps, schema_editor):
    """
    Delete copied records when rolling back migration.
    Args:
        apps: django.apps.registry.Apps, historical app registry provided by
        Django migrations.
        schema_editor: BaseDatabaseSchemaEditor, schema editor used by the
        migration system.
    """
    target_profile_model = apps.get_model("profiles", "Profile")

    database = schema_editor.connection.alias

    target_profile_model.objects.using(database).all().delete()


class Migration(migrations.Migration):
    """
    Data migration that copies Profile records from source
    application to 'profiles' new application.
    """
    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_profile_data,
            reverse_copy_profile_data
        )
    ]
