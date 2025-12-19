import os

# ==========================================
# 1. FIXED ASSETS & CONFIGURATION
# ==========================================

# LOGO
logo_svg = """
<svg version="1.1" viewBox="0 0 300 70" class="h-12 w-auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#fbbf24;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
        </linearGradient>
    </defs>
    <g transform="translate(10, 10)">
        <path fill="url(#goldGradient)" d="M25,0 L50,12.5 L50,37.5 L25,50 L0,37.5 L0,12.5 Z" />
        <path fill="#ffffff" d="M18,18 H32 V22 H28 V32 H22 V22 H18 Z" />
    </g>
    <text x="70" y="42" font-family="'Syne', sans-serif" font-weight="800" font-size="32" fill="#ffffff" letter-spacing="-0.5">TRISTAR</text>
    <text x="72" y="56" font-family="'Inter', sans-serif" font-weight="500" font-size="9" fill="#94a3b8" letter-spacing="3" style="text-transform: uppercase;">Group Inc.</text>
</svg>
"""

logo_svg_dark = logo_svg.replace('fill="#ffffff"', 'fill="#0f172a"')

# HEAD
head_html = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tristar Group Inc. | Global Manufacturing Partner</title>
    <meta name="description" content="Tier-1 manufacturer specializing in Injection Moulding, PCB Assembly, and Metal Fabrication.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&family=Space+Grotesk:wght@300;400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { font-family: 'Inter', sans-serif; overflow-x: hidden; }
        h1, h2, h3, h4, .brand-font { font-family: 'Syne', sans-serif; }
        .tech-font { font-family: 'Space Grotesk', sans-serif; }
        .glass-nav { background: rgba(2, 6, 23, 0.7); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .glass-card { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.05); }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0f172a; }
        ::-webkit-scrollbar-thumb { background: #d97706; border-radius: 4px; }
    </style>
</head>
"""

# SCRIPTS
scripts_html = """<script>AOS.init({ duration: 1000, once: true, offset: 50 }); const counters = document.querySelectorAll('.counter'); counters.forEach(counter => { const updateCount = () => { const target = +counter.getAttribute('data-target'); const count = +counter.innerText; const inc = target / 200; if (count < target) { counter.innerText = Math.ceil(count + inc); setTimeout(updateCount, 20); } else { counter.innerText = target; } }; updateCount(); });</script>"""

# NAV
navbar = f"""
<nav class="fixed top-0 w-full z-50 glass-nav transition-all duration-300 py-4">
    <div class="container mx-auto px-6 flex justify-between items-center">
        <a href="index.html" class="transform hover:scale-105 transition duration-300">{logo_svg}</a>
        <div class="hidden lg:flex space-x-12 items-center">
            <a href="index.html" class="text-xs font-bold uppercase tracking-widest text-white hover:text-amber-500 transition">Home</a>
            <div class="group relative py-4">
                <a href="about.html" class="text-xs font-bold uppercase tracking-widest text-white hover:text-amber-500 transition cursor-pointer">Company</a>
                <div class="hidden group-hover:block absolute top-full -left-4 w-48 bg-slate-950 border border-slate-800 p-2 rounded shadow-2xl">
                    <a href="about.html" class="block px-4 py-3 text-xs text-slate-400 hover:text-white hover:bg-slate-900 transition">About Us</a>
                    <a href="sustainability.html" class="block px-4 py-3 text-xs text-slate-400 hover:text-white hover:bg-slate-900 transition">Sustainability</a>
                </div>
            </div>
            <a href="divisions.html" class="text-xs font-bold uppercase tracking-widest text-white hover:text-amber-500 transition">Expertise</a>
            <a href="infrastructure.html" class="text-xs font-bold uppercase tracking-widest text-white hover:text-amber-500 transition">Infrastructure</a>
            <a href="news.html" class="text-xs font-bold uppercase tracking-widest text-white hover:text-amber-500 transition">News</a>
            <a href="contact.html" class="text-xs font-bold uppercase tracking-widest text-white hover:text-amber-500 transition">Contact</a>
        </div>
        <div class="flex items-center space-x-6">
            <a href="login.html" class="text-slate-400 hover:text-white transition" title="Employee Portal"><i class="fas fa-lock"></i></a>
            <a href="contact.html" class="hidden md:inline-block px-8 py-3 bg-amber-600 text-white text-xs font-bold uppercase tracking-widest hover:bg-amber-500 transition rounded-sm shadow-[0_0_15px_rgba(217,119,6,0.3)]">Get Quote</a>
        </div>
    </div>
</nav>
"""

# FOOTER
footer_html = f"""
<footer class="bg-slate-950 text-slate-400 pt-32 pb-12 border-t border-slate-900 relative overflow-hidden">
    <div class="container mx-auto px-6 relative z-10">
        <div class="grid md:grid-cols-4 gap-16 mb-24">
            <div class="col-span-1 md:col-span-2">
                {logo_svg}
                <p class="mt-6 text-sm">Tristar Group Inc. is a global Tier-1 manufacturing partner.</p>
            </div>
            <div>
                <h4 class="text-white font-bold uppercase tracking-widest mb-8 text-xs">Quick Links</h4>
                <ul class="space-y-4 text-sm">
                    <li><a href="index.html" class="hover:text-amber-500 transition">Home</a></li>
                    <li><a href="divisions.html" class="hover:text-amber-500 transition">Manufacturing</a></li>
                    <li><a href="infrastructure.html" class="hover:text-amber-500 transition">Infrastructure</a></li>
                    <li><a href="contact.html" class="hover:text-amber-500 transition">Contact</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold uppercase tracking-widest mb-8 text-xs">Contact HQ</h4>
                <p class="mb-6 text-sm">854/6, Group Number 6,<br>Tagore Nagar, Vikhroli East,<br>Mumbai, Maharashtra 400083</p>
                <p class="text-slate-500 text-sm">sales@tristargroupinc.com</p>
            </div>
        </div>
        <div class="flex flex-col md:flex-row justify-between items-center pt-8 border-t border-slate-900 text-xs text-slate-600 font-mono">
            <p>&copy; 2025 Tristar Group Inc.</p>
            <div class="flex space-x-8 mt-4 md:mt-0">
                <a href="#" class="hover:text-white transition">PRIVACY</a>
                <a href="sitemap.xml" class="hover:text-white transition">SITEMAP</a>
            </div>
        </div>
    </div>
</footer>
"""

# ==========================================
# 2. HELPER FUNCTION (MOVED UP)
# ==========================================

def create_page(title, subtitle, bg_img, content):
    return f"""<!DOCTYPE html><html lang="en">{head_html}<body class="bg-slate-50 text-slate-800">{navbar}
    <header class="relative py-32 bg-slate-900 overflow-hidden">
        <div class="absolute inset-0 z-0"><img src="{bg_img}" class="w-full h-full object-cover opacity-20"></div>
        <div class="container mx-auto px-6 relative z-10 text-center" data-aos="fade-up">
            <h1 class="text-5xl md:text-7xl font-bold text-white mb-4 brand-font">{title}</h1>
            <p class="text-xl text-amber-500 font-light tracking-widest uppercase">{subtitle}</p>
        </div>
    </header>
    {content}
    {footer_html}{scripts_html}</body></html>"""

# ==========================================
# 3. PAGE CONTENT
# ==========================================

# --- INDEX PAGE ---
index_html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth bg-slate-950 text-white">
{head_html}
<body>
    {navbar}

    <header class="relative h-[110vh] min-h-[900px] flex items-center overflow-hidden">
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=2000&q=80" class="w-full h-full object-cover opacity-30 scale-110 animate-[pulse_15s_infinite]">
            <div class="absolute inset-0 bg-gradient-to-r from-slate-950 via-slate-950/80 to-transparent"></div>
            <div class="absolute bottom-0 w-full h-64 bg-gradient-to-t from-slate-950 to-transparent"></div>
        </div>
        <div class="container mx-auto px-6 relative z-10 mt-20">
            <div class="max-w-5xl">
                <div data-aos="fade-down" class="inline-flex items-center gap-3 border border-amber-500/30 bg-amber-500/5 backdrop-blur-md rounded-full px-6 py-2 mb-8">
                    <span class="relative flex h-2 w-2"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-amber-500"></span></span>
                    <span class="text-amber-500 text-xs font-bold uppercase tracking-[0.25em]">Tristar Group Inc.</span>
                </div>
                <h1 data-aos="fade-up" data-aos-delay="200" class="text-7xl md:text-9xl font-extrabold leading-[0.9] mb-8 tracking-tight">SCALING <br> <span class="text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-500">PERFECTION.</span></h1>
                <p data-aos="fade-up" data-aos-delay="400" class="text-lg text-slate-400 max-w-xl leading-relaxed border-l-2 border-amber-600 pl-6">We transform complex engineering challenges into mass-produced reality. The silent force behind the world's most trusted brands.</p>
                <div data-aos="fade-up" data-aos-delay="600" class="flex flex-col gap-4 w-full md:w-auto mt-12">
                    <a href="divisions.html" class="px-10 py-5 bg-amber-600 text-white font-bold uppercase tracking-widest text-sm hover:bg-amber-500 transition text-center">Explore Divisions</a>
                </div>
            </div>
        </div>
    </header>

    <div class="bg-amber-600 overflow-hidden py-3 relative z-20">
        <div class="flex whitespace-nowrap animate-[marquee_20s_linear_infinite]">
            <span class="text-xs font-bold text-black uppercase tracking-[0.2em] mx-8">● ISO 9001:2015 Certified</span>
            <span class="text-xs font-bold text-black uppercase tracking-[0.2em] mx-8">● Exporting to 15 Countries</span>
            <span class="text-xs font-bold text-black uppercase tracking-[0.2em] mx-8">● Production Status: Online</span>
            <span class="text-xs font-bold text-black uppercase tracking-[0.2em] mx-8">● Mumbai HQ: Operational</span>
        </div>
    </div>

    <section class="py-28 bg-slate-950 border-b border-slate-900">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
                <div><h3 class="text-6xl font-bold text-white mb-2 brand-font"><span class="counter" data-target="30">0</span>+</h3><p class="text-xs font-bold text-amber-600 uppercase tracking-[0.2em]">Years Legacy</p></div>
                <div><h3 class="text-6xl font-bold text-white mb-2 brand-font"><span class="counter" data-target="50">0</span>M</h3><p class="text-xs font-bold text-amber-600 uppercase tracking-[0.2em]">Parts Annually</p></div>
                <div><h3 class="text-6xl font-bold text-white mb-2 brand-font"><span class="counter" data-target="45">0</span>K</h3><p class="text-xs font-bold text-amber-600 uppercase tracking-[0.2em]">Sq. Ft. Area</p></div>
                <div><h3 class="text-6xl font-bold text-white mb-2 brand-font"><span class="counter" data-target="850">0</span>T</h3><p class="text-xs font-bold text-amber-600 uppercase tracking-[0.2em]">Max Tonnage</p></div>
            </div>
        </div>
    </section>

    <section class="py-32 bg-slate-900">
        <div class="container mx-auto px-6">
            <div class="flex flex-col lg:flex-row gap-20 items-center">
                <div class="lg:w-1/2" data-aos="fade-right">
                    <span class="text-amber-500 font-bold tracking-widest uppercase text-xs mb-6 block">Strategic Partner</span>
                    <h2 class="text-4xl md:text-6xl font-bold text-white mb-8 leading-tight brand-font">From Component Supplier to <span class="text-slate-600">Systems Integrator.</span></h2>
                    <p class="text-slate-400 text-lg leading-relaxed mb-8 font-light">Established in 1995, Tristar Group has evolved from a boutique moulding unit into a vertically integrated manufacturing conglomerate.</p>
                    <a href="about.html" class="inline-block border-b border-amber-600 pb-2 text-white hover:text-amber-500 transition uppercase text-xs font-bold tracking-widest">Read Our History</a>
                </div>
                <div class="lg:w-1/2 relative" data-aos="fade-left">
                    <img src="https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?auto=format&fit=crop&w=1000&q=80" class="rounded-lg shadow-2xl grayscale hover:grayscale-0 transition duration-700">
                </div>
            </div>
        </div>
    </section>

    <section class="py-32 bg-slate-950">
        <div class="container mx-auto px-6">
            <div class="flex justify-between items-end mb-20">
                <div><h2 class="text-4xl md:text-5xl font-bold text-white mb-2 brand-font">Integrated Ecosystem</h2><p class="text-slate-500">Three specialized divisions. One standard of quality.</p></div>
                <a href="divisions.html" class="hidden md:block text-amber-500 text-xs font-bold uppercase tracking-widest hover:text-white transition">View All Specs -></a>
            </div>
            <div class="grid lg:grid-cols-3 gap-8">
                <div class="group relative h-[600px] bg-slate-900 border border-slate-800 rounded-xl overflow-hidden" data-aos="fade-up">
                    <img src="https://plus.unsplash.com/premium_photo-1661963212517-830bbb7d76fc?auto=format&fit=crop&w=800&q=80" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-40 transition duration-700">
                    <div class="absolute bottom-0 left-0 p-10 w-full"><i class="fas fa-cube text-4xl text-amber-500 mb-6"></i><h3 class="text-3xl font-bold text-white mb-4 brand-font">Polymers</h3><p class="text-slate-400 text-sm mb-8 opacity-0 translate-y-4 group-hover:opacity-100 group-hover:translate-y-0 transition">High-precision injection moulding (50T-850T).</p><span class="text-white text-xs font-bold uppercase border-b border-amber-500 pb-1">Explore</span></div>
                </div>
                <div class="group relative h-[600px] bg-slate-900 border border-slate-800 rounded-xl overflow-hidden" data-aos="fade-up" data-aos-delay="200">
                    <img src="https://images.unsplash.com/photo-1598553696590-379e403d1685?auto=format&fit=crop&w=800&q=80" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-40 transition duration-700">
                    <div class="absolute bottom-0 left-0 p-10 w-full"><i class="fas fa-microchip text-4xl text-blue-500 mb-6"></i><h3 class="text-3xl font-bold text-white mb-4 brand-font">Electronics</h3><p class="text-slate-400 text-sm mb-8 opacity-0 translate-y-4 group-hover:opacity-100 group-hover:translate-y-0 transition">ESD-protected EMS facility. High-speed SMT.</p><span class="text-white text-xs font-bold uppercase border-b border-blue-500 pb-1">Explore</span></div>
                </div>
                <div class="group relative h-[600px] bg-slate-900 border border-slate-800 rounded-xl overflow-hidden" data-aos="fade-up" data-aos-delay="400">
                    <img src="https://images.unsplash.com/photo-1531297461136-82lw8.jpg" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-40 transition duration-700">
                    <div class="absolute bottom-0 left-0 p-10 w-full"><i class="fas fa-layer-group text-4xl text-slate-400 mb-6"></i><h3 class="text-3xl font-bold text-white mb-4 brand-font">Metal Fab</h3><p class="text-slate-400 text-sm mb-8 opacity-0 translate-y-4 group-hover:opacity-100 group-hover:translate-y-0 transition">Heavy stamping and deep drawing.</p><span class="text-white text-xs font-bold uppercase border-b border-slate-400 pb-1">Explore</span></div>
                </div>
            </div>
        </div>
    </section>

    {footer_html}
    {scripts_html}
</body>
</html>
"""

# --- CONTACT PAGE ---
contact_html = f"""<!DOCTYPE html><html lang="en">{head_html}<body class="bg-slate-50 text-slate-800">{navbar}
<header class="relative py-32 bg-slate-900 overflow-hidden">
    <div class="container mx-auto px-6 relative z-10 text-center" data-aos="fade-up">
        <h1 class="text-5xl md:text-7xl font-bold text-white mb-4 brand-font">Contact Us</h1>
        <p class="text-xl text-amber-500 font-light tracking-widest uppercase">Start the conversation</p>
    </div>
</header>
<section class="py-24 container mx-auto px-6 grid md:grid-cols-2 gap-16">
    <div class="bg-white p-10 shadow-lg border"><h3 class="text-2xl font-bold mb-6">Quote Request</h3>
        <form class="space-y-4"><input class="w-full p-4 border rounded" placeholder="Name"><input class="w-full p-4 border rounded" placeholder="Email"><textarea class="w-full p-4 border rounded" rows="4" placeholder="Details"></textarea><button class="w-full bg-slate-900 text-white font-bold py-4 rounded hover:bg-amber-600 transition">Send</button></form>
    </div>
    <div>
        <h3 class="text-3xl font-bold mb-8">Headquarters</h3>
        <p class="mb-4 text-lg"><strong>Address:</strong><br>854/6, Group Number 6, Tagore Nagar,<br>Vikhroli East, Mumbai, Maharashtra 400083</p>
        <p class="text-lg"><strong>Email:</strong> sales@tristargroupinc.com</p>
    </div>
</section>
{footer_html}{scripts_html}</body></html>"""

# --- LOGIN PAGE (Secure, Fails) ---
login_html = f"""<!DOCTYPE html><html lang="en">{head_html}
<style>.shake {{ animation: shake 0.5s; }} @keyframes shake {{ 0%, 100% {{ transform: translateX(0); }} 25%, 75% {{ transform: translateX(-10px); }} 50% {{ transform: translateX(10px); }} }}</style>
<body class="bg-slate-950 flex items-center justify-center min-h-screen relative overflow-hidden">
    <div class="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')]"></div>
    <div class="relative z-10 w-full max-w-md glass-card rounded-xl border border-slate-800 shadow-2xl p-10">
        <div class="text-center mb-10">{logo_svg_dark.replace('fill="#0f172a"', 'fill="#ffffff"')} <p class="text-slate-500 text-xs uppercase tracking-[0.3em] mt-4 font-bold">Secure Access</p></div>
        <div id="errorMsg" class="hidden bg-red-900/30 border border-red-800 text-red-400 p-4 mb-6 text-sm rounded"><p class="font-bold">Access Denied</p><p>Invalid Credentials.</p></div>
        <form id="loginForm" class="space-y-6">
            <input type="text" class="w-full bg-slate-900/50 border border-slate-700 text-white p-3 rounded" placeholder="ID">
            <input type="password" id="pass" class="w-full bg-slate-900/50 border border-slate-700 text-white p-3 rounded" placeholder="Password">
            <button type="submit" id="submitBtn" class="w-full bg-amber-600 text-white font-bold py-4 rounded hover:bg-amber-500 transition">LOGIN</button>
        </form>
        <div class="mt-8 text-center"><a href="index.html" class="text-slate-600 text-xs hover:text-white transition">Back to Site</a></div>
    </div>
    <script>document.getElementById('loginForm').addEventListener('submit',function(e){{e.preventDefault();const btn=document.getElementById('submitBtn');const card=document.querySelector('.glass-card');const orig=btn.innerHTML;btn.innerHTML='Verifying...';btn.classList.add('opacity-75');setTimeout(()=>{{btn.innerHTML=orig;btn.classList.remove('opacity-75');document.getElementById('errorMsg').classList.remove('hidden');card.classList.add('shake');}},1500);}});</script>
</body></html>"""

# --- ROBOTS & SITEMAP ---
robots_txt = "User-agent: *\nAllow: /\nSitemap: https://www.tristargroupinc.com/sitemap.xml"
sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://www.tristargroupinc.com/index.html</loc></url></urlset>"""

# --- PAGE DICTIONARY ---
pages = {
    'index.html': index_html,
    'contact.html': contact_html,
    'login.html': login_html,
    'robots.txt': robots_txt,
    'sitemap.xml': sitemap_xml,
    'about.html': create_page("About Us", "History & Leadership", "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=2000&q=80", "<div class='py-20 text-center container mx-auto'><h2>30 Years of Excellence</h2></div>"),
    'divisions.html': create_page("Divisions", "Our Expertise", "https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&w=2000&q=80", "<div class='py-20 text-center container mx-auto'><h2>Engineering, Electronics, Metal</h2></div>"),
    'infrastructure.html': create_page("Infrastructure", "Our Facilities", "https://images.unsplash.com/photo-1565514020176-db7923709b17?auto=format&fit=crop&w=2000&q=80", "<div class='py-20 text-center container mx-auto'><h2>Mumbai & Vasai Units</h2></div>"),
    'sustainability.html': create_page("Sustainability", "Green Future", "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=2000&q=80", "<div class='py-20 text-center container mx-auto'><h2>Net Zero by 2040</h2></div>"),
    'news.html': create_page("Newsroom", "Latest Updates", "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=2000&q=80", "<div class='py-20 text-center container mx-auto'><h2>Press Releases</h2></div>"),
    'careers.html': create_page("Careers", "Join Us", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=2000&q=80", "<div class='py-20 text-center container mx-auto'><h2>Open Positions</h2></div>"),
    'portal.html': "<html><body>Access Denied</body></html>"
}

# ==========================================
# 4. BUILD EXECUTION
# ==========================================

def build():
    print("🌟 Building Final Tristar Website...")
    for filename, content in pages.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            print(f"  -> Generated: {filename}")
    print("\n✅ Build Complete! Open 'index.html'.")

if __name__ == "__main__":
    build()