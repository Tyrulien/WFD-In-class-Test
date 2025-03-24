# test_django.py
import django
from django.test import SimpleTestCase
from django.conf import settings

# Configure settings if not already configured.
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='a-very-secret-key',
        ROOT_URLCONF='django_app',  # This tells Django to use our django_app.py as the URL conf.
        ALLOWED_HOSTS=['*'],
        MIDDLEWARE=[
            'django.middleware.common.CommonMiddleware',
        ],
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.staticfiles',
        ),
    )
django.setup()

from django_app import index  # Import the view from our Django app.

class DjangoAppTests(SimpleTestCase):
    def test_index_view(self):
        """Test that the index view returns the expected content."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Status: Working", response.content.decode())

if __name__ == '__main__':
    # Run the tests when the file is executed.
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'test', '--verbosity=2'])
