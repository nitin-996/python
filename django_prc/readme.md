# Django

 [w3school](https://www.w3schools.com/django/django_admin_create_user.php)

 # object create in django

 [one method needs to be save using save() function other method directly save it to db](https://stackoverflow.com/questions/26672077/django-model-vs-model-objects-create)

# models in django (it means database)

In Django, models are used to define the structure and behavior of the database tables. Here are some important points about Django models:

1. **Model Definition:**
   - A model in Django is a Python class that subclasses `django.db.models.Model`.
   - Each model class represents a database table, and each attribute of the class corresponds to a field in the table.

2. **Fields:**
   - Django provides various field types (e.g., `CharField`, `IntegerField`, `DateField`) to define different types of data that can be stored in the database.
   - Field options allow you to define constraints, default values, and other properties.

3. **Primary Key:**
   - By default, Django automatically adds an integer field named `id` as the primary key for each model unless specified otherwise.

4. **Relationships:**
   - Django supports relationships between models, such as `ForeignKey` for many-to-one relationships and `ManyToManyField` for many-to-many relationships.
   - Relationships are defined using the `related_name` and `on_delete` attributes.

5. **Model Instances:**
   - Instances of a model represent individual records in the database.
   - You can create, update, and delete records using model instances.

6. **Querying:**
   - Django provides a powerful query API to retrieve and filter data from the database using the `objects` attribute of a model.
   - Common methods include `filter()`, `get()`, and `exclude()`.

7. **Migrations:**
   - Changes to models are managed through migrations.
   - Migrations allow you to evolve the database schema over time, reflecting changes in your models.

8. **Admin Interface:**
   - Django provides a built-in admin interface that allows you to manage model data through a web interface.
   - The admin interface is customizable and can be extended to suit specific needs.

9. **Validation:**
   - Models include built-in validation for fields, ensuring that data entered into the database meets specified criteria.
   - Custom validation can be added using the `clean()` method.

10. **Signals:**
    - Django signals allow decoupled applications to get notified when certain actions occur elsewhere in the application.
    - Common signals include `pre_save`, `post_save`, and `pre_delete`.

11. **Model Managers:**
    - Model managers are used to encapsulate complex queries or provide additional methods for working with model instances.
    - The default manager is named `objects`, and you can create custom managers as needed.

12. **Abstract Models:**
    - Abstract models provide a way to factor out common fields and behavior from multiple models.
    - Abstract models are not created as database tables; they are used to factor out code and fields.

Understanding and effectively using Django models is crucial for building robust and scalable web applications. They serve as a bridge between your application's code and the underlying database, providing a high-level and Pythonic way to interact with data.

