import { useState } from "react";

const PW = "Liverpool2026";
const f = "'Montserrat', 'Helvetica Neue', Arial, sans-serif";
const mono = "'IBM Plex Mono', 'SF Mono', monospace";

const PasswordGate = ({ onUnlock }) => {
  const [pw, setPw] = useState(""); const [err, setErr] = useState(false);
  const go = () => { if (pw === PW) onUnlock(); else { setErr(true); setTimeout(() => setErr(false), 2000); } };
  return (<div style={{ minHeight: "100vh", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: f }}>
    <div style={{ textAlign: "center", maxWidth: 380, padding: "0 24px" }}>
      <div style={{ fontSize: 10, textTransform: "uppercase", letterSpacing: "0.2em", color: "#999", marginBottom: 8 }}>Weekly Performance Report</div>
      <div style={{ fontSize: 20, fontWeight: 700, color: "#000", textTransform: "uppercase", letterSpacing: "0.12em", marginBottom: 6 }}>Liverpool Los Angeles</div>
      <div style={{ fontSize: 11, color: "#999", fontFamily: mono, marginBottom: 32 }}>Mar 9 – 15, 2026</div>
      <div style={{ width: 48, height: 1, background: "#ddd", margin: "0 auto 32px" }} />
      <div style={{ fontSize: 11, color: "#666", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 12 }}>Enter Password</div>
      <input type="password" value={pw} onChange={e => setPw(e.target.value)} onKeyDown={e => e.key === "Enter" && go()} placeholder="••••••••" style={{ width: "100%", padding: "12px 16px", background: "#fafafa", border: `1px solid ${err ? "#e53e3e" : "#ddd"}`, color: "#000", fontSize: 14, fontFamily: mono, outline: "none", boxSizing: "border-box" }} />
      {err && <div style={{ fontSize: 11, color: "#e53e3e", marginTop: 8, fontFamily: mono }}>Incorrect password</div>}
      <button onClick={go} style={{ marginTop: 16, width: "100%", padding: "10px 0", background: "#000", color: "#fff", border: "none", fontSize: 11, fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.08em", cursor: "pointer" }}>Unlock Report</button>
      <div style={{ fontSize: 10, color: "#bbb", marginTop: 24, fontFamily: mono }}>Prepared by DigitsUp</div>
    </div>
  </div>);
};

// ── S1 DATA ──
const yoyS1 = { totalRevenue: "$200,404.16", totalRevenueChange: -1.6, attributedRevenue: "$102K", attributedRevenuePct: "50.95%", attributedRevenueChange: -6.1, campaigns: "$28.5K", campaignsPct: "27.87%", campaignsChange: -30.1, flows: "$73.7K", flowsPct: "72.13%", flowsChange: 8.3, email: "$64.4K", emailPct: "63.03%", emailChange: -13.9, sms: "$37.8K", smsPct: "36.97%", smsChange: 11.2, label: "vs. same period in previous year" };
const wowS1 = { totalRevenue: "$200,404.16", totalRevenueChange: -23.4, attributedRevenue: "$102K", attributedRevenuePct: "50.95%", attributedRevenueChange: -40.4, campaigns: "$28.5K", campaignsPct: "27.87%", campaignsChange: -61.7, flows: "$73.7K", flowsPct: "72.13%", flowsChange: -24.1, email: "$64.4K", emailPct: "63.03%", emailChange: -46.5, sms: "$37.8K", smsPct: "36.97%", smsChange: -25.9, label: "vs. previous period" };

// ── S2 DATA ──
const yoyCM = [
  { metric: "Total Recipients", email: "670K", emailChange: 5.2, sms: "79K", smsChange: 66.9 },
  { metric: "Unique Opens", email: "300K", emailChange: -8, sms: "–", smsChange: null },
  { metric: "Open Rate", email: "44.8%", emailChange: -12.6, sms: "–", smsChange: null },
  { metric: "Unique Clicks", email: "5.99K", emailChange: 63.5, sms: "6.11K", smsChange: -8.4 },
  { metric: "Click Rate", email: "0.895%", emailChange: 55.4, sms: "7.76%", smsChange: -44.9 },
  { metric: "Unique Conversions", email: "119", emailChange: -48.5, sms: "23", smsChange: -4.2 },
  { metric: "Conversion Rate", email: "0.018%", emailChange: -50, sms: "0.029%", smsChange: -43.1 },
  { metric: "Conversion Value", email: "$23.9K", emailChange: -35.4, sms: "$4.54K", smsChange: 24.5 },
  { metric: "Rev Per Recipient", email: "$0.0357", emailChange: -38.6, sms: "$0.0577", smsChange: -25.2 },
  { metric: "Avg Order Value", email: "$198", emailChange: 24.3, sms: "$197", smsChange: 35.3 },
];
const wowCM = [
  { metric: "Total Recipients", email: "670K", emailChange: -56.8, sms: "79K", smsChange: -60.7 },
  { metric: "Unique Opens", email: "300K", emailChange: -56.3, sms: "–", smsChange: null },
  { metric: "Open Rate", email: "44.8%", emailChange: 1.2, sms: "–", smsChange: null },
  { metric: "Unique Clicks", email: "5.99K", emailChange: -55.3, sms: "6.11K", smsChange: -57.3 },
  { metric: "Click Rate", email: "0.895%", emailChange: 3.3, sms: "7.76%", smsChange: 9.1 },
  { metric: "Unique Conversions", email: "119", emailChange: -64.8, sms: "23", smsChange: -51.1 },
  { metric: "Conversion Rate", email: "0.018%", emailChange: -18.2, sms: "0.029%", smsChange: 26.1 },
  { metric: "Conversion Value", email: "$23.9K", emailChange: -63.4, sms: "$4.54K", smsChange: -48.8 },
  { metric: "Rev Per Recipient", email: "$0.0357", emailChange: -15.4, sms: "$0.0577", smsChange: 30.6 },
  { metric: "Avg Order Value", email: "$198", emailChange: 3.3, sms: "$197", smsChange: 4.5 },
];
const campaignsThisWeek = [
  { name: "New Arrivals Freshly Picked: Stripes", date: "Mar 12", recipients: "243K", orders: 41, revenue: "$8.38K" },
  { name: "Statement Pants for Spring", date: "Mar 11", recipients: "150K", orders: 23, revenue: "$4.95K" },
  { name: "Ecru Set (Petal to the Edge)", date: "Mar 10", recipients: "154K", orders: 19, revenue: "$4.34K" },
  { name: "Outfit of the Week Travel Ready Look", date: "Mar 15", recipients: "83K", orders: 22, revenue: "$3.73K" },
  { name: "SMS: Months Most Reordered Pieces", date: "Mar 13", recipients: "27.7K", orders: 15, revenue: "$3.55K" },
];
const campaigns2025 = [
  { name: "Mens New Arrivals: Overshirts", date: "Mar 15", recipients: "189K", orders: 67, revenue: "$9.24K" },
  { name: "Petite New Arrivals: Cropped", date: "Mar 16", recipients: "26.9K", orders: 40, revenue: "$9.16K" },
  { name: "Montreal Convertible Dress", date: "Mar 11", recipients: "171K", orders: 50, revenue: "$7.68K" },
  { name: "New Arrivals: Shoes", date: "Mar 13", recipients: "162K", orders: 36, revenue: "$5.61K" },
  { name: "SMS Women's Shoes", date: "Mar 13", recipients: "44.7K", orders: 22, revenue: "$3.31K" },
];
const campaignsLastWeek = [
  { name: "Flash Sale Begins", date: "Mar 6", recipients: "296K", orders: 78, revenue: "$16.5K" },
  { name: "Flash Sale Continues", date: "Mar 7", recipients: "158K", orders: 63, revenue: "$10.2K" },
  { name: "Dresses", date: "Mar 4", recipients: "90K", orders: 38, revenue: "$8.9K" },
  { name: "Flash Sale PM", date: "Mar 8", recipients: "188K", orders: 49, revenue: "$8.88K" },
  { name: "Flash Sale AM", date: "Mar 8", recipients: "238K", orders: 36, revenue: "$7.17K" },
];

// ── S3 DATA ──
const yoyFM = [
  { metric: "Total Recipients", email: "39K", emailChange: 13.6, sms: "11.3K", smsChange: 201.5 },
  { metric: "Unique Opens", email: "21.6K", emailChange: 13, sms: "–", smsChange: null },
  { metric: "Open Rate", email: "55.6%", emailChange: -0.5, sms: "–", smsChange: null },
  { metric: "Unique Clicks", email: "2.07K", emailChange: 8.2, sms: "1.95K", smsChange: 144.4 },
  { metric: "Click Rate", email: "5.33%", emailChange: -4.7, sms: "17.3%", smsChange: -18.8 },
  { metric: "Unique Conversions", email: "286", emailChange: 17.2, sms: "207", smsChange: 7.3 },
  { metric: "Conversion Rate", email: "0.736%", emailChange: 3.2, sms: "1.84%", smsChange: -64.3 },
  { metric: "Conversion Value", email: "$40.4K", emailChange: 7.1, sms: "$33.2K", smsChange: 9.6 },
  { metric: "Rev Per Recipient", email: "$1.04", emailChange: -5.7, sms: "$2.95", smsChange: -63.5 },
  { metric: "Avg Order Value", email: "$140", emailChange: -8.5, sms: "$158", smsChange: 0.8 },
];
const wowFM = [
  { metric: "Total Recipients", email: "39K", emailChange: 0.1, sms: "11.3K", smsChange: 0.9 },
  { metric: "Unique Opens", email: "21.6K", emailChange: -4.3, sms: "–", smsChange: null },
  { metric: "Open Rate", email: "55.6%", emailChange: -4.4, sms: "–", smsChange: null },
  { metric: "Unique Clicks", email: "2.07K", emailChange: -12.5, sms: "1.95K", smsChange: -0.5 },
  { metric: "Click Rate", email: "5.33%", emailChange: -12.5, sms: "17.3%", smsChange: -1.5 },
  { metric: "Unique Conversions", email: "286", emailChange: -16.9, sms: "207", smsChange: -14.8 },
  { metric: "Conversion Rate", email: "0.736%", emailChange: -16.9, sms: "1.84%", smsChange: -15.7 },
  { metric: "Conversion Value", email: "$40.4K", emailChange: -26.4, sms: "$33.2K", smsChange: -21.1 },
  { metric: "Rev Per Recipient", email: "$1.04", emailChange: -26.5, sms: "$2.95", smsChange: -21.9 },
  { metric: "Avg Order Value", email: "$140", emailChange: -11.1, sms: "$158", smsChange: -8.3 },
];
const flowsThisWeek = [
  { name: "Welcome Series – SMS 2026", recipients: "1.56K", orders: 96, revenue: "$15.9K" },
  { name: "Welcome Series – Email 2026", recipients: "5.08K", orders: 74, revenue: "$11.5K" },
  { name: "Added2Cart 2025", recipients: "3.07K", orders: 59, revenue: "$11.2K" },
  { name: "Abandoned Checkout 2025", recipients: "1.3K", orders: 58, revenue: "$9.01K" },
  { name: "Post-Purchase Optimization", recipients: "5.55K", orders: 32, revenue: "$3.97K" },
];
const flows2025 = [
  { name: "Welcome Series – SMS", recipients: "1.59K", orders: 128, revenue: "$18.3K" },
  { name: "Added2Cart 2025", recipients: "3.72K", orders: 89, revenue: "$16.2K" },
  { name: "Welcome Series – New 2024", recipients: "3.59K", orders: 58, revenue: "$11.4K" },
  { name: "Abandoned Checkout 2025", recipients: "754", orders: 45, revenue: "$8.05K" },
  { name: "Wonderment | Delivered", recipients: "1.32K", orders: 27, revenue: "$3.25K" },
];
const flowsLastWeek = [
  { name: "Added2Cart 2025", recipients: "4.23K", orders: 88, revenue: "$16.8K" },
  { name: "Abandoned Checkout 2025", recipients: "1.65K", orders: 67, revenue: "$15.2K" },
  { name: "Welcome Series – SMS 2026", recipients: "1.43K", orders: 93, revenue: "$14.5K" },
  { name: "Welcome Series – Email 2026", recipients: "4.72K", orders: 76, revenue: "$11.6K" },
  { name: "Toki – Tier Earned Points Reward", recipients: "1.02K", orders: 48, revenue: "$8.58K" },
];

// ── S4 DATA ──
const s4Base = { totalRevenue: "$890,317.12", attributedRevenue: "$546,843.70", attributedRevenuePct: "61.42%", perRecipient: "$0.09", campaigns: "$200,022.86", campaignsPct: "36.58%", flows: "$346,820.84", flowsPct: "63.42%", email: "$364,018.08", emailPct: "66.57%", textMessage: "$182,825.62", textMessagePct: "33.43%" };
const yoyS4 = { ...s4Base, totalRevenueChange: -3, attributedRevenueChange: 7, topFlows: [
  { name: "Welcome Series – SMS 2026", deliveries: "6,395", revenue: "$62,152", change: null },
  { name: "Added2Cart 2025", deliveries: "14,271", revenue: "$49,855", change: -17.13 },
  { name: "Abandoned Checkout 2025", deliveries: "5,111", revenue: "$48,296", change: 86.40 },
  { name: "Welcome Series – Email 2026", deliveries: "19,494", revenue: "$42,623", change: null },
  { name: "Toki – Tier Earned Points Reward", deliveries: "3,260", revenue: "$23,678", change: null },
  { name: "Browse Abandonment", deliveries: "30,118", revenue: "$15,897", change: 132.13 },
  { name: "Post-Purchase Optimization", deliveries: "24,035", revenue: "$15,852", change: null },
  { name: "Liverpool Bucks – LOVECASH25", deliveries: "11,665", revenue: "$15,274", change: null },
  { name: "Back In Stock – VIP vs. Non-VIP", deliveries: "2,662", revenue: "$13,455", change: 438.59 },
  { name: "Wonderment | Delivered", deliveries: "4,454", revenue: "$10,221", change: -9.67 },
]};
const wowS4 = { ...s4Base, totalRevenueChange: 29, attributedRevenueChange: 44, topFlows: [
  { name: "Welcome Series – SMS 2026", deliveries: "6,395", revenue: "$62,152", change: 44.66 },
  { name: "Added2Cart 2025", deliveries: "14,271", revenue: "$49,855", change: 69.37 },
  { name: "Abandoned Checkout 2025", deliveries: "5,111", revenue: "$48,296", change: 139.06 },
  { name: "Welcome Series – Email 2026", deliveries: "19,494", revenue: "$42,623", change: 63.09 },
  { name: "Toki – Tier Earned Points Reward", deliveries: "3,260", revenue: "$23,678", change: 30.79 },
  { name: "Browse Abandonment", deliveries: "30,118", revenue: "$15,897", change: 84.16 },
  { name: "Post-Purchase Optimization", deliveries: "24,035", revenue: "$15,852", change: 20.21 },
  { name: "Liverpool Bucks – LOVECASH25", deliveries: "11,665", revenue: "$15,274", change: null },
  { name: "Back In Stock – VIP vs. Non-VIP", deliveries: "2,662", revenue: "$13,455", change: -26.62 },
  { name: "Wonderment | Delivered", deliveries: "4,454", revenue: "$10,221", change: 101.31 },
]};

// ── COMMENTARY ──
const yoyComm = {
  s2: {
    improved: [
      "Email click rate +55.4% YoY — strongest engagement metric across campaigns",
      "AOV surging: email $198 (+24.3%), SMS $197 (+35.3%) — converters spending significantly more",
      "SMS conversion value +24.5% YoY — SMS campaigns recovering from last week's decline",
    ],
    declined: [
      "Email conversions -48.5% YoY, conversion rate -50% — fewer sends post-flash sale hitting hard",
      "Campaign revenue -30.1% YoY — $28.5K vs $40.7K LY, biggest gap in weeks",
      "Open rate -12.6% YoY — audience growth diluting open engagement",
    ],
    actions: [
      "This is a send volume issue, not an efficiency issue — click rate and AOV are strong",
      "Review campaign calendar to increase non-promotional send frequency",
      "Consider a targeted mid-week campaign to recover conversion volume",
    ],
  },
  s3: {
    improved: [
      "Flows still positive YoY at +8.3% — carrying the business while campaigns are down",
      "Email conversions +17.2% YoY, conversion rate +3.2% — consistent improvement trend",
      "Welcome Email jumped to #2: $11.5K, 74 orders — new subscriber quality strong",
      "SMS flow value +9.6% YoY ($33.2K) — steady growth despite campaign SMS volatility",
    ],
    declined: [
      "Email AOV dipped to $140 (-8.5% YoY) — possible flash sale hangover on cart values",
      "SMS conversion rate -64.3% YoY — volume growth continues diluting efficiency",
      "Email click rate -4.7% YoY — persistent top-of-funnel engagement gap",
    ],
    actions: [
      "Monitor AOV recovery next week — if it stays low, investigate product mix in flow emails",
      "Test email flow CTAs and product placement to recover click rates",
      "Flows at 72% of attributed revenue — strong but campaigns need to pull more weight",
    ],
  },
  s4: {
    improved: [
      "Attributed revenue flipped positive: +7% YoY (was -1% last week, -13% two weeks ago)",
      "Total revenue nearly flat: -3% YoY (was -12% last week) — gap closing fast",
      "Abandoned Checkout: +86.4% YoY — $48.3K over 30 days, the standout recovery flow",
      "Back In Stock: +438.59% YoY — continues to be the highest-growth flow",
    ],
    declined: [
      "Added2Cart: -17.13% YoY at 30-day level — improving but still negative",
      "Wonderment | Delivered: -9.67% YoY — stabilizing but not yet recovered",
      "Total revenue still slightly negative — unattributed channels still lagging",
    ],
    actions: [
      "Attributed revenue +7% YoY is a major milestone — highlight to the client",
      "Added2Cart trending toward parity — should continue improving as flash sale week rolls in",
      "Push for campaign volume increase to close the unattributed revenue gap",
    ],
  },
};
const wowComm = {
  s2: {
    improved: [
      "Open rate +1.2% WoW — efficiency actually improved despite massive volume drop",
      "Click rate up: email +3.3%, SMS +9.1% WoW — engagement per send is better",
      "AOV up: email +3.3%, SMS +4.5% WoW — cart values recovering from flash sale",
      "SMS conversion rate +26.1% WoW — SMS campaigns more efficient at lower volume",
    ],
    declined: [
      "Conversion value -61.7% WoW — expected flash sale correction",
      "Email conversions -64.8% WoW — volume-driven decline, not efficiency",
      "Recipients -57.3% WoW — half the sends of flash sale week",
    ],
    actions: [
      "Flash sale hangover is expected — the efficiency improvements are the real signal",
      "Next week will show whether this is the new baseline or further correction",
      "Increase non-promotional campaign frequency to rebuild volume",
    ],
  },
  s3: {
    improved: [
      "Flow recipients flat (+0.3%) — traffic into flows is stable unlike campaigns",
      "Revenue decline is purely conversion-driven, not traffic-driven",
    ],
    declined: [
      "Conversion value -24.1% WoW — flash sale pulled forward purchases from flows",
      "Conversions down: email -16.9%, SMS -14.8% WoW",
      "AOV down: email -11.1%, SMS -8.3% WoW — cart values normalizing",
    ],
    actions: [
      "This is the expected post-sale correction — YoY is still +8.3% which is the real read",
      "Watch next week to see if flow conversions stabilize at a higher baseline than pre-sale",
      "Click rates declining 3 weeks straight — email flow CTA testing is overdue",
    ],
  },
  s4: {
    improved: [
      "Total Revenue: +29% WoW — flash sale week now in the 30-day window",
      "Attributed Revenue: +44% WoW — strongest 30-day WoW gain we've seen",
      "Abandoned Checkout: +139.06% WoW — flash sale created massive checkout recovery volume",
      "Added2Cart: +69.37% WoW — the flash sale spike lifting the 30-day number",
    ],
    declined: [
      "Back In Stock: -26.62% WoW — normalizing after weeks of explosive growth",
      "Wonderment | Delivered: -9.67% YoY — still slightly down",
    ],
    actions: [
      "30-day numbers are inflated by flash sale — set expectations that next week may dip",
      "The YoY read (+7% attributed, -3% total) is the more reliable signal",
      "Flows at 63.4% of attributed revenue — automation is the backbone of the business",
    ],
  },
};

// ── COMPONENTS ──
const Badge = ({ value, size = "md" }) => {
  if (value === null || value === undefined) return <span style={{ color: "#bbb", fontSize: 11 }}>–</span>;
  const p = value > 0; const fs = size === "sm" ? 10 : 12;
  return <span style={{ display: "inline-flex", alignItems: "center", gap: 2, background: p ? "#e8f5e9" : "#fce4ec", color: p ? "#2e7d32" : "#c62828", padding: size === "sm" ? "2px 5px" : "2px 7px", borderRadius: 2, fontSize: fs, fontWeight: 600, fontFamily: mono }}>{p ? "+" : "–"}{Math.abs(value)}%</span>;
};
const VT = ({ view, setView, compact }) => (
  <div style={{ display: "flex", border: "1px solid #ddd", padding: 2, background: "#fafafa" }}>
    {["yoy", "wow"].map(v => <button key={v} onClick={() => setView(v)} style={{ padding: compact ? "4px 12px" : "7px 18px", border: "none", cursor: "pointer", background: view === v ? "#000" : "transparent", color: view === v ? "#fff" : "#999", fontWeight: 600, fontSize: compact ? 10 : 11, fontFamily: f, textTransform: "uppercase", letterSpacing: "0.06em" }}>{v === "yoy" ? "YoY" : "WoW"}</button>)}
  </div>
);
const SH = ({ n, title, view, setView }) => (
  <div style={{ display: "flex", alignItems: "center", gap: 14, marginBottom: 16, marginTop: 40, flexWrap: "wrap" }}>
    <div style={{ width: 26, height: 26, background: "#000", color: "#fff", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 12, fontWeight: 700, fontFamily: mono }}>{n}</div>
    <h2 style={{ fontSize: 14, fontWeight: 700, color: "#000", margin: 0, fontFamily: f, textTransform: "uppercase", letterSpacing: "0.08em" }}>{title}</h2>
    <div style={{ flex: 1, height: 1, background: "#e0e0e0", marginLeft: 8 }} />
    <VT view={view} setView={setView} compact />
  </div>
);
const Commentary = ({ data }) => {
  const hs = (c) => ({ fontSize: 10, fontWeight: 700, color: c, fontFamily: f, textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 6 });
  const is = { fontSize: 11.5, color: "#444", lineHeight: 1.55, fontFamily: f, paddingLeft: 12, position: "relative", marginBottom: 4 };
  const ds = (c) => ({ position: "absolute", left: 0, top: 6, width: 4, height: 4, borderRadius: "50%", background: c });
  const ri = (items, c) => items.map((t, i) => <div key={i} style={is}><div style={ds(c)} />{t}</div>);
  return (<div>
    <div style={{ marginBottom: 14 }}><div style={hs("#2e7d32")}>Improved</div>{ri(data.improved, "#2e7d32")}</div>
    <div style={{ marginBottom: 14 }}><div style={hs("#c62828")}>Declined</div>{ri(data.declined, "#c62828")}</div>
    <div><div style={hs("#000")}>Next Steps</div>{ri(data.actions, "#000")}</div>
  </div>);
};
const ths = (l) => ({ textAlign: l ? "left" : "right", padding: "7px 8px", fontWeight: 600, color: "#999", fontSize: 9, textTransform: "uppercase", letterSpacing: "0.08em", fontFamily: f, borderBottom: "2px solid #000" });
const tds = (l, mn, b, d) => ({ textAlign: l ? "left" : "right", padding: "7px 8px", fontFamily: mn ? mono : f, fontWeight: b ? 600 : l ? 500 : 400, color: d ? "#aaa" : "#222", fontSize: 11.5 });
const MT = ({ metrics }) => (
  <div style={{ overflowX: "auto" }}><table style={{ width: "100%", borderCollapse: "collapse" }}>
    <thead><tr>{["Metric", "Email", "Chg", "SMS", "Chg"].map((h, i) => <th key={i} style={ths(i === 0)}>{h}</th>)}</tr></thead>
    <tbody>{metrics.map((r2, i) => <tr key={i} style={{ borderBottom: `1px solid ${i === metrics.length - 1 ? "transparent" : "#eee"}` }}>
      <td style={tds(true)}>{r2.metric}</td><td style={tds(false, true)}>{r2.email}</td>
      <td style={{ textAlign: "right", padding: "7px 8px" }}><Badge value={r2.emailChange} size="sm" /></td>
      <td style={tds(false, true)}>{r2.sms}</td>
      <td style={{ textAlign: "right", padding: "7px 8px" }}><Badge value={r2.smsChange} size="sm" /></td>
    </tr>)}</tbody></table></div>
);
const Card = ({ children }) => <div style={{ background: "#fff", padding: "20px 24px", border: "1px solid #e5e5e5" }}>{children}</div>;
const SP = ({ label1, val1, chg1, label2, val2, chg2 }) => (
  <div style={{ display: "flex", gap: 24, flexWrap: "wrap", marginBottom: 16, paddingBottom: 14, borderBottom: "1px solid #eee" }}>
    {[{ l: label1, v: val1, c: chg1 }, { l: label2, v: val2, c: chg2 }].map((s, i) => <div key={i} style={{ flex: 1, minWidth: 160 }}>
      <div style={{ fontSize: 9, color: "#999", textTransform: "uppercase", letterSpacing: "0.1em", fontFamily: f, marginBottom: 2 }}>{s.l}</div>
      <div style={{ fontSize: 22, fontWeight: 700, color: "#000", fontFamily: mono }}>{s.v}</div>
      <div style={{ marginTop: 2 }}><Badge value={s.c} /></div>
    </div>)}
  </div>
);
const CT = ({ campaigns, dim, label }) => (<>
  <div style={{ fontSize: 10, fontWeight: 600, color: dim ? "#bbb" : "#666", marginTop: dim ? 10 : 14, marginBottom: 4, textTransform: "uppercase", letterSpacing: "0.08em", fontFamily: f }}>{label}</div>
  <div style={{ overflowX: "auto" }}><table style={{ width: "100%", borderCollapse: "collapse", opacity: dim ? 0.5 : 1 }}>
    <thead><tr>{["Campaign", "Date", "Rcpts", "Orders", "Rev"].map(h => <th key={h} style={ths(h === "Campaign")}>{h}</th>)}</tr></thead>
    <tbody>{campaigns.map((c, i) => <tr key={i} style={{ borderBottom: `1px solid ${i === campaigns.length - 1 ? "transparent" : "#eee"}` }}>
      <td style={tds(true, false, false, dim)}>{c.name}</td><td style={tds(false, true, false, true)}>{c.date}</td>
      <td style={tds(false, true, false, dim)}>{c.recipients}</td><td style={tds(false, true, false, dim)}>{c.orders}</td>
      <td style={tds(false, true, true, dim)}>{c.revenue}</td>
    </tr>)}</tbody></table></div>
</>);
const FT = ({ flows, dim, label }) => (<>
  <div style={{ fontSize: 10, fontWeight: 600, color: dim ? "#bbb" : "#666", marginTop: dim ? 10 : 14, marginBottom: 4, textTransform: "uppercase", letterSpacing: "0.08em", fontFamily: f }}>{label}</div>
  <div style={{ overflowX: "auto" }}><table style={{ width: "100%", borderCollapse: "collapse", opacity: dim ? 0.5 : 1 }}>
    <thead><tr>{["Flow", "Recipients", "Orders", "Revenue"].map(h => <th key={h} style={ths(h === "Flow")}>{h}</th>)}</tr></thead>
    <tbody>{flows.map((fl, i) => <tr key={i} style={{ borderBottom: `1px solid ${i === flows.length - 1 ? "transparent" : "#eee"}` }}>
      <td style={tds(true, false, false, dim)}>{fl.name}</td><td style={tds(false, true, false, dim)}>{fl.recipients}</td>
      <td style={tds(false, true, false, dim)}>{fl.orders}</td><td style={tds(false, true, true, dim)}>{fl.revenue}</td>
    </tr>)}</tbody></table></div>
</>);
const TwoCol = ({ commentary, children }) => (
  <div style={{ display: "flex", gap: 24, flexWrap: "wrap" }}>
    <div style={{ flex: "0 0 36%", minWidth: 260 }}>{commentary}</div>
    <div style={{ flex: 1, minWidth: 340 }}>{children}</div>
  </div>
);

// ── MAIN ──
export default function LiverpoolReport() {
  const [unlocked, setUnlocked] = useState(false);
  const [view, setView] = useState("yoy");
  if (!unlocked) return <PasswordGate onUnlock={() => setUnlocked(true)} />;
  const isYoY = view === "yoy";
  const s1 = isYoY ? yoyS1 : wowS1; const s4 = isYoY ? yoyS4 : wowS4;
  const comm = isYoY ? yoyComm : wowComm;
  const cM = isYoY ? yoyCM : wowCM; const fM = isYoY ? yoyFM : wowFM;
  const cOv = isYoY ? { cv: -30.1, tr: 9.5 } : { cv: -61.7, tr: -57.3 };
  const fOv = isYoY ? { cv: 8.3, tr: 32.1 } : { cv: -24.1, tr: 0.3 };
  const compC = isYoY ? campaigns2025 : campaignsLastWeek;
  const compCL = isYoY ? "Top Campaigns — 2025" : "Top Campaigns — Last Week";
  const compF = isYoY ? flows2025 : flowsLastWeek;
  const compFL = isYoY ? "Top Flows — 2025" : "Top Flows — Last Week";

  return (
    <div style={{ minHeight: "100vh", background: "#f7f7f7", fontFamily: f }}>
      <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet" />
      <div style={{ background: "#000", padding: "28px 32px", color: "#fff", display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 16 }}>
        <div>
          <div style={{ fontSize: 10, textTransform: "uppercase", letterSpacing: "0.2em", color: "#777", marginBottom: 4 }}>Weekly Performance Report</div>
          <h1 style={{ fontSize: 20, fontWeight: 700, margin: 0, textTransform: "uppercase", letterSpacing: "0.12em" }}>Liverpool Los Angeles</h1>
          <div style={{ fontSize: 11, color: "#777", marginTop: 4, fontFamily: mono }}>Mar 9 – 15, 2026 &nbsp;|&nbsp; Klaviyo + Shopify</div>
        </div>
        <VT view={view} setView={setView} />
      </div>
      <div style={{ maxWidth: 1100, margin: "0 auto", padding: "0 24px 60px" }}>

        <SH n="1" title="Growth Overview" view={view} setView={setView} />
        <Card>
          <div style={{ textAlign: "center", marginBottom: 20, paddingBottom: 16, borderBottom: "1px solid #eee" }}>
            <div style={{ fontSize: 32, fontWeight: 700, color: "#000", fontFamily: mono }}>{s1.totalRevenue}</div>
            <div style={{ fontSize: 11, color: "#666", marginTop: 3 }}>Total Revenue &nbsp;<Badge value={s1.totalRevenueChange} /></div>
            <div style={{ fontSize: 10, color: "#999", marginTop: 3, fontFamily: mono, textTransform: "uppercase", letterSpacing: "0.05em" }}>{s1.label}</div>
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))", gap: 8 }}>
            {[{ label: "Attributed Revenue", value: s1.attributedRevenue, pct: s1.attributedRevenuePct, change: s1.attributedRevenueChange },
              { label: "Campaigns", value: s1.campaigns, pct: s1.campaignsPct, change: s1.campaignsChange },
              { label: "Flows", value: s1.flows, pct: s1.flowsPct, change: s1.flowsChange },
              { label: "Email", value: s1.email, pct: s1.emailPct, change: s1.emailChange },
              { label: "SMS", value: s1.sms, pct: s1.smsPct, change: s1.smsChange },
            ].map((item, i) => <div key={i} style={{ background: "#fafafa", padding: "10px 12px", border: "1px solid #eee" }}>
              <div style={{ fontSize: 9, color: "#999", textTransform: "uppercase", letterSpacing: "0.08em" }}>{item.label}</div>
              <div style={{ fontSize: 18, fontWeight: 700, color: "#000", marginTop: 2, fontFamily: mono }}>{item.value}</div>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 4 }}>
                <span style={{ fontSize: 10, color: "#aaa", fontFamily: mono }}>{item.pct}</span>
                <Badge value={item.change} size="sm" />
              </div>
            </div>)}
          </div>
        </Card>

        <SH n="2" title="Campaign Performance" view={view} setView={setView} />
        <Card>
          <SP label1="Total Recipients" val1="749,465" chg1={cOv.tr} label2="Conversion Value" val2="$28,455.56" chg2={cOv.cv} />
          <TwoCol commentary={<Commentary data={comm.s2} />}>
            <div style={{ fontSize: 10, fontWeight: 600, color: "#666", marginBottom: 4, textTransform: "uppercase", letterSpacing: "0.08em" }}>Email & SMS Metrics</div>
            <MT metrics={cM} />
            <CT campaigns={campaignsThisWeek} label="Top Campaigns — This Week" />
            <CT campaigns={compC} dim label={compCL} />
          </TwoCol>
        </Card>

        <SH n="3" title="Flow Performance" view={view} setView={setView} />
        <Card>
          <SP label1="Total Recipients" val1="50,260" chg1={fOv.tr} label2="Conversion Value" val2="$73,651.14" chg2={fOv.cv} />
          <TwoCol commentary={<Commentary data={comm.s3} />}>
            <div style={{ fontSize: 10, fontWeight: 600, color: "#666", marginBottom: 4, textTransform: "uppercase", letterSpacing: "0.08em" }}>Email & SMS Metrics</div>
            <MT metrics={fM} />
            <FT flows={flowsThisWeek} label="Top Flows — This Week" />
            <FT flows={compF} dim label={compFL} />
          </TwoCol>
        </Card>

        <SH n="4" title="Klaviyo Performance — Last 30 Days" view={view} setView={setView} />
        <Card>
          <SP label1="Total Revenue" val1={s4.totalRevenue} chg1={s4.totalRevenueChange} label2={`Attributed Revenue (${s4.attributedRevenuePct})`} val2={s4.attributedRevenue} chg2={s4.attributedRevenueChange} />
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(120px, 1fr))", gap: 6, marginBottom: 16, padding: "12px 0", borderBottom: "1px solid #eee" }}>
            {[{ label: "Per Recipient", value: s4.perRecipient },
              { label: "Campaigns", value: s4.campaigns, sub: s4.campaignsPct },
              { label: "Flows", value: s4.flows, sub: s4.flowsPct },
              { label: "Email", value: s4.email, sub: s4.emailPct },
              { label: "Text Message", value: s4.textMessage, sub: s4.textMessagePct },
            ].map((item, i) => <div key={i}>
              <div style={{ fontSize: 9, color: "#999", textTransform: "uppercase", letterSpacing: "0.08em" }}>{item.label}</div>
              <div style={{ fontSize: 12, fontWeight: 700, color: "#000", fontFamily: mono, marginTop: 1 }}>{item.value}</div>
              {item.sub && <div style={{ fontSize: 10, color: "#aaa", fontFamily: mono }}>{item.sub}</div>}
            </div>)}
          </div>
          <TwoCol commentary={<Commentary data={comm.s4} />}>
            <div style={{ fontSize: 10, fontWeight: 600, color: "#666", marginBottom: 4, textTransform: "uppercase", letterSpacing: "0.08em" }}>Flow Breakdown</div>
            <div style={{ overflowX: "auto" }}><table style={{ width: "100%", borderCollapse: "collapse" }}>
              <thead><tr>{["Flow", "Dlvrs", "Revenue", "Chg"].map(h => <th key={h} style={ths(h === "Flow")}>{h}</th>)}</tr></thead>
              <tbody>{s4.topFlows.map((fl, i) => <tr key={i} style={{ borderBottom: `1px solid ${i === s4.topFlows.length - 1 ? "transparent" : "#eee"}` }}>
                <td style={tds(true)}>{fl.name}</td><td style={tds(false, true, false, true)}>{fl.deliveries}</td>
                <td style={tds(false, true, true)}>{fl.revenue}</td>
                <td style={{ textAlign: "right", padding: "7px 8px" }}><Badge value={fl.change} size="sm" /></td>
              </tr>)}</tbody></table></div>
          </TwoCol>
        </Card>

        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 40, paddingTop: 16, borderTop: "1px solid #e0e0e0" }}>
          <span style={{ color: "#bbb", fontSize: 10, textTransform: "uppercase", letterSpacing: "0.1em" }}>Prepared by DigitsUp</span>
          <span style={{ color: "#bbb", fontSize: 10, fontFamily: mono }}>Klaviyo + Shopify</span>
        </div>
      </div>
    </div>
  );
}
