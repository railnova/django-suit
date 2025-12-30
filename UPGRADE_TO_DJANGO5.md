# Django Suit - Upgrade Guide to Django 5.x

This guide outlines the changes made to upgrade Django Suit to Django 5.x compatibility.

## Requirements

- **Django**: 5.0 or 5.1
- **Python**: 3.10, 3.11, or 3.12

## Major Changes

### 1. Django Version
The minimum supported Django version is now **5.0**. Django Suit no longer supports Django versions below 5.0.

### 2. Python Version
Due to Django 5.x requirements, Python 3.10+ is now required. Python 2.7 and Python 3.4-3.9 are no longer supported.

## Breaking Changes

### URL Configuration
The URL configuration has been updated to use the modern Django URL patterns:

**Old (Django < 2.0):**
```python
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```

**New (Django 5.x):**
```python
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Use re_path for regex patterns
    re_path(r'^some-regex/$', view),
]
```

### Translation Functions
The deprecated `ugettext_lazy` has been replaced with `gettext_lazy`:

**Old:**
```python
from django.utils.translation import ugettext_lazy as _
```

**New:**
```python
from django.utils.translation import gettext_lazy as _
```

### Model Methods
`__unicode__` methods have been replaced with `__str__` (Python 3 standard):

**Old:**
```python
def __unicode__(self):
    return self.name
```

**New:**
```python
def __str__(self):
    return self.name
```

### ForeignKey Fields
All ForeignKey fields now require the `on_delete` parameter (mandatory since Django 2.0):

**Old:**
```python
country = models.ForeignKey(Country, null=True, blank=True)
```

**New:**
```python
country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
```

### Middleware Configuration
`MIDDLEWARE_CLASSES` has been replaced with `MIDDLEWARE`:

**Old:**
```python
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    # ...
]
```

**New:**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ...
]
```

Also note that `SessionAuthenticationMiddleware` has been removed (it was deprecated in Django 1.10 and removed in Django 2.0).

### App Configuration
The `default_app_config` variable has been removed from `__init__.py` files as it was deprecated in Django 3.2 and removed in Django 4.0.

Instead, ensure your app's `apps.py` has the proper configuration and is listed in `INSTALLED_APPS` using the dotted path if needed.

## Code Cleanup

### Python 2/3 Compatibility
All Python 2 compatibility code has been removed since Django 5.x only supports Python 3.10+.

### Django Version Checks
Removed version checks for Django < 1.9, including:
- `assignment_tag` vs `simple_tag` conditionals
- Old URL resolver imports

## Migration Steps

1. **Update Dependencies:**
   ```bash
   pip install 'Django>=5.0,<5.2'
   ```

2. **Update Your URLconf:**
   - Replace `from django.conf.urls import url` with `from django.urls import path, re_path`
   - Convert simple patterns to use `path()` instead of `url()`
   - Use `re_path()` for regex patterns

3. **Update Settings:**
   - Change `MIDDLEWARE_CLASSES` to `MIDDLEWARE`
   - Remove `SessionAuthenticationMiddleware` if present

4. **Update Models:**
   - Add `on_delete` parameter to all ForeignKey and OneToOneField fields
   - Replace `__unicode__` with `__str__`

5. **Update Translation Imports:**
   - Replace `ugettext_lazy` with `gettext_lazy`
   - Replace `ugettext` with `gettext`

6. **Remove App Config:**
   - Remove `default_app_config` from `__init__.py` files

7. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Test Thoroughly:**
   Run your test suite to ensure everything works correctly with Django 5.x.

## Additional Notes

- The upgrade maintains backward compatibility in URL resolvers (try/except blocks for imports)
- All template tags have been updated to use `simple_tag` instead of the deprecated `assignment_tag`
- Static file handling remains unchanged

## References

- [Django 5.0 Release Notes](https://docs.djangoproject.com/en/5.0/releases/5.0/)
- [Django 5.1 Release Notes](https://docs.djangoproject.com/en/5.1/releases/5.1/)
- [Django Deprecation Timeline](https://docs.djangoproject.com/en/5.0/internals/deprecation/)
