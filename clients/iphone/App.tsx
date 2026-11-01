import { StatusBar } from "expo-status-bar";
import { useEffect, useState } from "react";
import { Linking, Pressable, RefreshControl, SafeAreaView, ScrollView, StyleSheet, Text, View } from "react-native";

const apiUrl = process.env.EXPO_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

export default function App() {
  const [status, setStatus] = useState("Checking API...");
  const [refreshing, setRefreshing] = useState(false);

  const checkApi = async () => {
    setRefreshing(true);
    setStatus("Checking API...");
    try {
      const response = await fetch(`${apiUrl}/api/health/`);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data: { status?: string } = await response.json();
      setStatus(`API: ${data.status ?? "unknown"}`);
    } catch {
      setStatus("API unavailable. Configure EXPO_PUBLIC_API_URL.");
    } finally {
      setRefreshing(false);
    }
  };

  useEffect(() => {
    void checkApi();
  }, []);

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="dark" />
      <ScrollView refreshControl={<RefreshControl refreshing={refreshing} onRefresh={() => void checkApi()} />} contentContainerStyle={styles.content}>
        <Text style={styles.eyebrow}>LEDGERFORGE ERP</Text>
        <Text style={styles.title}>Your business, in one place.</Text>
        <Text style={styles.subtitle}>A focused workspace for companies, finance, inventory, and operations.</Text>
        <View style={styles.toolbar}>
          <Text accessibilityRole="status" style={styles.status}>{status}</Text>
          <Pressable style={styles.primaryButton} onPress={() => void Linking.openURL(`${apiUrl}/accounts/login/`)}>
            <Text style={styles.primaryButtonText}>Web sign-in</Text>
          </Pressable>
        </View>
        <View style={styles.card}><Text style={styles.cardTitle}>Companies</Text><Text style={styles.cardText}>Manage organizations and active team memberships.</Text><Text style={styles.badge}>FOUNDATION READY</Text></View>
        <View style={styles.card}><Text style={styles.cardTitle}>Accounting</Text><Text style={styles.cardText}>Double-entry accounting and financial reports are coming next.</Text><Text style={styles.badge}>COMING NEXT</Text></View>
        <View style={styles.card}><Text style={styles.cardTitle}>Operations</Text><Text style={styles.cardText}>Inventory, purchasing, sales, and invoicing will share this workspace.</Text><Text style={styles.badge}>ROADMAP</Text></View>
        <Text style={styles.footer}>Phase 1 foundation · iOS and Android</Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: "#f5f7fb" },
  content: { padding: 24, paddingTop: 48 },
  eyebrow: { color: "#1769aa", fontSize: 12, fontWeight: "800", letterSpacing: 2 },
  title: { marginTop: 8, fontSize: 32, fontWeight: "800", letterSpacing: -1, color: "#172033" },
  subtitle: { marginTop: 12, fontSize: 16, lineHeight: 24, color: "#596579" },
  toolbar: { marginTop: 28, marginBottom: 8, flexDirection: "row", alignItems: "center", justifyContent: "space-between", gap: 12 },
  status: { flex: 1, fontSize: 14, color: "#596579" },
  primaryButton: { paddingHorizontal: 14, paddingVertical: 10, borderRadius: 8, backgroundColor: "#1769aa" },
  primaryButtonText: { color: "#fff", fontWeight: "700" },
  card: { marginTop: 16, padding: 20, borderWidth: 1, borderColor: "#e1e7f0", borderRadius: 14, backgroundColor: "#fff" },
  cardTitle: { fontSize: 17, fontWeight: "700", color: "#172033" },
  cardText: { marginTop: 8, fontSize: 15, lineHeight: 22, color: "#596579" },
  badge: { alignSelf: "flex-start", marginTop: 16, paddingHorizontal: 9, paddingVertical: 5, borderRadius: 99, backgroundColor: "#eef2f7", color: "#69778b", fontSize: 11, fontWeight: "700" },
  footer: { marginTop: 28, color: "#7a8798", fontSize: 13 },
});
