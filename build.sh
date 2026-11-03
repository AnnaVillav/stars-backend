
#!/usr/bin/env bash
set -o errexit

uv sync --frozen --no-dev

uv run --no-sync python manage.py collectstatic --noinput

uv run --no-sync python manage.py migrate

PRODUCTOS=$(uv run --no-sync python manage.py shell -c "from tienda.models import Producto; print(Producto.objects.count())" | tail -n 1)

if [ "$PRODUCTOS" = "0" ]; then
    echo "Cargando catalogo inicial de STARS..."
    uv run --no-sync python manage.py loaddata catalogo_stars
else
    echo "El catalogo ya tiene productos. No se cargan datos duplicados."
fi


if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
    uv run --no-sync python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ['DJANGO_SUPERUSER_USERNAME']

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=os.environ.get('DJANGO_SUPERUSER_EMAIL', ''),
        password=os.environ['DJANGO_SUPERUSER_PASSWORD']
    )
    print('Administrador inicial creado.')
else:
    print('El administrador ya existe.')
"
fi