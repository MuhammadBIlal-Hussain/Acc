# LedgerForge mobile app

This directory contains an Expo/React Native client shell for iPhone and Android. It uses the shared Django API and intentionally exposes the Phase 1 starter dashboard until mobile authentication and tenant-scoped ERP endpoints are implemented.

```powershell
npm install
npx expo start
```

Set `EXPO_PUBLIC_API_URL` to the reachable API URL for a physical device. `127.0.0.1` refers to the phone itself, not the development computer.

Use `npx expo start --android` for Android or `npx expo start --ios` for iPhone. The two platforms share the same app entry point and API behavior.
