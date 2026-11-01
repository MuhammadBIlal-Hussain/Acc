# LedgerForge ERP

LedgerForge is an independent, multi-company accounting and ERP application. It is not affiliated with or a reproduction of any existing accounting product.

## Phase 1 status

Implemented:

- Django 5.2 project with Python 3.12 baseline.
- Environment-based settings and SQLite development/PostgreSQL production support.
- Custom UUID user model with unique email addresses.
- Company and membership models with an enforced unique user/company relationship.
- Role vocabulary for owner, administrator, accountant, sales, purchase, inventory, cashier, and auditor.
- CSRF-protected login/logout, secure production cookie defaults, admin registration, and a tenant-aware dashboard.
- Dockerfile, Docker Compose PostgreSQL service, migrations, and focused tests.
- A shared authenticated Django REST API foundation with public health status and tenant-filtered `/api/me/`.
- Windows desktop client shell in `clients/windows` using Tauri.
- iPhone client shell in `clients/iphone` using Expo/React Native.

Not yet implemented: mobile authentication tokens, accounting posting, inventory, purchasing/sales, imports, barcode/QR, AI, reports, and cloud deployment. These are scheduled in the phased roadmap and are deliberately not represented as completed UI features.

## Windows PowerShell setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py makemigrations accounts
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Use `/admin/` to create a company and membership, then sign in.

## Docker

```powershell
Copy-Item .env.example .env
docker compose up --build
```

The local SQLite database is suitable for development only. Production requires PostgreSQL, HTTPS, managed secret storage, backups, monitoring, and a reviewed deployment configuration.

## Client apps

The shared API must be running before starting either client:

```powershell
python manage.py runserver
```

Windows desktop client:

```powershell
Set-Location clients\windows
npm install
npm run tauri dev
```

iPhone client:

```powershell
Set-Location clients\iphone
npm install
$env:EXPO_PUBLIC_API_URL = "http://192.168.1.10:8000"
npx expo start
```

Replace the example LAN address with the development computer's reachable address. Do not use `127.0.0.1` on a physical iPhone.

## Tests

```powershell
.\.venv\Scripts\Activate.ps1
pytest
```

## Roadmap

1. Foundation, tenancy, authentication, and dashboard.
2. Double-entry accounting and financial reports.
3. Inventory, purchasing, sales, invoicing, and returns.
4. Bulk operations, barcode/QR, labels, and exports.
5. Permission-aware AI assistant, alerts, analytics, and integrations.
6. Security review, performance testing, deployment, backup/restore, and complete documentation.
