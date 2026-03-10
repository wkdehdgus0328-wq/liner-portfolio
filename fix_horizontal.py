import codecs

files = [
    r"c:/Users/cob/Desktop/취업자료26/지원서/HD중공업 지원서/index.html",
    r"c:/Users/cob/Desktop/취업자료26/지원서/HD중공업 지원서/HD중공업 포트폴리오.html"
]

for path in files:
    with codecs.open(path, 'r', 'utf-8') as f:
        html = f.read()

    is_hd = "HD중공업" in path

    if is_hd:
        border_color = "#233554"
        hover_color = "bg-hd-green/10"
        span_bg = "bg-[#0A192F]/80"
    else:
        border_color = "gray-800"
        hover_color = "bg-[#2563EB]/10"
        span_bg = "bg-black/80"

    # ---- Beauty R사 ----
    # Replace the current two-image vertical stack with horizontal grid
    beauty_vertical_hd = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-r border-[#233554] bg-[#111] flex flex-col">
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

    beauty_vertical_cosmax = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-r border-gray-800 bg-[#111] flex flex-col">
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

    # Horizontal grid replacements
    beauty_horizontal_hd = """                    <div class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-r border-[#233554] bg-[#233554] grid grid-cols-2 gap-px">
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 모바일 화면 1" />
                        </div>
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

    beauty_horizontal_cosmax = """                    <div class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-r border-gray-800 bg-gray-800 grid grid-cols-2 gap-px">
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 모바일 화면 1" />
                        </div>
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_beauty_r2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Beauty R사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

    # ---- Fashion L사 ----
    fashion_vertical_hd = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-l border-[#233554] bg-[#111] flex flex-col">
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

    fashion_vertical_cosmax = """                    <div class="w-full md:w-1/2 border-b md:border-b-0 md:border-l border-gray-800 bg-[#111] flex flex-col">
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

    fashion_horizontal_hd = """                    <div class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-l border-[#233554] bg-[#233554] grid grid-cols-2 gap-px">
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 모바일 화면 1" />
                        </div>
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-hd-green/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-[#0A192F]/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

    fashion_horizontal_cosmax = """                    <div class="w-full md:w-1/2 h-80 md:h-auto border-b md:border-b-0 md:border-l border-gray-800 bg-gray-800 grid grid-cols-2 gap-px">
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l.jpg.png"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 모바일 화면 1" />
                        </div>
                        <div class="relative group cursor-pointer overflow-hidden bg-[#111] flex items-center justify-center">
                            <div class="absolute inset-0 bg-[#2563EB]/10 opacity-0 group-hover:opacity-100 transition duration-300 z-10 pointer-events-none flex items-center justify-center">
                                <span class="bg-black/80 px-2 py-1 text-[10px] md:text-xs font-bold text-white rounded tracking-wider">클릭하여 확대</span>
                            </div>
                            <img src="./assets/img_crm_fashion_l2.jpg"
                                class="w-full h-full object-contain cursor-pointer hover:scale-105 transition duration-300"
                                alt="Fashion L사 CRM 상세 결과 2" />
                        </div>
                    </div>"""

    if is_hd:
        html = html.replace(beauty_vertical_hd.replace('\n','\r\n'), beauty_horizontal_hd.replace('\n','\r\n'))
        html = html.replace(fashion_vertical_hd.replace('\n','\r\n'), fashion_horizontal_hd.replace('\n','\r\n'))
    else:
        html = html.replace(beauty_vertical_cosmax.replace('\n','\r\n'), beauty_horizontal_cosmax.replace('\n','\r\n'))
        html = html.replace(fashion_vertical_cosmax.replace('\n','\r\n'), fashion_horizontal_cosmax.replace('\n','\r\n'))

    if 'grid grid-cols-2 gap-px' not in html or 'img_crm_beauty_r2' not in html or 'img_crm_fashion_l2' not in html:
        print(f"[ERROR] Replacement failed for: {path}")
        exit(1)

    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(html)
    print(f"[OK] {path}")

print("[DONE] Both files updated to horizontal grid layout.")
