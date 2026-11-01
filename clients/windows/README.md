# LedgerForge Windows app

This directory is the Windows desktop client shell. It uses Tauri so the client can reuse a small web UI without bundling a second browser runtime. The shell calls the Django API at `http://127.0.0.1:8000/api/` during local development.

Install the prerequisites (Node.js, Rust, and the Tauri system dependencies), then run:

```powershell
npm install
npm run tauri dev
```

The client currently provides a starter dashboard, API health check, and a link to the web sign-in flow. ERP actions must not be added here until the corresponding tenant-scoped API endpoints exist.

The first build downloads Rust/Tauri crates and may take several minutes.
