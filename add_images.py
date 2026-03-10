import codecs, re

path = r"c:/Users/cob/Desktop/취업자료26/지원서/HD중공업 지원서/HD중공업 포트폴리오.html"

with codecs.open(path, 'r', 'utf-8') as f:
    html = f.read()

# --- Beauty R사 Block: Replace single image div with two-image grid ---
beauty_old = re.compile(
    r'(<!-- Segment 1: Beauty R사 -->.*?<div class="cyber-card flex flex-col md:flex-row.*?overflow-hidden">)\s*'
    r'(<div\s+class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-r border-\[#233554\] bg-\[#111\] relative group cursor-pointer overflow-hidden">.*?</div>)',
    re.DOTALL
)

beauty_new_panel = '''                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-r border-[#233554] bg-[#111] flex flex-col">
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden border-b border-[#233554]">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 모바일 화면 1" />
                        </div>
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 상세 결과 2" />
                        </div>
                    </div>'''

# Find the beauty section single img div specifically
beauty_single_re = re.compile(
    r'(\s*<div\s*\n\s*class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-r border-\[#233554\] bg-\[#111\] relative group cursor-pointer overflow-hidden">.*?</div>)',
    re.DOTALL
)

# Do a targeted search-replace for the Beauty block using line numbers approach
lines = html.split('\n')

def replace_block(lines, old_lines, new_block):
    """Find old_lines as consecutive matching lines and replace with new_block lines."""
    n = len(old_lines)
    for i in range(len(lines) - n + 1):
        if all(lines[i+j].rstrip() == old_lines[j].rstrip() for j in range(n)):
            return lines[:i] + new_block.split('\n') + lines[i+n:]
    return None

# Build replacement HTML for Beauty R sa
beauty_old_block = """                    <div
                        class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-r border-[#233554] bg-[#111] relative group cursor-pointer overflow-hidden">
                        <div
                            class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                            <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여
                                확대</span>
                        </div>
                        <img src="./assets/img_crm_beauty_r.jpg.png"
                            class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                            alt="Beauty R사 CRM 모바일 화면" />
                    </div>""".rstrip()

beauty_new_block = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-r border-[#233554] bg-[#111] flex flex-col">
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden border-b border-[#233554]">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 모바일 화면 1" />
                        </div>
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

fashion_old_block = """                    <div
                        class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-l border-[#233554] bg-[#111] relative group cursor-pointer overflow-hidden">
                        <div
                            class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                            <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여
                                확대</span>
                        </div>
                        <img src="./assets/img_crm_fashion_l.jpg.png"
                            class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                            alt="Fashion L사 CRM 모바일 화면" />
                    </div>""".rstrip()

fashion_new_block = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-l border-[#233554] bg-[#111] flex flex-col">
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden border-b border-[#233554]">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 모바일 화면 1" />
                        </div>
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

# We use simple string replacement with \r\n since the file likely has Windows line endings
html = html.replace(beauty_old_block.replace('\n','\r\n'), beauty_new_block.replace('\n','\r\n'))
html = html.replace(fashion_old_block.replace('\n','\r\n'), fashion_new_block.replace('\n','\r\n'))

# verify replacements landed
if 'img_crm_beauty_r2.jpg' not in html:
    print("[ERROR] Beauty R2 image not inserted!")
    exit(1)
if 'img_crm_fashion_l2.jpg' not in html:
    print("[ERROR] Fashion L2 image not inserted!")
    exit(1)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(html)

print("[OK] Both image sections updated with two-image grids.")
