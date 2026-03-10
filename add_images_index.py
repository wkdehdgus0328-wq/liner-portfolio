import codecs

path = r"c:/Users/cob/Desktop/취업자료26/지원서/HD중공업 지원서/index.html"

with codecs.open(path, 'r', 'utf-8') as f:
    html = f.read()

# Beauty R사 - single image block to replace
beauty_old = """                    <div
                        class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-r border-gray-800 bg-[#111] relative group cursor-pointer overflow-hidden">
                        <div
                            class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                            <span class="bg-black/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여
                                확대</span>
                        </div>
                        <img src="./assets/img_crm_beauty_r.jpg.png"
                            class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                            alt="Beauty R사 CRM 모바일 화면" />
                    </div>"""

beauty_new = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-r border-gray-800 bg-[#111] flex flex-col">
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden border-b border-gray-800">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 모바일 화면 1" />
                        </div>
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

# Fashion L사 - single image block to replace
fashion_old = """                    <div
                        class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-l border-gray-800 bg-[#111] relative group cursor-pointer overflow-hidden">
                        <div
                            class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                            <span class="bg-black/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여
                                확대</span>
                        </div>
                        <img src="./assets/img_crm_fashion_l.jpg.png"
                            class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                            alt="Fashion L사 CRM 모바일 화면" />
                    </div>"""

fashion_new = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-l border-gray-800 bg-[#111] flex flex-col">
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden border-b border-gray-800">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 모바일 화면 1" />
                        </div>
                        <div class="flex-1 h-40 relative group cursor-pointer overflow-hidden">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-3 py-2 text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

# Apply Windows line endings
html = html.replace(
    beauty_old.replace('\n', '\r\n'),
    beauty_new.replace('\n', '\r\n')
)
html = html.replace(
    fashion_old.replace('\n', '\r\n'),
    fashion_new.replace('\n', '\r\n')
)

if 'img_crm_beauty_r2.jpg' not in html:
    print("[ERROR] Beauty R2 image NOT inserted in index.html")
    exit(1)
if 'img_crm_fashion_l2.jpg' not in html:
    print("[ERROR] Fashion L2 image NOT inserted in index.html")
    exit(1)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(html)

print("[OK] index.html updated: both beauty_r2 and fashion_l2 images added.")
