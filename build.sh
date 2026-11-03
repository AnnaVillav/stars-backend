
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