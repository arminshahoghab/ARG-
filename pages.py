# pages.py - پنل عقاب (نسخه کامل با تم RGB و تنظیمات)

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🦅 ورود · پنل عقاب</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
@keyframes fireBG{0%{background-position:0% 50%}25%{background-position:50% 0%}50%{background-position:100% 50%}75%{background-position:50% 100%}100%{background-position:0% 50%}}
@keyframes flameFlicker{0%{opacity:0.6;transform:scale(1)}50%{opacity:1;transform:scale(1.02)}100%{opacity:0.6;transform:scale(1)}}
@keyframes rgbBG{0%{background:#1a0505}25%{background:#050a1a}50%{background:#1a0a05}75%{background:#0a051a}100%{background:#1a0505}}
:root{--bg:#0a0a1a;--card:rgba(20,10,10,0.85);--accent:#FF6B35;--accent2:#FF8C00;--text:#F0EEFF;--dim:#8A4A3A;--mid:#A06040;--border:rgba(255,100,50,0.2)}
[data-theme="white"]{--bg:#F5E6E0;--card:rgba(255,245,240,0.85);--accent:#E05A2A;--accent2:#CC5500;--text:#2A0A05;--dim:#8A5A4A;--mid:#6A3A2A;--border:rgba(200,80,40,0.2)}
body.rgb-mode{background:linear-gradient(135deg,#1a0505,#050a1a,#1a0a05,#0a051a,#1a0505) !important;background-size:400% 400% !important;animation:rgbBG 4s ease infinite !important}
[data-theme="white"] body.rgb-mode{background:linear-gradient(135deg,#f5e6e0,#e0e8f5,#f0e8d5,#e8d5f0,#f5e6e0) !important;background-size:400% 400% !important;animation:rgbBG 4s ease infinite !important}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:linear-gradient(135deg,#1a0505,#2a0a0a,#3d0f0a,#2a0505,#1a0a0a);background-size:400% 400%;animation:fireBG 8s ease infinite;display:flex;align-items:center;justify-content:center;padding:20px;transition:background .3s}
[data-theme="white"] body{background:linear-gradient(135deg,#F5E6E0,#E8D5CC,#F0D5C8)}
.fire-particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.fire-particle{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(255,120,50,0.4),rgba(255,50,0,0));width:6px;height:6px;animation:floatFire 12s ease-in-out infinite}
@keyframes floatFire{0%{transform:translateY(100vh) scale(0) rotate(0deg);opacity:0}20%{opacity:1}80%{opacity:1}100%{transform:translateY(-10vh) scale(1.5) rotate(720deg);opacity:0}}
.glow-orb{position:fixed;border-radius:50%;filter:blur(150px);z-index:0;animation:flameFlicker 3s ease-in-out infinite;pointer-events:none}
.orb1{width:500px;height:500px;background:rgba(255,80,20,0.05);top:-200px;right:-100px}
.orb2{width:400px;height:400px;background:rgba(255,150,50,0.04);bottom:-100px;left:-80px;animation-delay:2s}
.orb3{width:300px;height:300px;background:rgba(200,50,0,0.03);top:50%;left:50%;transform:translate(-50%,-50%);animation-delay:4s}
.wrap{position:relative;z-index:10;width:100%;max-width:420px}
.card{background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid rgba(255,100,50,0.15);border-radius:28px;padding:44px 38px 38px;box-shadow:0 0 100px rgba(255,80,20,0.04),0 25px 70px rgba(0,0,0,0.6);animation:cardIn 0.6s ease;transition:background .3s}
@keyframes cardIn{from{opacity:0;transform:translateY(30px) scale(0.96)}to{opacity:1;transform:translateY(0) scale(1)}}
.brand{display:flex;align-items:center;gap:16px;margin-bottom:30px}
.brand-icon{width:56px;height:56px;border-radius:16px;background:linear-gradient(135deg,#FF6B35,#FF4500);display:flex;align-items:center;justify-content:center;font-size:28px;flex-shrink:0;box-shadow:0 0 60px rgba(255,80,20,0.15),0 8px 30px rgba(255,80,20,0.2);animation:flameFlicker 2s ease-in-out infinite}
.brand-name{font-size:20px;font-weight:800;background:linear-gradient(135deg,#FF8C00,#FF4500,#FF6B35);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.brand-sub{font-size:11px;color:var(--dim);margin-top:2px;-webkit-text-fill-color:var(--dim)}
h1{font-size:22px;font-weight:800;color:var(--text);margin-bottom:6px}
.sub{font-size:12.5px;color:var(--mid);margin-bottom:26px;line-height:1.7}
.hint{display:flex;align-items:center;gap:10px;background:rgba(255,80,20,0.06);border:1px solid rgba(255,80,20,0.12);border-radius:12px;padding:10px 16px;margin-bottom:22px}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:#FF8C00;background:rgba(255,80,20,0.1);border:1px solid rgba(255,80,20,0.2);padding:3px 13px;border-radius:8px;cursor:pointer;transition:.2s}
.hint-val:hover{background:rgba(255,80,20,0.2);box-shadow:0 0 30px rgba(255,80,20,0.1)}
.field{margin-bottom:20px}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--mid);margin-bottom:8px;text-transform:uppercase;letter-spacing:.08em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:14px 48px 14px 18px;border-radius:12px;border:1px solid rgba(255,100,50,0.15);background:rgba(0,0,0,.3);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.3s}
input[type=password]:focus{border-color:rgba(255,100,50,.5);background:rgba(0,0,0,.4);box-shadow:0 0 0 4px rgba(255,80,20,.06),0 0 40px rgba(255,80,20,.03)}
.ic{position:absolute;left:16px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;transition:.3s}
input:focus+.ic{color:#FF8C00}
.err{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.2);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px}
.err.show{display:flex}
.btn{width:100%;padding:14px;border-radius:12px;border:none;cursor:pointer;background:linear-gradient(135deg,#FF6B35,#FF4500,#FF8C00);background-size:200% 200%;animation:btnFire 3s ease infinite;color:#fff;font-family:inherit;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px;box-shadow:0 4px 30px rgba(255,80,20,.25);transition:all .3s;position:relative;overflow:hidden}
@keyframes btnFire{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn::before{content:'';position:absolute;inset:0;background:rgba(255,255,255,.08);opacity:0;transition:.3s}
.btn:hover::before{opacity:1}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(255,80,20,.35)}
.btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.footer{margin-top:24px;padding-top:20px;border-top:1px solid rgba(255,100,50,0.08);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim)}
.footer button{background:none;border:none;color:var(--accent);cursor:pointer;font-weight:600;font-family:inherit;font-size:11px;display:flex;align-items:center;gap:4px;transition:.3s}
.footer button:hover{color:#FF4500}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="fire-particles">
    <div class="fire-particle" style="left:5%;animation-delay:0s;width:8px;height:8px"></div>
    <div class="fire-particle" style="left:15%;animation-delay:2s;width:5px;height:5px"></div>
    <div class="fire-particle" style="left:25%;animation-delay:4s;width:10px;height:10px"></div>
    <div class="fire-particle" style="left:35%;animation-delay:1s;width:6px;height:6px"></div>
    <div class="fire-particle" style="left:45%;animation-delay:5s;width:7px;height:7px"></div>
    <div class="fire-particle" style="left:55%;animation-delay:3s;width:9px;height:9px"></div>
    <div class="fire-particle" style="left:65%;animation-delay:6s;width:5px;height:5px"></div>
    <div class="fire-particle" style="left:75%;animation-delay:2s;width:8px;height:8px"></div>
    <div class="fire-particle" style="left:85%;animation-delay:4s;width:6px;height:6px"></div>
    <div class="fire-particle" style="left:95%;animation-delay:7s;width:7px;height:7px"></div>
</div>
<div class="glow-orb orb1"></div><div class="glow-orb orb2"></div><div class="glow-orb orb3"></div>
<div class="wrap">
  <div class="card">
    <div class="brand"><div class="brand-icon">🦅</div><div><div class="brand-name">پنل عقاب</div><div class="brand-sub">مدیریت کاربران</div></div></div>
    <h1>ورود به پنل عقاب</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint"><span class="hint-label">رمز پیش‌فرض</span><span class="hint-val" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span></div>
    <form id="form">
      <div class="field"><label>رمز عبور</label><div class="inp-wrap"><input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required><i class="ti ti-lock ic"></i></div></div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به پنل</button>
    </form>
    <div class="footer">🦅 پنل عقاب · v10.0 · <button onclick="toggleTheme()"><i class="ti ti-palette"></i> تغییر تم</button></div>
  </div>
</div>
<script>
let currentTheme = localStorage.getItem('eagle-theme') || 'dark';
function applyTheme(theme){document.documentElement.setAttribute('data-theme',theme);localStorage.setItem('eagle-theme',theme);}
function toggleTheme(){currentTheme=currentTheme==='dark'?'white':'dark';applyTheme(currentTheme);}
applyTheme(currentTheme);
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به پنل';
  }
});
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🦅 پنل عقاب · مدیریت کاربران</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0a0a1a;--bg2:#12122a;--bg3:#1a1a3a;
  --card:rgba(20,10,10,0.7);--card-b:rgba(255,100,50,0.12);--card-bh:rgba(255,100,50,0.28);
  --accent:#FF6B35;--accent2:#FF8C00;--accent-d:rgba(255,80,20,0.08);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;
  --pink:#EC4899;--pink-bg:rgba(236,72,153,0.08);
  --purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.08);
  --t1:#F0EEFF;--t2:#A07050;--t3:#7A4A3A;
  --sidebar-w:240px;--radius:16px;
  --shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(255,80,20,0.03);
}
[data-theme="white"]{
  --bg:#F5E6E0;--bg2:#E8D5CC;--bg3:#F0D5C8;
  --card:rgba(255,245,240,0.7);--card-b:rgba(200,80,40,0.14);--card-bh:rgba(200,80,40,0.3);
  --accent:#E05A2A;--accent2:#CC5500;--accent-d:rgba(200,80,40,0.06);
  --green:#059669;--green-bg:rgba(5,150,105,0.06);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.06);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.06);--amber-t:#92400E;
  --pink:#DB2777;--pink-bg:rgba(219,39,119,0.06);
  --purple:#7C3AED;--purple-bg:rgba(124,58,237,0.06);
  --t1:#2A0A05;--t2:#6A3A2A;--t3:#8A5A4A;
  --shadow:0 8px 32px rgba(0,0,0,0.06);
}
@keyframes fireBG{0%{background-position:0% 50%}25%{background-position:50% 0%}50%{background-position:100% 50%}75%{background-position:50% 100%}100%{background-position:0% 50%}}
@keyframes flamePulse{0%,100%{opacity:0.4}50%{opacity:0.8}}
@keyframes rgbBG{0%{background:#1a0505}25%{background:#050a1a}50%{background:#1a0a05}75%{background:#0a051a}100%{background:#1a0505}}
@keyframes rgbBGLight{0%{background:#f5e6e0}25%{background:#e0e8f5}50%{background:#f0e8d5}75%{background:#e8d5f0}100%{background:#f5e6e0}}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:linear-gradient(135deg,#1a0505,#2a0a0a,#3d0f0a,#2a0505,#1a0a0a);background-size:400% 400%;animation:fireBG 8s ease infinite;color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
[data-theme="white"] body{background:linear-gradient(135deg,#F5E6E0,#E8D5CC,#F0D5C8)}
body.rgb-mode{background:linear-gradient(135deg,#1a0505,#050a1a,#1a0a05,#0a051a,#1a0505) !important;background-size:400% 400% !important;animation:rgbBG 4s ease infinite !important}
[data-theme="white"] body.rgb-mode{background:linear-gradient(135deg,#f5e6e0,#e0e8f5,#f0e8d5,#e8d5f0,#f5e6e0) !important;background-size:400% 400% !important;animation:rgbBGLight 4s ease infinite !important}
.fire-glow{position:fixed;border-radius:50%;filter:blur(150px);z-index:0;animation:flamePulse 2s ease-in-out infinite;pointer-events:none}
.fg1{width:600px;height:600px;background:rgba(255,80,20,0.04);top:-250px;right:-150px}
.fg2{width:450px;height:450px;background:rgba(255,150,50,0.03);bottom:-150px;left:-100px;animation-delay:1s}
.fg3{width:300px;height:300px;background:rgba(200,50,0,0.03);top:50%;left:50%;transform:translate(-50%,-50%);animation-delay:2s}
@keyframes orbFloat{0%,100%{transform:translate(0,0)}33%{transform:translate(40px,-40px)}66%{transform:translate(-30px,30px)}}

.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .3s cubic-bezier(.4,0,.2,1),background .3s;box-shadow:var(--shadow)}
.logo{display:flex;align-items:center;gap:14px;padding:22px 18px 18px;border-bottom:1px solid var(--card-b)}
.logo-icon{width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,#FF6B35,#FF4500);display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;box-shadow:0 0 40px rgba(255,80,20,0.15);animation:flamePulse 2s ease-in-out infinite}
.logo-name{font-size:15px;font-weight:800;background:linear-gradient(135deg,#FF8C00,#FF4500);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo-sub{font-size:9px;color:var(--t3);margin-top:1px;-webkit-text-fill-color:var(--t3)}
.nav-wrap{flex:1;overflow-y:auto;padding:8px 0}
.nav-it{display:flex;align-items:center;gap:10px;padding:10px 16px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .2s;margin:2px 8px;border-radius:10px}
.nav-it i{font-size:16px;width:20px;text-align:center;flex-shrink:0;transition:transform .3s}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it:hover i{transform:scale(1.1)}
.nav-it.on{background:linear-gradient(135deg,var(--accent-d),rgba(255,80,20,0.05));color:var(--t1);border-right-color:var(--accent);font-weight:600;box-shadow:0 0 30px rgba(255,80,20,0.03)}
.nav-badge{margin-right:auto;background:linear-gradient(135deg,#FF6B35,#FF4500);color:#fff;font-size:9px;padding:1px 8px;border-radius:20px;font-weight:700}
.sb-foot{padding:14px 16px;border-top:1px solid var(--card-b)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:10px;padding:8px;font-size:11px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.2s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.rgb-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:linear-gradient(135deg,#ff0000,#00ff00,#0000ff,#ff0000);background-size:300% 300%;animation:btnFire 3s ease infinite;color:#fff;border-radius:10px;padding:8px;font-size:11px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.2s;margin-bottom:7px;box-shadow:0 4px 15px rgba(255,0,0,0.2)}
.rgb-btn:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(255,0,0,0.3)}
.rgb-btn.off{background:var(--accent-d);color:var(--t2);animation:none;box-shadow:none}
.rgb-btn.off:hover{background:var(--card-b);color:var(--t1)}
.support-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:linear-gradient(135deg,#FF6B35,#FF4500);color:#fff;border-radius:10px;padding:8px;font-size:12px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.2s;margin-bottom:7px;box-shadow:0 4px 15px rgba(255,80,20,0.2)}
.support-btn:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(255,80,20,0.3)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:10px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.2s}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:56px;background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
.mob-top .ml{display:flex;align-items:center;gap:10px}
.mob-logo{width:32px;height:32px;border-radius:10px;background:linear-gradient(135deg,#FF6B35,#FF4500);display:flex;align-items:center;justify-content:center;font-size:17px}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:36px;height:36px;border-radius:9px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s}
.menu-btn:hover,.theme-mob:hover{background:var(--card-b);color:var(--t1)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 30px 40px;min-width:0;transition:margin .3s}
.pg{display:none;animation:pageIn .35s ease}
.pg.on{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.topbar{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:22px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:10px}
.tb-title i{background:linear-gradient(135deg,#FF8C00,#FF4500);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:24px}
.tb-sub{font-size:12px;color:var(--t3);margin-top:2px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:4px 12px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-purple{background:var(--purple-bg);color:#A78BFA}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-pink{background:var(--pink-bg);color:var(--pink)}
.bg-fire{background:rgba(255,80,20,0.12);color:#FF8C00}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}

.stats-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-bottom:22px}
.stat-card{background:var(--card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 16px;transition:all .3s;text-align:center;position:relative;overflow:hidden}
.stat-card:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}
.stat-card .icon{font-size:28px;margin-bottom:6px;display:block}
.stat-card .number{font-size:28px;font-weight:800;color:var(--t1);line-height:1.2}
.stat-card .label{font-size:11px;color:var(--t3);margin-top:4px;font-weight:500}
.stat-card .sub{font-size:9px;color:var(--t3);margin-top:2px;opacity:.6}
.stat-card .bar{position:absolute;bottom:0;right:0;left:0;height:3px;background:linear-gradient(90deg,#FF6B35,#FF4500);opacity:0;transition:.3s}
.stat-card:hover .bar{opacity:1}

.user-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}
.user-card{background:var(--card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:all .3s;box-shadow:var(--shadow);position:relative;overflow:hidden}
.user-card::before{content:'';position:absolute;top:-50%;right:-50%;width:200px;height:200px;background:radial-gradient(circle,rgba(255,80,20,0.03),transparent 70%);pointer-events:none}
.user-card:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 12px 40px rgba(0,0,0,0.3)}
.user-card .head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.user-card .name{font-size:14px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:6px}
.user-card .status{font-size:10px;font-weight:700;padding:3px 12px;border-radius:12px}
.user-card .status.on{background:var(--green-bg);color:var(--green-t)}
.user-card .status.off{background:var(--red-bg);color:var(--red-t)}
.user-card .uuid{font-family:monospace;font-size:9.5px;color:var(--t3);margin-bottom:8px;word-break:break-all}
.user-card .info{display:flex;justify-content:space-between;font-size:11px;color:var(--t2);gap:8px;flex-wrap:wrap;margin-bottom:6px}
.user-card .quota-info{display:flex;justify-content:space-between;font-size:11px;color:var(--t2);margin-bottom:4px}
.user-card .quota-bar{height:6px;border-radius:4px;background:var(--accent-d);overflow:hidden;margin-bottom:10px}
.user-card .quota-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,#FF6B35,#FF4500);transition:width .6s ease}
.user-card .actions{display:flex;gap:5px;flex-wrap:wrap;margin-top:8px}
.user-card .actions .btn{flex:1;justify-content:center;min-width:fit-content;font-size:10px}
.user-card .lock-badge{display:inline-flex;align-items:center;gap:3px;font-size:9px;color:var(--amber-t);background:var(--amber-bg);padding:2px 8px;border-radius:10px;border:1px solid rgba(245,158,11,0.15)}
.user-card .warning-box{background:rgba(239,68,68,0.05);border:1px solid rgba(239,68,68,0.12);border-radius:6px;padding:5px 8px;margin-top:6px;font-size:7.5px;color:var(--red-t);font-family:monospace;white-space:pre-wrap;max-height:50px;overflow-y:auto;direction:ltr;text-align:left;line-height:1.4}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:38px;opacity:.3;display:block;margin-bottom:12px}

.btn{font-family:inherit;font-size:11.5px;font-weight:600;border-radius:10px;padding:8px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .2s;white-space:nowrap}
.btn i{font-size:13px}
.btn-p{background:linear-gradient(135deg,#FF6B35,#FF4500,#FF8C00);background-size:200% 200%;animation:btnFire 3s ease infinite;color:#fff;box-shadow:0 4px 20px rgba(255,80,20,.2)}
@keyframes btnFire{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(255,80,20,.35)}
.btn-o{background:var(--card);backdrop-filter:blur(10px);border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(255,80,20,.2)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.2)}
.btn-pur:hover{background:rgba(139,92,246,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.2)}
.btn-amber:hover{background:rgba(245,158,11,0.22)}
.btn-sm{padding:5px 10px;font-size:10px;border-radius:8px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:8px}

.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:12px 22px;font-size:12.5px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;box-shadow:var(--shadow);white-space:nowrap;display:flex;align-items:center;gap:8px}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(8px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-b);border-radius:20px;padding:30px 28px;max-width:540px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:pageIn .3s ease;box-shadow:var(--shadow)}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:32px;height:32px;border-radius:9px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.2s}
.modal-close:hover{background:var(--red-bg);color:var(--red-t);transform:rotate(90deg)}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:20px;display:flex;align-items:center;gap:8px}
.modal-title i{background:linear-gradient(135deg,#FF8C00,#FF4500);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:18px}
.fg{display:flex;flex-direction:column;gap:5px;margin-bottom:12px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;display:flex;align-items:center;gap:4px}
.fi{width:100%;padding:10px 14px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.2s}
.fi:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(255,80,20,.08);background:rgba(0,0,0,.3)}
.fi::placeholder{color:var(--t3)}
select.fi{appearance:none;cursor:pointer}

.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px;transition:.2s}
.conn-card:hover{border-color:var(--card-bh)}
.conn-card .ip{font-family:monospace;font-size:13px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-card .label{font-size:10px;color:var(--t3);margin-top:2px}
.conn-card .conn-info{display:flex;justify-content:space-between;margin-top:8px;font-size:10px;color:var(--t2);gap:6px;flex-wrap:wrap}
.conn-status-dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:#34D399;animation:pulse 1.5s infinite;margin-right:3px}

.settings-card{background:var(--card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:24px;max-width:500px}
.settings-card .title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.settings-card .title i{color:var(--accent)}
.settings-card .field{margin-bottom:14px}
.settings-card .field label{font-size:11px;color:var(--t3);display:block;margin-bottom:4px;font-weight:600}
.settings-card .field input{width:100%;padding:10px 14px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:13px;outline:none;transition:.2s}
.settings-card .field input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(255,80,20,.08)}
.settings-card .field input::placeholder{color:var(--t3)}
.settings-card .btn{width:100%;justify-content:center;margin-top:4px}
.settings-card .toggle-row{display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--card-b)}
.settings-card .toggle-row .toggle-label{font-size:13px;color:var(--t2);display:flex;align-items:center;gap:8px}
.settings-card .toggle-row .toggle-label i{font-size:18px}
.switch{position:relative;width:48px;height:26px;background:var(--t3);border-radius:13px;cursor:pointer;transition:.3s;flex-shrink:0}
.switch.on{background:linear-gradient(135deg,#FF6B35,#FF4500)}
.switch .slider{position:absolute;top:2px;right:2px;width:22px;height:22px;background:#fff;border-radius:50%;transition:.3s;box-shadow:0 2px 8px rgba(0,0,0,0.2)}
.switch.on .slider{right:24px}

@media(max-width:1200px){.stats-grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:900px){.stats-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:768px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0)}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .user-grid{grid-template-columns:1fr}
  .stats-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:500px){.stats-grid{grid-template-columns:1fr}.main{padding:64px 12px 30px}}
</style>
</head>
<body>
<div class="fire-glow fg1"></div>
<div class="fire-glow fg2"></div>
<div class="fire-glow fg3"></div>
<div class="toast" id="toast"></div>

<!-- ===== مودال ساخت کانفیگ ===== -->
<div class="modal-bg" id="modal-user">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-user')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> 🦅 ساخت کانفیگ جدید</div>
    
    <div class="fg"><label><i class="ti ti-tag"></i> نام کاربری</label><input class="fi" id="user-label" placeholder="مثلاً: کاربر علی"></div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-database"></i> حجم</label><input class="fi" id="user-quota" type="number" min="0.5" step="0.5" value="2"></div>
      <div class="fg"><label><i class="ti ti-ruler"></i> واحد</label><select class="fi" id="user-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> انقضا (روز)</label><input class="fi" id="user-exp" type="number" min="0" value="30" placeholder="0=نامحدود"></div>
    </div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-fingerprint"></i> فینگرپرینت</label><select class="fi" id="user-fingerprint"><option value="chrome">Chrome</option><option value="firefox">Firefox</option><option value="safari">Safari</option><option value="edge">Edge</option><option value="random">Random</option><option value="none">None</option></select></div>
      <div class="fg"><label><i class="ti ti-devices"></i> محدودیت دستگاه</label><input class="fi" id="user-devices" type="number" min="0" max="10" value="1" placeholder="0=نامحدود"></div>
    </div>
    
    <div class="fg"><label><i class="ti ti-settings"></i> پروتکل</label><select class="fi" id="user-protocol"><option value="vless-ws">VLESS (WebSocket)</option><option value="xhttp-stream-up">XHTTP (Stream)</option></select></div>
    
    <div class="fg">
      <label><i class="ti ti-plug"></i> پورت (پیش‌فرض: 443)</label>
      <input class="fi" id="user-port" type="number" min="1" max="65535" value="443" placeholder="443">
    </div>
    
    <div class="fg">
      <label><i class="ti ti-lock"></i> رمز کانفیگ (اختیاری)</label>
      <input class="fi" id="user-password" type="password" placeholder="برای حذف/ویرایش نیاز است" dir="ltr">
    </div>
    
    <div style="display:flex;gap:8px;margin-top:16px">
      <button class="btn btn-p" onclick="saveUser()" style="flex:2"><i class="ti ti-check"></i> ساخت کانفیگ</button>
      <button class="btn btn-o" onclick="closeModal('modal-user')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<!-- ===== مودال ویرایش ===== -->
<div class="modal-bg" id="modal-edit">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> 🦅 ویرایش کانفیگ</div>
    <input type="hidden" id="edit-uuid">
    
    <div class="fg" id="edit-password-section">
      <label><i class="ti ti-lock"></i> 🔑 رمز کانفیگ (برای ویرایش لازم است)</label>
      <input class="fi" id="edit-password" type="password" placeholder="رمز کانفیگ را وارد کنید" dir="ltr">
    </div>
    
    <div class="fg"><label><i class="ti ti-tag"></i> نام کاربری</label><input class="fi" id="edit-label" placeholder="نام کاربری"></div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-database"></i> حجم (0=نامحدود)</label><input class="fi" id="edit-quota" type="number" min="0" step="0.5"></div>
      <div class="fg"><label><i class="ti ti-ruler"></i> واحد</label><select class="fi" id="edit-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> انقضا (روز)</label><input class="fi" id="edit-exp" type="number" min="0" placeholder="0=نامحدود"></div>
    </div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-fingerprint"></i> فینگرپرینت</label><select class="fi" id="edit-fingerprint"><option value="chrome">Chrome</option><option value="firefox">Firefox</option><option value="safari">Safari</option><option value="edge">Edge</option><option value="random">Random</option><option value="none">None</option></select></div>
      <div class="fg"><label><i class="ti ti-devices"></i> محدودیت دستگاه</label><input class="fi" id="edit-devices" type="number" min="0" max="10" placeholder="0=نامحدود"></div>
    </div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div class="fg"><label><i class="ti ti-settings"></i> پروتکل</label>
        <select class="fi" id="edit-protocol">
          <option value="vless-ws">VLESS (WebSocket)</option>
          <option value="xhttp-stream-up">XHTTP (Stream)</option>
        </select>
      </div>
      <div class="fg"><label><i class="ti ti-toggle-left"></i> وضعیت</label>
        <select class="fi" id="edit-status">
          <option value="true">✅ فعال</option>
          <option value="false">❌ غیرفعال</option>
        </select>
      </div>
    </div>
    
    <div class="fg">
      <label><i class="ti ti-plug"></i> پورت</label>
      <input class="fi" id="edit-port" type="number" min="1" max="65535" placeholder="443">
    </div>
    
    <div style="display:flex;gap:8px;margin-top:16px">
      <button class="btn btn-p" onclick="saveEdit()" style="flex:2"><i class="ti ti-check"></i> ذخیره تغییرات</button>
      <button class="btn btn-o" onclick="closeModal('modal-edit')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<!-- ===== مودال حذف ===== -->
<div class="modal-bg" id="modal-delete">
  <div class="modal" style="max-width:400px">
    <button class="modal-close" onclick="closeModal('modal-delete')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-trash"></i> 🦅 حذف کانفیگ</div>
    <input type="hidden" id="delete-uuid">
    <p style="font-size:13px;color:var(--t2);margin-bottom:16px">برای حذف این کانفیگ، رمز آن را وارد کنید.</p>
    <div class="fg">
      <label><i class="ti ti-lock"></i> رمز کانفیگ</label>
      <input class="fi" id="delete-password" type="password" placeholder="رمز کانفیگ را وارد کنید" dir="ltr">
    </div>
    <div style="display:flex;gap:8px;margin-top:16px">
      <button class="btn btn-d" onclick="confirmDelete()" style="flex:2"><i class="ti ti-trash"></i> حذف</button>
      <button class="btn btn-o" onclick="closeModal('modal-delete')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<!-- ===== هدر موبایل ===== -->
<div class="mob-top">
  <div class="ml"><div class="mob-logo">🦅</div><span class="mob-title">پنل عقاب</span></div>
  <div class="mob-right"><button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-palette" id="theme-mob-icon"></i></button><button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button></div>
</div>
<div class="overlay" id="overlay"></div>

<!-- ===== سایدبار ===== -->
<aside class="sidebar" id="sb">
  <div class="logo"><div class="logo-icon">🦅</div><div><div class="logo-name">پنل عقاب</div><div class="logo-sub">مدیریت کاربران</div></div></div>
  <div class="nav-wrap">
    <div class="nav-it on" data-pg="users"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات زنده</div>
    <div class="nav-it" data-pg="support"><i class="ti ti-headset"></i> پشتیبانی</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-it" data-pg="backup"><i class="ti ti-database"></i> بکاپ</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-palette" id="theme-icon"></i> <span id="theme-label">تغییر تم</span></button>
    <button class="rgb-btn off" id="rgb-btn" onclick="toggleRGB()"><i class="ti ti-color-swatch"></i> <span id="rgb-label">تم RGB</span></button>
    <button class="support-btn" onclick="window.open('https://t.me/+QyEVU0FquFczYjQ0','_blank')"><i class="ti ti-brand-telegram"></i> گروه پشتیبانی</button>
    <button class="logout-btn" onclick="logout()"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>

<!-- ===== محتوای اصلی ===== -->
<main class="main">
<section class="pg on" id="pg-users">
  <div class="topbar">
    <div>
      <div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد عقاب</div>
      <div class="tb-sub" id="last-update">آخرین بروزرسانی: لحظه‌ای</div>
    </div>
    <div class="tb-right">
      <span class="badge bg-fire" id="online-badge"><span class="dot dg"></span> ۰ آنلاین</span>
      <button class="btn btn-p" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> کانفیگ جدید</button>
    </div>
  </div>

  <div class="stats-grid">
    <div class="stat-card"><span class="icon">🔥</span><div class="number" id="online-count">۰</div><div class="label">سرویس‌های آنلاین</div><div class="sub">در حال اتصال</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">👥</span><div class="number" id="total-users">۰</div><div class="label">کل کاربران</div><div class="sub">ثبت‌شده</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">📊</span><div class="number" id="total-usage">۰</div><div class="label">مصرف کل</div><div class="sub">مگابایت</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">📱</span><div class="number" id="active-devices">۰</div><div class="label">دستگاه‌های فعال</div><div class="sub">متصل</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">⛔</span><div class="number" id="inactive-count">۰</div><div class="label">غیرفعال</div><div class="sub">غیرفعال</div><div class="bar"></div></div>
    <div class="stat-card"><span class="icon">🏆</span><div class="number" id="top-user-label" style="font-size:16px">-</div><div class="label">پر مصرف‌ترین کاربر</div><div class="sub" id="top-user-usage">۰</div><div class="bar"></div></div>
  </div>

  <div id="users-grid" class="user-grid"><div class="empty"><i class="ti ti-users"></i><p>هیچ کاربری ساخته نشده</p></div></div>
</section>

<section class="pg" id="pg-connections">
  <div class="topbar"><div><div class="tb-title">🔌 اتصالات زنده</div><div class="tb-sub" id="conn-count">۰ اتصال</div></div><div class="tb-right"><span class="badge bg-green" id="conn-live-badge"><span class="dot dg pulse"></span> فعال</span><button class="btn btn-sm btn-o" onclick="loadConnections()"><i class="ti ti-refresh"></i> بروزرسانی</button></div></div>
  <div id="conns-grid" class="conn-grid"><div class="empty"><i class="ti ti-plug-off"></i><p>هیچ اتصال فعالی وجود ندارد</p></div></div>
</section>

<section class="pg" id="pg-support">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> پشتیبانی</div><div class="tb-sub">راهنمایی و پشتیبانی سریع</div></div></div>
  <div style="background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:24px;max-width:600px">
    <div style="font-size:16px;font-weight:700;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px"><i class="ti ti-messages" style="color:var(--accent)"></i> ارتباط با پشتیبانی</div>
    <p style="font-size:13px;color:var(--t2);line-height:1.9;margin-bottom:16px">برای دریافت راهنمایی، پشتیبانی و پاسخ به سوالات خود، به گروه تلگرامی ما بپیوندید.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn btn-p" onclick="window.open('https://t.me/+QyEVU0FquFczYjQ0','_blank')" style="flex:2"><i class="ti ti-brand-telegram"></i> عضویت در گروه پشتیبانی</button>
      <button class="btn btn-o" onclick="navigator.clipboard.writeText('https://t.me/+QyEVU0FquFczYjQ0').then(()=>toast('لینک گروه کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک</button>
    </div>
    <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--card-b);display:flex;align-items:center;gap:10px;flex-wrap:wrap">
      <span class="badge bg-green"><span class="dot dg"></span> آنلاین</span>
      <span style="font-size:11px;color:var(--t3)">گروه پشتیبانی عقاب · پاسخگویی سریع</span>
    </div>
  </div>
</section>

<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات پنل</div><div class="tb-sub">تنظیمات ظاهری و مدیریتی</div></div></div>
  <div class="settings-card">
    <div class="title"><i class="ti ti-color-swatch"></i> تنظیمات ظاهری</div>
    <div class="toggle-row">
      <div class="toggle-label"><i class="ti ti-color-palette" style="background:linear-gradient(135deg,#ff0000,#00ff00,#0000ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent"></i> تم RGB متحرک</div>
      <div class="switch" id="rgb-switch" onclick="toggleRGB()">
        <div class="slider"></div>
      </div>
    </div>
    <div style="margin-top:12px;font-size:10px;color:var(--t3)">💡 با فعال کردن این گزینه، رنگ پنل هر ۲ ثانیه به صورت آرام تغییر میکند</div>
  </div>
</section>

<section class="pg" id="pg-backup">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-database"></i> مدیریت بکاپ</div><div class="tb-sub">ذخیره و بازیابی اطلاعات</div></div></div>
  <div class="settings-card">
    <div class="title"><i class="ti ti-download"></i> بکاپ‌گیری</div>
    <p style="font-size:12px;color:var(--t2);margin-bottom:16px;line-height:1.8">از اطلاعات کاربران، کانفیگ‌ها و تنظیمات بکاپ بگیرید.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn btn-p" onclick="createBackup()" style="flex:2"><i class="ti ti-download"></i> دانلود بکاپ</button>
      <button class="btn btn-o" onclick="document.getElementById('restore-input').click()" style="flex:1"><i class="ti ti-upload"></i> بازیابی</button>
      <input type="file" id="restore-input" accept=".json" style="display:none" onchange="restoreBackup(event)">
    </div>
    <div style="margin-top:12px;font-size:10px;color:var(--t3)">📁 فایل بکاپ با فرمت JSON ذخیره می‌شود</div>
  </div>
</section>
</main>

<script>
// ===== تنظیمات تم =====
let currentTheme = localStorage.getItem('eagle-theme') || 'dark';
function applyTheme(theme) {
  currentTheme = theme;
  localStorage.setItem('eagle-theme', theme);
  document.documentElement.setAttribute('data-theme', theme);
  const icon = document.getElementById('theme-icon');
  const mobIcon = document.getElementById('theme-mob-icon');
  const label = document.getElementById('theme-label');
  icon.className = 'ti ' + (theme === 'dark' ? 'ti-moon' : 'ti-sun');
  if (mobIcon) mobIcon.className = 'ti ' + (theme === 'dark' ? 'ti-moon' : 'ti-sun');
  label.textContent = theme === 'dark' ? 'تم آتشین تیره' : 'تم آتشین روشن';
}
function toggleTheme() {
  const next = currentTheme === 'dark' ? 'white' : 'dark';
  applyTheme(next);
}
applyTheme(currentTheme);

// ===== تم RGB =====
let rgbMode = false;

async function loadRGBStatus() {
  try {
    const r = await authF('/api/settings');
    const data = await r.json();
    rgbMode = data.rgb_mode || false;
    updateRGBUI();
  } catch(e) {}
}

function updateRGBUI() {
  const btn = document.getElementById('rgb-btn');
  const label = document.getElementById('rgb-label');
  const sw = document.getElementById('rgb-switch');
  
  if (rgbMode) {
    document.body.classList.add('rgb-mode');
    btn.classList.remove('off');
    btn.style.background = 'linear-gradient(135deg,#ff0000,#00ff00,#0000ff,#ff0000)';
    btn.style.backgroundSize = '300% 300%';
    btn.style.animation = 'btnFire 3s ease infinite';
    label.textContent = 'RGB: روشن';
    sw.classList.add('on');
  } else {
    document.body.classList.remove('rgb-mode');
    btn.classList.add('off');
    btn.style.background = '';
    btn.style.animation = '';
    label.textContent = 'تم RGB';
    sw.classList.remove('on');
  }
}

async function toggleRGB() {
  const newState = !rgbMode;
  try {
    const r = await authF('/api/settings/rgb', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ enabled: newState })
    });
    const data = await r.json();
    rgbMode = data.rgb_mode;
    updateRGBUI();
    toast(rgbMode ? '🌈 تم RGB فعال شد' : '🌙 تم RGB غیرفعال شد', 'ok');
  } catch(e) {
    toast('خطا در تغییر تنظیمات', 'err');
  }
}

// ===== توابع کمکی =====
function toast(msg, type='') {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show' + (type ? ' ' + type : '');
  setTimeout(() => t.classList.remove('show'), 2500);
}

function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
  return (b/1024**3).toFixed(2) + ' GB';
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }

// ===== احراز هویت =====
async function authF(url, opts={}) {
  const r = await fetch(url, opts);
  if (r.status === 401) { location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

async function logout() {
  try { await fetch('/api/logout', {method:'POST'}); } catch(e) {}
  location.href = '/login';
}

// ===== ناوبری =====
function navTo(name) {
  document.querySelectorAll('.nav-it').forEach(n => n.classList.toggle('on', n.dataset.pg === name));
  document.querySelectorAll('.pg').forEach(p => p.classList.toggle('on', p.id === 'pg-' + name));
  closeSb();
  if (name === 'users') loadUsers();
  if (name === 'connections') loadConnections();
}

document.querySelectorAll('.nav-it').forEach(el => {
  el.addEventListener('click', () => navTo(el.dataset.pg));
});

const sb = document.getElementById('sb'), overlay = document.getElementById('overlay');
function openSb(){ sb.classList.add('open'); overlay.classList.add('show'); }
function closeSb(){ sb.classList.remove('open'); overlay.classList.remove('show'); }
document.getElementById('open-sb').addEventListener('click', openSb);
overlay.addEventListener('click', closeSb);

// ===== بارگذاری کاربران =====
async function loadUsers() {
  try {
    const r = await authF('/api/links');
    const { links=[] } = await r.json();
    const grid = document.getElementById('users-grid');
    
    const total = links.length;
    const online = links.filter(l => l.active && !l.expired).length;
    const inactive = links.filter(l => !l.active || l.expired).length;
    const totalBytes = links.reduce((sum, l) => sum + (l.used_bytes || 0), 0);
    const devices = links.reduce((sum, l) => sum + (l.max_devices || 0), 0);
    
    document.getElementById('total-users').textContent = total;
    document.getElementById('online-count').textContent = online;
    document.getElementById('inactive-count').textContent = inactive;
    document.getElementById('total-usage').textContent = (totalBytes / (1024*1024)).toFixed(1);
    document.getElementById('active-devices').textContent = devices;
    document.getElementById('last-update').textContent = 'آخرین بروزرسانی: ' + new Date().toLocaleTimeString('fa-IR');
    document.getElementById('online-badge').innerHTML = '<span class="dot dg"></span> ' + online + ' آنلاین';
    
    try {
      const sr = await authF('/stats');
      const statsData = await sr.json();
      if (statsData.top_user) {
        document.getElementById('top-user-label').textContent = '🦅 ' + statsData.top_user.label;
        document.getElementById('top-user-usage').textContent = statsData.top_user.used_fmt || '0';
      } else {
        document.getElementById('top-user-label').textContent = '—';
        document.getElementById('top-user-usage').textContent = '۰';
      }
    } catch(e) {}
    
    if (!links.length) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-users"></i><p>هیچ کاربری ساخته نشده</p></div>';
      return;
    }
    
    const host = window.location.host;
    grid.innerHTML = links.map(l => {
      const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
      const bc = pct > 90 ? '#EF4444' : pct > 70 ? '#F59E0B' : '#FF6B35';
      const active = l.active && !l.expired;
      const fp = l.fingerprint || 'chrome';
      const subLink = `https://${host}/sub/${l.uuid}`;
      const hasPassword = l.has_password === true;
      const port = l.port || 443;
      const warningText = l.warning_config || '';
      
      const todayBytes = l.today_bytes || 0;
      const todayFmt = fmtB(todayBytes);
      const lastSeen = l.last_connected_at ? new Date(l.last_connected_at).toLocaleString('fa-IR') : '—';
      const statusText = active ? '🟢 آنلاین' : '🔴 آفلاین';
      const statusClass = active ? 'on' : 'off';
      
      return `<div class="user-card">
        <div class="head">
          <div class="name">🦅 ${esc(l.label)} ${hasPassword ? '<span class="lock-badge"><i class="ti ti-lock"></i> رمزدار</span>' : ''}</div>
          <span class="status ${statusClass}">${statusText}</span>
        </div>
        <div class="uuid">🔑 ${esc(l.uuid)}</div>
        <div class="info">
          <span>📊 امروز: ${todayFmt}</span>
          <span>📅 آخرین اتصال: ${lastSeen}</span>
          <span>📱 ${l.max_devices === 0 ? '∞' : l.max_devices + ' دستگاه'}</span>
          <span>🔌 ${port}</span>
        </div>
        <div class="quota-info">
          <span>📊 مصرف: ${fmtB(l.used_bytes)}</span>
          <span>📦 کل: ${l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes)}</span>
        </div>
        <div class="quota-bar">
          <div class="quota-fill" style="width: ${pct}%; background: ${bc}"></div>
        </div>
        ${warningText ? `<div class="warning-box">${esc(warningText)}</div>` : ''}
        <div class="actions">
          <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))"><i class="ti ti-copy"></i> لینک</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(subLink)}').then(()=>toast('ساب‌لینک کپی شد','ok'))"><i class="ti ti-link"></i> ساب</button>
          <button class="btn btn-sm btn-amber" onclick="resetUsage('${l.uuid}')"><i class="ti ti-rotate"></i> ریست</button>
          <button class="btn btn-sm btn-pur btn-icon" onclick="openEditModal('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
          <button class="btn btn-sm btn-d" onclick="openDeleteModal('${l.uuid}')"><i class="ti ti-trash"></i></button>
        </div>
      </div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== باز کردن مودال ویرایش =====
async function openEditModal(uuid) {
    try {
        const r = await authF('/api/links');
        const { links=[] } = await r.json();
        const link = links.find(l => l.uuid === uuid);
        
        if (!link) {
            toast('کاربر یافت نشد', 'err');
            return;
        }
        
        document.getElementById('edit-uuid').value = uuid;
        document.getElementById('edit-label').value = link.label || '';
        document.getElementById('edit-password').value = '';
        
        if (link.limit_bytes === 0) {
            document.getElementById('edit-quota').value = '';
        } else {
            document.getElementById('edit-quota').value = (link.limit_bytes / (1024**3)).toFixed(1);
        }
        document.getElementById('edit-unit').value = 'GB';
        
        if (link.expires_at) {
            const days = Math.ceil((new Date(link.expires_at) - new Date()) / (1000 * 60 * 60 * 24));
            document.getElementById('edit-exp').value = days > 0 ? days : 0;
        } else {
            document.getElementById('edit-exp').value = '';
        }
        
        document.getElementById('edit-fingerprint').value = link.fingerprint || 'chrome';
        document.getElementById('edit-devices').value = link.max_devices || 0;
        document.getElementById('edit-protocol').value = link.protocol || 'vless-ws';
        document.getElementById('edit-status').value = link.active ? 'true' : 'false';
        document.getElementById('edit-port').value = link.port || 443;
        
        if (link.has_password) {
            document.getElementById('edit-password-section').style.display = 'block';
        } else {
            document.getElementById('edit-password-section').style.display = 'none';
        }
        
        openModal('modal-edit');
    } catch(e) {
        toast('خطا در بارگذاری', 'err');
    }
}

// ===== ذخیره ویرایش =====
async function saveEdit() {
    const uuid = document.getElementById('edit-uuid').value;
    const password = document.getElementById('edit-password').value.trim();
    const label = document.getElementById('edit-label').value.trim() || 'کاربر';
    const quota = parseFloat(document.getElementById('edit-quota').value) || 0;
    const unit = document.getElementById('edit-unit').value || 'GB';
    const exp = parseInt(document.getElementById('edit-exp').value) || 0;
    const fingerprint = document.getElementById('edit-fingerprint').value || 'chrome';
    const devices = parseInt(document.getElementById('edit-devices').value) || 0;
    const protocol = document.getElementById('edit-protocol').value || 'vless-ws';
    const active = document.getElementById('edit-status').value === 'true';
    const port = parseInt(document.getElementById('edit-port').value) || 443;
    
    try {
        const r = await authF('/api/links/' + uuid, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                label: label,
                limit_value: quota,
                limit_unit: unit,
                expires_days: exp,
                fingerprint: fingerprint,
                max_devices: devices,
                protocol: protocol,
                active: active,
                password: password,
                port: port
            })
        });
        
        if (!r.ok) {
            const err = await r.json().catch(() => ({}));
            if (r.status === 403) {
                toast('❌ رمز کانفیگ اشتباه است!', 'err');
            } else {
                throw new Error(err.detail || 'خطا');
            }
            return;
        }
        
        closeModal('modal-edit');
        toast('🦅 کانفیگ ویرایش شد ✓', 'ok');
        loadUsers();
    } catch(e) {
        toast('خطا در ویرایش: ' + e.message, 'err');
    }
}

// ===== باز کردن مودال حذف =====
function openDeleteModal(uuid) {
    document.getElementById('delete-uuid').value = uuid;
    document.getElementById('delete-password').value = '';
    openModal('modal-delete');
}

// ===== تایید حذف با رمز =====
async function confirmDelete() {
    const uuid = document.getElementById('delete-uuid').value;
    const password = document.getElementById('delete-password').value.trim();
    
    try {
        const r = await authF('/api/links/' + uuid, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password: password })
        });
        
        if (!r.ok) {
            const err = await r.json().catch(() => ({}));
            if (r.status === 403) {
                toast('❌ رمز کانفیگ اشتباه است!', 'err');
            } else {
                throw new Error(err.detail || 'خطا');
            }
            return;
        }
        
        closeModal('modal-delete');
        toast('🦅 کاربر حذف شد', 'ok');
        loadUsers();
    } catch(e) {
        toast('خطا در حذف: ' + e.message, 'err');
    }
}

// ===== ساخت کانفیگ جدید =====
async function saveUser() {
  const label = document.getElementById('user-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('user-quota').value) || 2;
  const unit = document.getElementById('user-unit').value || 'GB';
  const exp = parseInt(document.getElementById('user-exp').value) || 0;
  const fingerprint = document.getElementById('user-fingerprint').value || 'chrome';
  const devices = parseInt(document.getElementById('user-devices').value) || 0;
  const protocol = document.getElementById('user-protocol').value || 'vless-ws';
  const password = document.getElementById('user-password').value.trim();
  const port = parseInt(document.getElementById('user-port').value) || 443;
  
  try {
    const r = await authF('/api/links', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        label,
        limit_value: quota,
        limit_unit: unit,
        expires_days: exp,
        fingerprint: fingerprint,
        max_devices: devices,
        protocol: protocol,
        note: '',
        password: password,
        port: port
      })
    });
    if (!r.ok) throw new Error();
    
    document.getElementById('user-label').value = '';
    document.getElementById('user-quota').value = '2';
    document.getElementById('user-unit').value = 'GB';
    document.getElementById('user-exp').value = '30';
    document.getElementById('user-fingerprint').value = 'chrome';
    document.getElementById('user-devices').value = '1';
    document.getElementById('user-protocol').value = 'vless-ws';
    document.getElementById('user-password').value = '';
    document.getElementById('user-port').value = '443';
    
    closeModal('modal-user');
    toast('🦅 کانفیگ ساخته شد ✓', 'ok');
    loadUsers();
  } catch(e) {
    toast('خطا در ساخت', 'err');
  }
}

// ===== ریست مصرف =====
async function resetUsage(uuid) {
  if (!confirm('مصرف این کاربر ریست شود؟')) return;
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reset_usage: true })
    });
    if (!r.ok) throw new Error();
    toast('مصرف ریست شد ✓', 'ok');
    loadUsers();
  } catch(e) { toast('خطا', 'err'); }
}

// ===== اتصالات زنده =====
async function loadConnections() {
  try {
    const r = await authF('/api/connections');
    const d = await r.json();
    const grid = document.getElementById('conns-grid');
    const count = d.count || 0;
    document.getElementById('conn-count').textContent = count + ' اتصال';
    
    if (!count) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-plug-off"></i><p>هیچ اتصال فعالی وجود ندارد</p></div>';
      return;
    }
    
    grid.innerHTML = d.connections.map(c => {
      const secs = c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0;
      const dur = secs < 60 ? secs + ' ث' : secs < 3600 ? Math.floor(secs/60) + ' د' : Math.floor(secs/3600) + ' س';
      return `<div class="conn-card">
        <div class="ip"><span class="conn-status-dot"></span> ${esc(c.ip)}</div>
        <div class="label">${esc(c.label || 'نامشخص')}</div>
        <div class="conn-info">
          <span>📥 ${esc(c.bytes_fmt || '0 B')}</span>
          <span>⏱ ${dur}</span>
        </div>
      </div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== بکاپ =====
async function createBackup() {
  try {
    const r = await authF('/api/backup');
    const data = await r.json();
    const blob = new Blob([JSON.stringify(data, null, 2)], {type:'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `eagle_backup_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    toast('✅ بکاپ با موفقیت دانلود شد', 'ok');
  } catch(e) {
    toast('خطا در بکاپ‌گیری', 'err');
  }
}

async function restoreBackup(event) {
  const file = event.target.files[0];
  if (!file) return;
  try {
    const text = await file.text();
    const data = JSON.parse(text);
    const r = await authF('/api/backup/restore', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!r.ok) throw new Error();
    toast('✅ بکاپ با موفقیت بازیابی شد', 'ok');
    setTimeout(() => location.reload(), 1500);
  } catch(e) {
    toast('خطا در بازیابی بکاپ', 'err');
  }
  event.target.value = '';
}

// ===== بارگذاری اولیه =====
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.authenticated) location.href = '/login';
  } catch(e) { location.href = '/login'; }
  
  await loadRGBStatus();
  loadUsers();
  loadConnections();
  
  setInterval(() => {
    if (document.getElementById('pg-users').classList.contains('on')) loadUsers();
    if (document.getElementById('pg-connections').classList.contains('on')) loadConnections();
  }, 5000);
});
</script>
</body></html>"""


# ===== صفحه ساب‌لینک =====
def get_sub_page_html(uuid: str, link: dict) -> str:
    """صفحه ساب‌لینک با اتصالات زنده"""
    
    used = link.get('used_bytes', 0)
    limit = link.get('limit_bytes', 0)
    active = link.get('active', True)
    expired = link.get('expired', False)
    label = link.get('label', 'کاربر')
    fingerprint = link.get('fingerprint', 'chrome')
    max_devices = link.get('max_devices', 0)
    protocol = link.get('protocol', 'vless-ws')
    port = link.get('port', 443)
    active_connections = link.get('active_connections', 0)
    active_connections_list = link.get('active_connections_list', [])
    
    percent = 0
    if limit > 0:
        percent = min(100, (used / limit) * 100)
    
    expires_at = link.get('expires_at')
    if expires_at:
        try:
            from datetime import datetime
            exp_date = datetime.fromisoformat(expires_at.replace('Z', '+00:00'))
            days_left = (exp_date - datetime.now().astimezone()).days
            if days_left < 0:
                days_left = 0
        except:
            days_left = 'نامشخص'
    else:
        days_left = 'نامحدود'
    
    is_allowed = active and not expired
    sub_url = link.get('sub_url', '')
    
    def fmt_bytes(b):
        if not b or b == 0:
            return '0 B'
        if b < 1024:
            return f'{b} B'
        if b < 1024**2:
            return f'{b/1024:.1f} KB'
        if b < 1024**3:
            return f'{b/1024**2:.2f} MB'
        return f'{b/1024**3:.2f} GB'
    
    used_fmt = fmt_bytes(used)
    limit_fmt = 'نامحدود' if limit == 0 else fmt_bytes(limit)
    
    conns_html = ""
    if active_connections > 0:
        conns_html = f"""
        <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:12px;padding:12px 14px;margin:12px 0">
            <div style="display:flex;align-items:center;gap:6px;margin-bottom:8px;font-size:11px;color:#8A4A3A">
                <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#34D399;animation:pulse 1.5s infinite"></span>
                <span style="font-weight:700;color:#34D399">{active_connections} دستگاه متصل</span>
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">
        """
        for conn in active_connections_list[:10]:
            ip = conn.get('ip', 'نامشخص')
            conns_html += f"""
                <span style="font-family:monospace;font-size:10px;background:rgba(255,80,20,0.06);border:1px solid rgba(255,80,20,0.06);padding:3px 10px;border-radius:6px;color:#8A4A3A">🔵 {ip}</span>
            """
        if len(active_connections_list) > 10:
            conns_html += f"""
                <span style="font-family:monospace;font-size:10px;background:rgba(255,80,20,0.04);padding:3px 10px;border-radius:6px;color:#5A3A2A">+{len(active_connections_list)-10} بیشتر</span>
            """
        conns_html += """
            </div>
        </div>
        """
    else:
        conns_html = f"""
        <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:12px;padding:10px 14px;margin:12px 0;text-align:center">
            <span style="font-size:11px;color:#5A3A2A">🔴 بدون اتصال فعال</span>
        </div>
        """
    
    from main import get_host, generate_vless_link
    host = get_host()
    remark = f"عقاب-{label}"
    new_vless_link = generate_vless_link(
        uuid, 
        host, 
        remark=remark,
        protocol=protocol,
        fingerprint=fingerprint,
        port=port
    )
    
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🦅 {label} · پنل عقاب</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
@keyframes fireBG{{
    0%{{background-position:0% 50%}}
    25%{{background-position:50% 0%}}
    50%{{background-position:100% 50%}}
    75%{{background-position:50% 100%}}
    100%{{background-position:0% 50%}}
}}
@keyframes flameFlicker{{
    0%{{opacity:0.6;transform:scale(1) rotate(0deg)}}
    25%{{opacity:0.8;transform:scale(1.02) rotate(2deg)}}
    50%{{opacity:0.5;transform:scale(0.98) rotate(-1deg)}}
    75%{{opacity:0.9;transform:scale(1.01) rotate(1deg)}}
    100%{{opacity:0.6;transform:scale(1) rotate(0deg)}}
}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
body{{
    font-family:'Vazirmatn',sans-serif;
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:20px;
    color:#F0EEFF;
    position:relative;
    overflow-x:hidden;
    background:linear-gradient(135deg,#1a0505,#2a0a0a,#3d0f0a,#2a0505,#1a0a0a);
    background-size:400% 400%;
    animation:fireBG 8s ease infinite;
}}
.fire-particles{{
    position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;
}}
.fire-particle{{
    position:absolute;
    border-radius:50%;
    background:radial-gradient(circle,rgba(255,120,50,0.4),rgba(255,50,0,0));
    width:6px;height:6px;
    animation:floatFire 12s ease-in-out infinite;
}}
@keyframes floatFire{{
    0%{{transform:translateY(100vh) scale(0) rotate(0deg);opacity:0}}
    20%{{opacity:1}}
    80%{{opacity:1}}
    100%{{transform:translateY(-10vh) scale(1.5) rotate(720deg);opacity:0}}
}}
.fire-glow{{
    position:fixed;border-radius:50%;filter:blur(150px);z-index:0;animation:flameFlicker 3s ease-in-out infinite;pointer-events:none;
}}
.glow1{{width:500px;height:500px;background:rgba(255,80,20,0.06);top:-200px;right:-100px}}
.glow2{{width:400px;height:400px;background:rgba(255,150,50,0.05);bottom:-100px;left:-80px;animation-delay:2s}}
.glow3{{width:300px;height:300px;background:rgba(200,50,0,0.04);top:50%;left:50%;transform:translate(-50%,-50%);animation-delay:4s}}
.card{{
    position:relative;z-index:10;
    background:rgba(20,8,8,0.75);
    backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
    border:1px solid rgba(255,100,50,0.15);
    border-radius:28px;
    padding:40px 38px 34px;
    max-width:500px;width:100%;
    box-shadow:0 0 100px rgba(255,80,20,0.05),0 25px 70px rgba(0,0,0,0.7);
    animation:cardIn 0.6s ease;
}}
@keyframes cardIn{{from{{opacity:0;transform:translateY(30px) scale(0.96)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
.brand{{
    display:flex;align-items:center;gap:14px;margin-bottom:28px;
    padding-bottom:18px;border-bottom:1px solid rgba(255,100,50,0.08);
}}
.brand-icon{{
    width:52px;height:52px;border-radius:16px;
    background:linear-gradient(135deg,#FF6B35,#FF4500,#FF8C00);
    display:flex;align-items:center;justify-content:center;
    font-size:28px;flex-shrink:0;
    box-shadow:0 0 50px rgba(255,80,20,0.2),0 0 100px rgba(255,80,20,0.05);
    animation:flameFlicker 2s ease-in-out infinite;
}}
.brand-text .name{{
    font-size:18px;font-weight:800;
    background:linear-gradient(135deg,#FF8C00,#FF4500,#FF6B35);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.brand-text .sub{{font-size:10.5px;color:#8A4A3A;margin-top:2px;-webkit-text-fill-color:#8A4A3A}}
.user-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}}
.user-name{{font-size:24px;font-weight:800;color:#F0EEFF;display:flex;align-items:center;gap:8px}}
.user-name .fire{{font-size:20px}}
.status{{
    display:inline-flex;align-items:center;gap:5px;
    padding:5px 14px;border-radius:20px;
    font-size:12px;font-weight:700;
}}
.status.active{{
    background:rgba(255,80,20,0.12);color:#FF8C00;
    border:1px solid rgba(255,80,20,0.15);
}}
.status.inactive{{
    background:rgba(239,68,68,0.12);color:#F87171;
    border:1px solid rgba(239,68,68,0.15);
}}
.uuid-box{{
    background:rgba(255,255,255,0.02);
    border:1px solid rgba(255,255,255,0.04);
    border-radius:10px;padding:8px 12px;
    font-size:10px;font-family:monospace;color:#8A4A3A;
    word-break:break-all;margin:6px 0 16px;cursor:pointer;transition:.15s;
}}
.uuid-box:hover{{background:rgba(255,80,20,0.05);border-color:rgba(255,80,20,0.1)}}
.info-grid{{display:grid;gap:10px;margin:16px 0}}
.info-item{{
    background:rgba(255,255,255,0.02);
    border:1px solid rgba(255,255,255,0.04);
    border-radius:12px;padding:13px 16px;
    display:flex;justify-content:space-between;align-items:center;
    transition:.15s;
}}
.info-item:hover{{background:rgba(255,255,255,0.03);border-color:rgba(255,255,255,0.06)}}
.info-label{{font-size:12px;color:#8A4A3A;display:flex;align-items:center;gap:6px}}
.info-label i{{font-size:15px;color:#FF6B35}}
.info-value{{font-size:14px;font-weight:700;color:#F0EEFF}}
.info-value.used{{color:#FF8C00}}
.info-value.remain{{color:#34D399}}
.info-value.proto{{
    font-size:11px;
    background:rgba(255,80,20,0.08);
    padding:4px 12px;border-radius:8px;
    border:1px solid rgba(255,80,20,0.08);
}}
.progress{{margin:18px 0 20px}}
.progress-bar{{
    height:7px;border-radius:5px;
    background:rgba(255,255,255,0.05);overflow:hidden;
}}
.progress-fill{{
    height:100%;border-radius:5px;
    background:linear-gradient(90deg,#FF6B35,#FF4500,#FF8C00);
    width:{percent:.1f}%;transition:width 1s ease;
}}
.progress-text{{display:flex;justify-content:space-between;font-size:11px;color:#8A4A3A;margin-top:6px}}
.progress-text .pct{{font-weight:700;color:#F0EEFF}}
.vless-section{{
    background:rgba(255,255,255,0.02);
    border:1px solid rgba(255,255,255,0.04);
    border-radius:12px;padding:14px 16px;margin:16px 0;
}}
.vless-label{{
    font-size:10px;color:#8A4A3A;font-weight:700;
    text-transform:uppercase;letter-spacing:.06em;
    display:flex;align-items:center;gap:6px;margin-bottom:8px;
}}
.vless-label i{{color:#FF6B35;font-size:13px}}
.vless-link{{
    font-family:monospace;font-size:10px;color:#FF8C00;
    word-break:break-all;line-height:1.8;
    background:rgba(0,0,0,0.3);padding:10px 12px;
    border-radius:8px;border:1px solid rgba(255,80,20,0.06);
}}
.actions{{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}}
.btn{{
    font-family:inherit;font-size:12px;font-weight:600;
    border-radius:10px;padding:9px 16px;
    cursor:pointer;display:inline-flex;align-items:center;gap:6px;
    border:none;transition:all .2s;white-space:nowrap;flex:1;justify-content:center;
}}
.btn i{{font-size:14px}}
.btn-primary{{
    background:linear-gradient(135deg,#FF6B35,#FF4500);
    color:#fff;box-shadow:0 4px 20px rgba(255,80,20,0.2);
}}
.btn-primary:hover{{transform:translateY(-2px);box-shadow:0 8px 30px rgba(255,80,20,0.3)}}
.btn-secondary{{
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.06);
    color:#8A4A3A;
}}
.btn-secondary:hover{{background:rgba(255,255,255,0.08);color:#F0EEFF}}
.btn-success{{
    background:rgba(16,185,129,0.1);
    border:1px solid rgba(16,185,129,0.15);
    color:#34D399;
}}
.btn-success:hover{{background:rgba(16,185,129,0.15)}}
.footer{{
    margin-top:22px;padding-top:16px;
    border-top:1px solid rgba(255,255,255,0.03);
    text-align:center;font-size:10px;color:#5A3A2A;
}}
.footer .eagle{{color:#FF6B35;font-weight:700}}
.toast{{
    position:fixed;bottom:30px;left:50%;
    transform:translateX(-50%) translateY(60px);
    background:rgba(20,8,8,0.9);backdrop-filter:blur(20px);
    border:1px solid rgba(255,80,20,0.12);
    color:#F0EEFF;border-radius:12px;
    padding:12px 22px;font-size:13px;
    opacity:0;transition:all .3s;z-index:999;pointer-events:none;
    display:flex;align-items:center;gap:8px;
    box-shadow:0 10px 40px rgba(0,0,0,0.4);
}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,0.2);color:#34D399}}
@media(max-width:520px){{
    .card{{padding:28px 20px 24px}}
    .user-name{{font-size:20px}}
    .brand-icon{{width:44px;height:44px;font-size:22px}}
    .info-item{{padding:11px 14px}}
    .btn{{font-size:11px;padding:8px 12px}}
}}
</style>
</head>
<body>
<div class="fire-particles">
    <div class="fire-particle" style="left:5%;animation-delay:0s;width:8px;height:8px"></div>
    <div class="fire-particle" style="left:15%;animation-delay:2s;width:5px;height:5px"></div>
    <div class="fire-particle" style="left:25%;animation-delay:4s;width:10px;height:10px"></div>
    <div class="fire-particle" style="left:35%;animation-delay:1s;width:6px;height:6px"></div>
    <div class="fire-particle" style="left:45%;animation-delay:5s;width:7px;height:7px"></div>
    <div class="fire-particle" style="left:55%;animation-delay:3s;width:9px;height:9px"></div>
    <div class="fire-particle" style="left:65%;animation-delay:6s;width:5px;height:5px"></div>
    <div class="fire-particle" style="left:75%;animation-delay:2s;width:8px;height:8px"></div>
    <div class="fire-particle" style="left:85%;animation-delay:4s;width:6px;height:6px"></div>
    <div class="fire-particle" style="left:95%;animation-delay:7s;width:7px;height:7px"></div>
</div>
<div class="fire-glow glow1"></div><div class="fire-glow glow2"></div><div class="fire-glow glow3"></div>
<div class="toast" id="toast"></div>
<div class="card">
    <div class="brand">
        <div class="brand-icon">🦅</div>
        <div class="brand-text"><div class="name">پنل عقاب</div><div class="sub">اطلاعات اشتراک</div></div>
    </div>
    <div class="user-header">
        <div class="user-name"><span class="fire">🦅</span> {label}</div>
        <span class="status {'active' if is_allowed else 'inactive'}">
            <i class="ti {'ti-circle-check' if is_allowed else 'ti-circle-x'}"></i>
            {'فعال' if is_allowed else 'غیرفعال'}
        </span>
    </div>
    <div class="uuid-box" onclick="copyUUID()" title="کلیک برای کپی UUID">🔑 {uuid}</div>
    
    {conns_html}
    
    <div class="info-grid">
        <div class="info-item"><span class="info-label"><i class="ti ti-database"></i> مصرف</span><span class="info-value used">{used_fmt}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-package"></i> سهمیه</span><span class="info-value">{limit_fmt}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-calendar"></i> زمان باقیمانده</span><span class="info-value">{days_left if days_left == 'نامحدود' else f'{days_left} روز'}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-devices"></i> دستگاه‌ها</span><span class="info-value">{max_devices if max_devices > 0 else '∞'}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-fingerprint"></i> فینگرپرینت</span><span class="info-value proto">{fingerprint}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-settings"></i> پروتکل</span><span class="info-value proto">{protocol}</span></div>
        <div class="info-item"><span class="info-label"><i class="ti ti-plug"></i> پورت</span><span class="info-value proto">{port}</span></div>
    </div>
    <div class="progress">
        <div class="progress-bar"><div class="progress-fill" style="width:{percent:.1f}%"></div></div>
        <div class="progress-text"><span>میزان مصرف</span><span class="pct">{percent:.1f}%</span></div>
    </div>
    <div class="vless-section">
        <div class="vless-label"><i class="ti ti-link"></i> لینک کانفیگ (VLESS)</div>
        <div class="vless-link" id="vless-link">{new_vless_link}</div>
    </div>
    <div class="actions">
        <button class="btn btn-primary" onclick="copyVless()"><i class="ti ti-copy"></i> کپی لینک</button>
        <button class="btn btn-success" onclick="copySub()"><i class="ti ti-link"></i> کپی ساب‌لینک</button>
        <button class="btn btn-secondary" onclick="showQR()"><i class="ti ti-qrcode"></i> QR</button>
    </div>
    <div class="footer"><span class="eagle">🦅</span> پنل عقاب</div>
</div>
<script>
const vless = `{new_vless_link}`;
const subUrl = `{sub_url}`;
const uuid = `{uuid}`;
function toast(msg, type=''){{
    const t=document.getElementById('toast');
    t.textContent=msg;t.className='toast show'+(type?' '+type:'');
    setTimeout(()=>t.classList.remove('show'),2500);
}}
function copyVless(){{navigator.clipboard.writeText(vless).then(()=>toast('✅ لینک کانفیگ کپی شد','ok'));}}
function copySub(){{navigator.clipboard.writeText(subUrl).then(()=>toast('✅ ساب‌لینک کپی شد','ok'));}}
function copyUUID(){{navigator.clipboard.writeText(uuid).then(()=>toast('✅ UUID کپی شد','ok'));}}
function showQR(){{window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(vless),'_blank');}}
</script>
</body></html>"""
