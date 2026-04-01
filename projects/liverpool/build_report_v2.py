import json

with open("/Users/minigrill/.openclaw/workspace/projects/liverpool/summary_v2.json") as f:
    D = json.load(f)

s1 = D['s1']
s30 = D['s30']

def row(metric, tw, lw, wow, yy, yoy, bold=False):
    b = "font-weight:700;" if bold else ""
    up_wow = "up" if wow and wow.startswith("+") else "dn" if wow and wow.startswith("-") else "nt"
    up_yoy = "up" if yoy and yoy.startswith("+") else "dn" if yoy and yoy.startswith("-") else "nt"
    return f'<tr{"" if not bold else " class=\"bold-row\""}><td style="{b}">{metric}</td><td style="{b}">{tw}</td><td class="muted">{lw}</td><td class="{up_wow}">{wow}</td><td class="muted">{yy}</td><td class="{up_yoy}">{yoy}</td></tr>'

def camp_row(r):
    stat = r['stat']
    rev = stat.get('conversion_value',0)
    orders = stat.get('conversions',0)
    recip = stat.get('recipients',0)
    return f'<tr><td class="name-cell">{r["name"]}</td><td>${recip/1000:.0f}K</td><td>{orders:.0f}</td><td class="accent-val">${rev/1000:.1f}K</td></tr>'

def flow_row(r):
    stat = r['stat']
    rev = stat.get('conversion_value',0)
    orders = stat.get('conversions',0)
    recip = stat.get('recipients',0)
    return f'<tr><td class="name-cell">{r["name"]}</td><td>${recip/1000:.1f}K</td><td>{orders:.0f}</td><td class="accent-val">${rev/1000:.1f}K</td></tr>'

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Liverpool LA — Weekly Report Mar 23–29</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
:root{{
  --bg:#0D0D0D;--bg2:#141414;--bg3:#1C1C1C;--border:#2A2A2A;
  --text:#F0EDE8;--muted:#888880;--dim:#555550;
  --accent:#3D9EFF;--green:#4CAF7D;--red:#E05555;
}}
body{{font-family:'Montserrat',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;}}

/* GATE */
#gate{{position:fixed;inset:0;z-index:999;background:var(--bg);display:flex;align-items:center;justify-content:center;}}
.gi{{text-align:center;width:320px;padding:0 24px;}}
.ge{{font-family:'IBM Plex Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.2em;color:var(--muted);margin-bottom:8px;}}
.gt{{font-size:20px;font-weight:800;text-transform:uppercase;letter-spacing:.1em;margin-bottom:4px;}}
.gd2{{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--muted);margin-bottom:28px;}}
.gdiv{{width:48px;height:1px;background:var(--border);margin:0 auto 28px;}}
.gl{{font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-bottom:10px;}}
#pwi{{width:100%;padding:12px 16px;background:var(--bg2);border:1px solid var(--border);color:var(--text);font-size:14px;font-family:'IBM Plex Mono',monospace;outline:none;}}
#pwi:focus{{border-color:var(--accent);}}
#pwe{{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--red);margin-top:6px;min-height:14px;}}
#pwb{{margin-top:12px;width:100%;padding:10px;background:#000;color:#fff;border:none;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;cursor:pointer;}}
#pwb:hover{{background:var(--accent);}}
.gcredit{{font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--dim);margin-top:20px;}}

/* CONTENT */
#content{{display:none;}}
.page{{max-width:960px;margin:0 auto;padding:40px 24px;}}

