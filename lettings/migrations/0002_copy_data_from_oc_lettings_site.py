from django.db import migrations


def copy_address_and_letting_data(apps, schema_editor):
    """
    Copy data from the source application's Address and Letting models into
    the new Address and Letting models of the `lettings` application.
    This migration uses Django historical models obtained via
    `apps.get_model(...)`, which is the recommended approach for data
    migrations.
    Args:
        apps: django.apps.registry.Apps, historical app registry provided by
        Django migrations.
        schema_editor: BaseDatabaseSchemaEditor, schema editor used by the
        migration system.
    """
    source_address_model = apps.get_model("oc_lettings_site", "Address")
    source_letting_model = apps.get_model("oc_lettings_site", "Letting")
    target_address_model = apps.get_model("lettings", "Address")
    target_letting_model = apps.get_model("lettings", "Letting")

    database = schema_editor.connection.alias
    address_mapping = {}

    for source_address in source_address_model.objects.using(database).all():
        target_address = target_address_model.objects.using(database).create(
            number=source_address.number,
            street=source_address.street,
            city=source_address.city,
            state=source_address.state,
            zip_code=source_address.zip_code,
            country_iso_code=source_address.country_iso_code,
        )
        address_mapping[source_address.pk] = target_address

    for source_letting in source_letting_model.objects.using(database).all():
       target_letting = target_letting_model.objects.using(database).create(
            title=source_letting.title,
            address=address_mapping[source_letting.address_id]
        )


def reverse_copy_address_and_letting_data(apps, schema_editor):
    """
    Delete copied records when rolling back migration.
    Args:
        apps: django.apps.registry.Apps, historical app registry provided by
        Django migrations.
        schema_editor: BaseDatabaseSchemaEditor, schema editor used by the
        migration system.
    """
    target_address_model = apps.get_model("lettings", "Address")
    target_letting_model = apps.get_model("lettings", "Letting")

    database = schema_editor.connection.alias

    target_address_model.objects.using(database).all().delete()
    target_letting_model.objects.using(database).all().delete()


class Migration(migrations.Migration):
    """
    Data migration that copies Address and Letting records from source
    application to 'lettings' new application.
    """
    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_address_and_letting_data,
            reverse_copy_address_and_letting_data
        )
    ]
