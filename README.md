# simple-notes-manager-226133-226142

Backend: Django REST API for managing notes.
- Docs: /docs (Swagger UI)
- Health: /api/health/
- Notes list/create: /api/notes/
- Note detail: /api/notes/{id}/

Run (port 3001 is configured by the environment in this workspace):
- Apply migrations: python manage.py migrate
- Seed data (optional): python manage.py seed_notes
- Start server: python manage.py runserver 0.0.0.0:3001

Query examples:
/api/notes/?search=todo&ordering=-updated_at&page=1&page_size=5