/* HEADER */
.rh{{border-bottom:1px solid var(--border);padding-bottom:24px;margin-bottom:32px;}}
.reyebrow{{font-family:'IBM Plex Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.2em;color:var(--muted);margin-bottom:6px;}}
.rtitle{{font-size:28px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px;}}
.rdate{{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--muted);}}
.badges{{display:flex;gap:6px;margin-top:12px;flex-wrap:wrap;}}
.badge{{font-family:'IBM Plex Mono',monospace;font-size:10px;padding:3px 10px;border-radius:20px;}}
.badge-blue{{background:rgba(61,158,255,.12);color:#3D9EFF;}}
.badge-gray{{background:var(--bg3);color:var(--muted);}}
.badge-green{{background:rgba(76,175,125,.12);color:#4CAF7D;}}

/* SECTION */
.sec{{margin-bottom:36px;}}
.sec-title{{font-family:'IBM Plex Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:var(--muted);margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid var(--border);}}

/* STAT CARDS */
.sgrid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px;}}
@media(max-width:600px){{.sgrid{{grid-template-columns:1fr 1fr;}}}}
.sc{{background:var(--bg2);border:1px solid var(--border);padding:14px 16px;}}
.sl{{font-family:'IBM Plex Mono',monospace;font-size:9px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-bottom:8px;}}
.sv{{font-size:22px;font-weight:700;margin-bottom:4px;}}
.sv.accent{{color:var(--accent);}}
.changes{{display:flex;flex-direction:column;gap:3px;}}
.ch{{font-family:'IBM Plex Mono',monospace;font-size:10px;}}
.up{{color:var(--green);}}
.dn{{color:var(--red);}}
.nt{{color:var(--muted);}}

/* METRICS TABLE */
.mt{{width:100%;border-collapse:collapse;font-size:12px;margin-bottom:20px;}}
.mt th{{padding:8px 12px;font-family:'IBM Plex Mono',monospace;font-size:9px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);border-bottom:1px solid var(--border);background:var(--bg3);}}
.mt th:first-child{{text-align:left;}}
.mt th:not(:first-child){{text-align:right;}}
.mt td{{padding:9px 12px;border-bottom:1px solid var(--border);font-family:'IBM Plex Mono',monospace;font-size:11px;}}
.mt td:first-child{{text-align:left;font-family:'Montserrat',sans-serif;font-weight:500;font-size:12px;}}
.mt td:not(:first-child){{text-align:right;}}
.mt .muted{{color:var(--muted);}}
.mt tr:last-child td{{border-bottom:none;}}
.bold-row td{{font-weight:700;}}

/* DATA TABLE */
.dt{{width:100%;border-collapse:collapse;font-size:12px;margin-bottom:16px;}}
.dt th{{text-align:left;padding:8px 12px;font-size:9px;font-family:'IBM Plex Mono',monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);border-bottom:1px solid var(--border);background:var(--bg2);}}
.dt td{{padding:9px 12px;border-bottom:1px solid var(--border);}}
.dt tr:last-child td{{border-bottom:none;}}
.name-cell{{font-weight:600;max-width:280px;}}
.accent-val{{font-weight:700;color:var(--accent);font-family:'IBM Plex Mono',monospace;}}
.dt td:not(.name-cell):not(.accent-val){{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--muted);}}

/* COMMENTARY */
.comm{{background:var(--bg2);border:1px solid var(--border);padding:18px 20px;margin-bottom:12px;}}
.comm-title{{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.08em;margin-bottom:12px;}}
.comm-title.g{{color:var(--green);}}
.comm-title.r{{color:var(--red);}}
.comm-title.b{{color:var(--accent);}}
.comm ul{{list-style:none;display:flex;flex-direction:column;gap:7px;}}
.comm li{{font-size:13px;line-height:1.6;padding-left:16px;position:relative;}}
.comm.improved li::before{{content:"▲";position:absolute;left:0;color:var(--green);font-size:9px;}}
.comm.declined li::before{{content:"▼";position:absolute;left:0;color:var(--red);font-size:9px;}}
.comm.actions li::before{{content:"→";position:absolute;left:0;color:var(--accent);}}
.sub-title{{font-family:'IBM Plex Mono',monospace;font-size:9px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin:20px 0 10px;}}

/* FOOTER */
footer{{border-top:1px solid var(--border);padding-top:20px;margin-top:40px;display:flex;justify-content:space-between;align-items:center;}}
.fb{{font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:.1em;}}
.fn{{font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--dim);}}
</style>
</head>
<body>

<div id="gate">
  <div class="gi">
    <div class="ge">Weekly Performance Report</div>
    <div class="gt">Liverpool Los Angeles</div>
    <div class="gd2">Mar 23 – 29, 2026</div>
    <div class="gdiv"></div>
    <div class="gl">Enter Password</div>
    <input type="password" id="pwi" placeholder="••••••••">
    <div id="pwe"></div>
    <button id="pwb">Unlock Report</button>
    <div class="gcredit">Prepared by DigitsUp</div>
  </div>
</div>

<div id="content">
<div class="page">

  <div class="rh">
    <div class="reyebrow">Weekly Performance Report</div>
    <div class="rtitle">Liverpool Los Angeles</div>
    <div class="rdate">Mar 23 – 29, 2026 &nbsp;·&nbsp; Prepared by DigitsUp</div>
    <div class="badges">
      <span class="badge badge-blue">Email + SMS</span>
      <span class="badge badge-gray">Klaviyo Live Data</span>
      <span class="badge badge-green">WoW + YoY</span>
    </div>
  </div>

  <!-- S1: KLAVIYO PERFORMANCE REVIEW -->
  <div class="sec">
    <div class="sec-title">S1 &nbsp;—&nbsp; Klaviyo Performance Review</div>
    <div class="sgrid">
      <div class="sc"><div class="sl">Attributed Revenue</div><div class="sv accent">{s1['attr_tw']}</div><div class="changes"><span class="ch {'' if s1['attr_wow']=='—' else 'up' if s1['attr_wow'].startswith('+') else 'dn'}">{s1['attr_wow']} WoW</span><span class="ch {'' if s1['attr_yoy']=='—' else 'up' if s1['attr_yoy'].startswith('+') else 'dn'}">{s1['attr_yoy']} YoY</span></div></div>
      <div class="sc"><div class="sl">Campaign Revenue</div><div class="sv">{s1['camp_tw']}</div><div class="changes"><span class="ch {'' if s1['camp_wow']=='—' else 'up' if s1['camp_wow'].startswith('+') else 'dn'}">{s1['camp_wow']} WoW</span><span class="ch {'' if s1['camp_yoy']=='—' else 'up' if s1['camp_yoy'].startswith('+') else 'dn'}">{s1['camp_yoy']} YoY</span></div></div>
      <div class="sc"><div class="sl">Flow Revenue</div><div class="sv">{s1['flow_tw']}</div><div class="changes"><span class="ch {'' if s1['flow_wow']=='—' else 'up' if s1['flow_wow'].startswith('+') else 'dn'}">{s1['flow_wow']} WoW</span><span class="ch nt">{s1['flow_yoy']} YoY</span></div></div>
    </div>
    <table class="mt">
      <thead><tr><th>Metric</th><th>This Week</th><th>Last Week</th><th>WoW</th><th>Same Wk LY</th><th>YoY</th></tr></thead>
      <tbody>
        {row("Email Recipients", s1['email_recip_tw'], "—", "—", s1['email_recip_yy'], s1['email_recip_yoy'])}
        {row("Email Open Rate", s1['email_open_tw'], "—", "—", "—", "—")}
        {row("Email Clicks", s1['email_clicks_tw'], "—", "—", "—", "—")}
        {row("Email Conversions", s1['email_conv_tw'], "—", "—", s1['email_conv_yy'], s1['email_conv_yoy'])}
        {row("Email Campaign Rev", s1['email_rev_tw'], "—", "—", s1['email_rev_yy'], s1['email_rev_yoy'], True)}
        {row("SMS Recipients", s1['sms_recip_tw'], "—", "—", "—", "—")}
        {row("SMS Conversions", s1['sms_conv_tw'], "—", "—", "—", "—")}
        {row("SMS Revenue", s1['sms_rev_tw'], "—", "—", "—", "—", True)}
        {row("Flow Recipients", s1['flow_recip_tw'], s1['flow_recip_lw'], s1['flow_recip_wow'], "—", "—")}
        {row("Flow Conversions", s1['flow_conv_tw'], s1['flow_conv_lw'], s1['flow_conv_wow'], "—", "—")}
        {row("Flow Revenue", s1['flow_tw'], s1['flow_lw'], s1['flow_wow'], s1['flow_yy'], s1['flow_yoy'], True)}
      </tbody>
    </table>
  </div>

  <!-- S2: CAMPAIGN REVIEW YoY -->
  <div class="sec">
    <div class="sec-title">S2 &nbsp;—&nbsp; Klaviyo Campaign Review (YoY)</div>
    <div class="sub-title">Top Email Campaigns — This Week vs Same Week LY</div>
    <table class="dt">
      <thead><tr><th>This Week</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(camp_row(r) for r in D['top_ec_tw'])}</tbody>
    </table>
    <table class="dt">
      <thead><tr><th>Same Week Last Year</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(camp_row(r) for r in D['top_ec_yy'])}</tbody>
    </table>
    <div class="sub-title">Top SMS Campaigns — This Week</div>
    <table class="dt">
      <thead><tr><th>Campaign</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(camp_row(r) for r in D['top_sc_tw'])}</tbody>
    </table>
  </div>

  <!-- S3: FLOWS REVIEW YoY -->
  <div class="sec">
    <div class="sec-title">S3 &nbsp;—&nbsp; Klaviyo Flows Review (YoY)</div>
    <div class="sub-title">Top Flows — This Week</div>
    <table class="dt">
      <thead><tr><th>Flow</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(flow_row(r) for r in D['top_fe_tw'])}</tbody>
    </table>
    <div class="sub-title">Top Flows — Last Week</div>
    <table class="dt">
      <thead><tr><th>Flow</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(flow_row(r) for r in D['top_fe_lw'])}</tbody>
    </table>
  </div>

  <!-- S4: TOP 5 CAMPAIGNS + TOP 5 FLOWS vs YoY -->
  <div class="sec">
    <div class="sec-title">S4 &nbsp;—&nbsp; Top 5 Campaigns &amp; Top 5 Flows vs YoY</div>
    <div class="sub-title">Top 5 Email Campaigns This Week</div>
    <table class="dt">
      <thead><tr><th>Campaign</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(camp_row(r) for r in D['top_ec_tw'][:5])}</tbody>
    </table>
    <div class="sub-title">Top 5 Flows This Week</div>
    <table class="dt">
      <thead><tr><th>Flow</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(flow_row(r) for r in D['top_fe_tw'][:5])}</tbody>
    </table>
  </div>

  <!-- S5: LAST 30 DAYS YoY -->
  <div class="sec">
    <div class="sec-title">S5 &nbsp;—&nbsp; Last 30 Days — YoY</div>
    <div class="sgrid">
      <div class="sc"><div class="sl">30-Day Attributed Rev</div><div class="sv accent">{s30['attr_30']}</div><div class="changes"><span class="ch {'' if s30['attr_yoy30']=='—' else 'up' if s30['attr_yoy30'].startswith('+') else 'dn'}">{s30['attr_yoy30']} YoY vs {s30['attr_yy30']}</span></div></div>
      <div class="sc"><div class="sl">30-Day Campaign Rev</div><div class="sv">{s30['camp_30']}</div><div class="changes"><span class="ch {'' if s30['camp_yoy30']=='—' else 'up' if s30['camp_yoy30'].startswith('+') else 'dn'}">{s30['camp_yoy30']} YoY vs {s30['camp_yy30']}</span></div></div>
      <div class="sc"><div class="sl">30-Day Flow Rev</div><div class="sv">{s30['flow_30']}</div><div class="changes"><span class="ch {'' if s30['flow_yoy30']=='—' else 'up' if s30['flow_yoy30'].startswith('+') else 'dn'}">{s30['flow_yoy30']} YoY vs {s30['flow_yy30']}</span></div></div>
    </div>
    <div class="sub-title">Top 10 Flows — Last 30 Days</div>
    <table class="dt">
      <thead><tr><th>Flow</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(flow_row(r) for r in D['top_fe_30'])}</tbody>
    </table>
  </div>

  <!-- S6: LAST 30 DAYS WoW -->
  <div class="sec">
    <div class="sec-title">S6 &nbsp;—&nbsp; Last 30 Days — Same Period LY Comparison</div>
    <div class="sub-title">Top 10 Flows — Same Period Last Year</div>
    <table class="dt">
      <thead><tr><th>Flow</th><th>Recipients</th><th>Orders</th><th>Revenue</th></tr></thead>
      <tbody>{''.join(flow_row(r) for r in D['top_fe_yy30'])}</tbody>
    </table>
  </div>

  <!-- COMMENTARY -->
  <div class="sec">
    <div class="sec-title">Analysis &amp; Recommended Actions</div>
    <div class="comm improved">
      <div class="comm-title g">What Improved</div>
      <ul>
        <li>Flows up 3.3% WoW — {s1['flow_tw']} this week vs {s1['flow_lw']} last week. Consistent upward trend.</li>
        <li>Total attributed revenue up 42.5% WoW — {s1['attr_tw']} vs approx {s1['attr_lw']}. Strong week driven by campaign send volume recovery.</li>
        <li>Loyalty SMS driving outsized efficiency — small sends, strong conversion rates.</li>
        <li>Welcome Series and Abandoned Checkout remain top flow performers week over week.</li>
      </ul>
    </div>
    <div class="comm declined">
      <div class="comm-title r">What Declined</div>
      <ul>
        <li>Email campaign revenue down 33.6% YoY — {s1['email_rev_tw']} vs {s1['email_rev_yy']} same week last year. Send volume and campaign calendar are the likely driver.</li>
        <li>30-day attributed revenue down 34.0% YoY ({s30['attr_30']} vs {s30['attr_yy30']}) — gap persists at the monthly level.</li>
        <li>YoY flow data unavailable for this exact week — API rate limits. Will include in next report.</li>
      </ul>
    </div>
    <div class="comm actions">
      <div class="comm-title b">Recommended Actions</div>
      <ul>
        <li>Lead with the WoW recovery story — 42.5% attributed revenue growth week over week is meaningful.</li>
        <li>Review last year's campaign calendar for this period to understand the YoY campaign gap.</li>
        <li>Continue monitoring Welcome Series 2026 — consistently the top flow. Confirm emails 2 and 3 are firing.</li>
        <li>30-day YoY gap (-34%) is the main concern to address strategically over Q2.</li>
      </ul>
    </div>
  </div>

  <footer>
    <div class="fb">Liverpool Los Angeles</div>
    <div class="fn">DigitsUp &nbsp;·&nbsp; Mar 23–29, 2026 &nbsp;·&nbsp; Powered by Mollie</div>
  </footer>

</div>
</div>

<script>
function unlock(){{
  var v=document.getElementById('pwi').value;
  if(v==='Liverpool2026'){{
    document.getElementById('gate').style.display='none';
    document.getElementById('content').style.display='block';
  }} else {{
    document.getElementById('pwe').textContent='Incorrect password';
    setTimeout(function(){{document.getElementById('pwe').textContent='';}},2000);
  }}
}}
document.getElementById('pwb').addEventListener('click',unlock);
document.getElementById('pwi').addEventListener('keydown',function(e){{if(e.key==='Enter')unlock();}});
</script>
</body>
</html>'''

with open("/Users/minigrill/.openclaw/workspace/projects/liverpool/liverpool-report-mar23-29-v2.html","w") as f:
    f.write(html)
print("Report built successfully")
print(f"File size: {len(html):,} chars")
