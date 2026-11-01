# LedgerForge architecture

## Phase 1 boundary

The application currently contains the identity and tenancy foundation only. `accounts.User` is the project authentication model. `accounts.Company` is the tenant boundary, and `accounts.Membership` is the explicit authorization relationship between a user and a company. Business records added in later phases must carry a company foreign key and must be filtered through an authorized membership.

The dashboard derives its company list from active memberships and active companies; it does not trust a client-provided company identifier. Administrative setup is intentionally performed through Django admin until a tested company onboarding workflow is added.

## Planned layers

- **Web**: Django templates and server-rendered forms; HTMX may be introduced for targeted interactions.
- **API**: Django REST Framework endpoints with tenant-scoped queryset and permission classes. The current `/api/health/` endpoint is public; `/api/me/` requires Django session authentication.
- **Clients**: Tauri desktop shell for Windows and Expo/React Native shell for iPhone, both consuming the shared API.
- **Domain**: service functions for posting journals, stock movements, imports, and report queries. Financial mutations will use database transactions and append-only audit records.
- **Persistence**: PostgreSQL in production, SQLite for local development and tests. UUID identifiers are used for top-level identity and tenant records.
- **Operations**: Celery and Redis for resumable imports and scheduled work; these are not enabled until their domain contracts exist.

## Tenant isolation rules

1. Resolve the company from authenticated membership, never from an unverified request parameter.
2. Scope every business queryset to that company.
3. Check role/permission before reads and writes.
4. Add database constraints and service-level tests for cross-company access.
5. Keep audit history append-only for financial and permission changes.

## Phase roadmap

| Phase | Scope | Status |
|---|---|---|
| 1 | Identity, companies, memberships, auth, dashboard | Implemented |
| 2 | Accounts, periods, vouchers, posting, reports | Planned |
| 3 | Products, stock, purchasing, sales, invoices | Planned |
| 4 | Imports, barcodes, labels, exports | Planned |
| 5 | AI assistant, alerts, analytics, integrations | Planned |
| 6 | Security, performance, deployment, backup/restore | Planned |

## Initial file tree

```text
config/                 Django settings, URLs, and WSGI entry point
accounts/               User, Company, Membership, admin, views, tests, migration
templates/              Shared layout, login, and dashboard
docs/                   Architecture and roadmap documentation
Dockerfile              Container image
docker-compose.yml      Local web + PostgreSQL services
requirements.txt        Pinned Python dependencies
```
