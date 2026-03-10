import re
import codecs

path = r"c:/Users/cob/Desktop/취업자료26/지원서/HD중공업 지원서/HD중공업 포트폴리오.html"

with codecs.open(path, 'r', 'utf-8') as f:
    html = f.read()

# Locate the process grid block
pattern = re.compile(r'(<h4[^>]*>[\s\n]*기술 설계 및 데이터 수집 ➔ AI 분석 ➔ 미디어 렌더링 ➔ 배포 단계[\s\n]*</h4>\s*<div class="grid grid-cols-2 md:grid-cols-4 gap-2 h-24">)(.*?)(</div>\s*</div>\s*<!-- Phase 2: Results -->|</div>\s*</div>\s*<div class="mb-6">)', re.DOTALL)

match = pattern.search(html)
if match:
    prefix = match.group(1)
    grid_content = match.group(2)
    suffix = match.group(3)

    # We want pickpilot 1, 2, 3, 4 from left to right.
    # We will build 4 items based on the ones existing.
    # pickpilot 1 and 2 should have bg-[#0A192F] and object-cover (they are result screenshots)
    # pickpilot 3 and 4 should have bg-[#111] and object-contain (they are node diagrams)
    
    # Wait, the user wants:
    # 1. pickpilot1.png (Result 2 - deployment)
    # 2. pickpilot2.png (Result 1 - media rendering)
    # 3. pickpilot3.png (Process 1 - data collection)
    # 4. pickpilot4.png (Process 2 - ai analysis)
    # This means process diagrams will literally go to the RIGHT, and results go to the LEFT.
    # I should just copy exactly the div blocks from the source, and put them in 1,2,3,4 order.
    
    parts = re.split(r'(<div\s*class="h-full border)', grid_content)
    
    # Extract the 4 divs
    divs = []
    current_div = ""
    for p in parts:
        if p.startswith('<div'):
            if current_div:
                divs.append(current_div)
            current_div = p
        else:
            current_div += p
    if current_div:
        divs.append(current_div)
        
    div_1 = next(d for d in divs if 'pickpilot1.png' in d)
    div_2 = next(d for d in divs if 'pickpilot2.png' in d)
    div_3 = next(d for d in divs if 'pickpilot3.png' in d)
    div_4 = next(d for d in divs if 'pickpilot4.png' in d)
    
    new_grid_content = div_1 + div_2 + div_3 + div_4
    
    html = html[:match.start(2)] + new_grid_content + html[match.end(2):]

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(html)
