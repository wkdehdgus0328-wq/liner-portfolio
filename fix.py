import re
import codecs

path = r"c:/Users/cob/Desktop/취업자료26/지원서/테슬라 지원서/테슬라 포트폴리오.html"
out_path = r"c:/Users/cob/Desktop/취업자료26/지원서/HD중공업 지원서/HD중공업 포트폴리오.html"

with codecs.open(path, 'r', 'utf-8') as f:
    html = f.read()

# CSS adjustments
html = html.replace('.text-tesla-red', '.text-hd-green')
html = html.replace('.bg-tesla-red', '.bg-hd-green')
html = html.replace('.border-tesla-red', '.border-hd-green')
html = html.replace('#e82127', '#00C868')
html = html.replace('#000000', '#0A192F')
html = html.replace('#0a0a0a', '#112240')
html = html.replace('#1f2937', '#233554')
html = html.replace('rgba(232, 33, 39,', 'rgba(0, 200, 104,')
html = html.replace('text-tesla-red', 'text-hd-green')
html = html.replace('bg-tesla-red', 'bg-hd-green')
html = html.replace('border-tesla-red', 'border-hd-green')
html = html.replace('bg-red-600', 'bg-[#00C868]')
html = html.replace('bg-red-950', 'bg-emerald-950')
html = html.replace('border-red-900', 'border-emerald-900')
html = html.replace('bg-black', 'bg-[#0A192F]')
html = html.replace('bg-[#050505]', 'bg-[#112240]')
html = html.replace('from-red-950/20', 'from-teal-900/20')
html = html.replace('from-gray-800', 'from-[#112240]')
html = html.replace('via-black', 'via-[#0A192F]')
html = html.replace('to-black', 'to-[#0A192F]')

# Titles
def flex_replace(src, dest):
    global html
    pattern = re.escape(src).replace(r'\ ', r'\s+').replace(r'\n', r'\s+')
    html = re.sub(pattern, dest, html)

flex_replace('장동현 | Sales Advisor Portfolio', '장동현 | HD현대중공업 상품기획(로봇/자동화 솔루션) 포트폴리오')
flex_replace('01. Identity', '01. Hardware CX')
flex_replace('02. Inbound CX', '02. B2B Solution')
flex_replace('03. Lead Qual.', '03. Automation System')
flex_replace('04. Sales Ops', '04. Experience')
flex_replace('Inside Sales Advisor Target', 'Robotics & Automation PM Target')

html = re.sub(r'데이터로 <span class="text-hd-green">타겟팅</span>하고,<br />\s*압도적인 현장 경험으로\s*<span class="inline-block"><span class="text-hd-green">클로징</span>합니다.</span>',
    '산업 현장에 대한 <span class="text-hd-green">깊은 이해</span>와,<br />\nAI 자동화 설계 역량으로\n<span class="inline-block">미래 솔루션을 <span class="text-hd-green">기획합니다.</span></span>', html)

html = re.sub(r'세일즈 어드바이저의 본질은 고객과 소통하고 비전을 전달하는\s*것입니다.<br />\s*<strong class="text-gray-200">단순 반복 업무는 AI로 100% 무인화하고, 저는 오직 \'고객\'과\s*\'세일즈\'에만 집중합니다.</strong>',
    '로봇과 자동화 솔루션의 끝단에는 결국 <strong class="text-gray-200">\'현장의 작업자(End-user)\'</strong>가 있습니다.<br />\n<strong class="text-gray-200">하드웨어 현장 VOC 분석부터 B2B 소프트웨어 솔루션 기획, AI 파이프라인 구축까지 아우르는 실무형 기획자입니다.</strong>', html)

html = html.replace('01. FRONT-LINE CX', '01. HARDWARE CX')
html = html.replace('02. LEAD QUALIFICATION', '02. B2B SOLUTION')
html = html.replace('03. HARDCORE EFFICIENCY', '03. AUTOMATION SYSTEM')

html = html.replace('01. The Frontline</span>', '01. Hardware CX</span>')
html = html.replace('현장에서 체득한 인바운드 커뮤니케이션', '산업용 하드웨어 현장 이해 및 VOC 관리')
html = re.sub(r"테슬라 고객과의 첫 접점은 화면 너머의 '사람'입니다.\s*스탠리블랙앤데커에서\s*<strong class=\"text-white font-inter\">4,200명</strong>의 고객을 직접\s*응대하며, 고객을 교육하고 브랜드 비전을 영감으로\s*전환하는 최전선 세일즈 역량을 증명했습니다.",
    "다양한 산업 현장 작업자들이 겪는 하드웨어 툴의 파편화된 페인포인트를 파악하기 위해, 240여 종의 전동공구 포트폴리오를 기반으로 누적 <strong class=\"text-white font-inter\">4,200명 이상</strong>의 엔드유저 VOC를 수집하고 최적의 장비를 큐레이션한 하드웨어 현장 역량입니다.", html)

html = html.replace('"고객의 페인포인트를 기회로 바꾸다"', '"현장의 목소리(VOC)에서 솔루션을 찾다"')
html = re.sub(r'<strong class="text-gray-200 block mb-1">Respond to Inbound Leads</strong>인바운드 채널로 유입되는 방대한\s*고객의 질문과 불만을 신속하고\s*전문적으로 응대하여 브랜드 신뢰도 구축.',
    '<strong class="text-gray-200 block mb-1">하드웨어 툴 환경 분석</strong>240여 종의 툴 라인업을 기반으로 현장 작업자의 니즈와 불만을 수집 및 분석하여 최적의 장비 매칭.', html)
html = re.sub(r'<strong class="text-gray-200 block mb-1">Build Connections & Consult</strong>고객의 니즈를 정확히\s*진단\(Qualify\)하고, 단순 안내를 넘어 제품의\s*가치와 활용법을 컨설팅하는 맞춤형 커뮤니케이션 리드.',
    '<strong class="text-gray-200 block mb-1">B2B 고객 교육 및 컨설팅</strong>제품 스펙을 넘어, 현장 라인업 최적화와 생산성 향상을 위한 맞춤형 하드웨어 사용 컨설팅 주도.', html)
html = re.sub(r'<strong class="text-gray-200 block mb-1">Commitment to Excellence</strong>수많은 응대 케이스 속에서도\s*품질과 디테일에 집착하여 최상의\s*고객 경험\(CX\) 방어 및 유지.',
    '<strong class="text-gray-200 block mb-1">VOC 기반 인사이트 발굴</strong>최전선에서 누적 4,200건의 고객 피드백을 체계화하여 프로세스 개선 방향과 신규 솔루션 아이디어 도출.', html)

html = html.replace('02. Lead Qualification Engine</span>', '02. B2B Solution</span>')
html = html.replace('데이터 기반 리드(Lead) 타겟팅 전략', 'B2B 고객사 맞춤형 솔루션 기획 및 라이프사이클 관리')
html = re.sub(r'CRM 시스템에 쌓인 고객 정보는 단순한 명부가 아닙니다.\s*스냅컴퍼니에서 40여 개 브랜드의 데이터를 분석하여\s*<strong class="text-white">누가 진짜 구매할 잠재 고객인지 필터링하고, 맞춤형 소구점으로 클로징을 유도한</strong>\s*세일즈 타겟팅 역량입니다.',
    '단순한 소비재 마케팅을 넘어, 40여 개 B2B 고객사(브랜드사)의 비즈니스 데이터를 진단하고 <strong class="text-white">제품 라이프사이클(Lifecycle) 연장을 위한 CRM 소프트웨어 솔루션을 기획/제안한</strong> 솔루션 기획 역량입니다.', html)
html = html.replace('ROAS 985% 증진', 'B2B 고객사 성과 증명')
html = html.replace('매출액 300% 증가', 'B2B 고객사 성과 증명')
html = html.replace('미구매율 12.5%p 개선', 'B2B 고객사 성과 증명')
html = html.replace('행동 기반 A/B 테스트 최적화', '데이터 기반 고객 세그먼트 솔루션 제안')
html = html.replace('채널 최적화 및 리마인드 퍼널 구축', '발송 채널 최적화 및 리마인드 솔루션 구축')
html = html.replace('온사이트 퍼널 병목 해결', '온사이트 퍼널 병목 분석 및 추천 솔루션 기획')

html = re.sub(r'<strong class="text-hd-green font-inter tracking-wider block mb-1">PROBLEM</strong>\s*유입 고객 대비 첫 구매 이후의 중장기 리텐션이 현저히 저하되는\s*현상 발생.',
    '<strong class="text-hd-green font-inter tracking-wider block mb-1">PROBLEM</strong> 제품 도입 이후 고객 라이프사이클 단축 및 중장기 리텐션이 현저히 저하되는 퍼널 병목 발생.', html)
html = re.sub(r'<strong class="text-white block mb-1 font-inter tracking-wider">ACTION</strong>\s*전체 고객을 3개 세그먼트\(진성/관심/장바구니 이탈\)로 정밀 분류.\s*타겟의 심리에 맞춰 소구점\(할인율 강조 vs 희소성 강조\)을 다르게\s*적용한 CRM 캠페인 기획 및 발송.',
    '<strong class="text-white block mb-1 font-inter tracking-wider">ACTION</strong> B2B 고객사의 데이터를 진단하여, 엔드유저를 3개 세그먼트(진성/관심/이탈)로 정밀 분류하고 타겟 심리에 맞춘 CRM 솔루션 기획 및 스나이핑 제안.', html)
html = re.sub(r'<strong class="text-gray-200 block mb-1 font-inter tracking-wider">IMPACT</strong>\s*전체 광고 성과 747% →\s*<strong class="text-white">985% 상승</strong>, 캠페인\s*클릭률\(CTR\) 약 <strong class="text-white">400% 상승</strong>,\s*재구매 고객 <strong class="text-white">5%p 증가</strong>.',
    '<strong class="text-gray-200 block mb-1 font-inter tracking-wider">IMPACT</strong> B2B 고객사 지표 개선 (광고 성과 <strong class="text-white">985% 상승</strong>, 솔루션 클릭률 약 <strong class="text-white">400% 상승</strong>).', html)

html = re.sub(r'<strong class="text-hd-green font-inter tracking-wider block mb-1">PROBLEM</strong>\s*첫 구매 이후 재구매 전환이 저조하며, 기존 발송 채널\(친구톡\)의\s*도달률 한계 확인.',
    '<strong class="text-hd-green font-inter tracking-wider block mb-1">PROBLEM</strong> 기존 채널의 메시지 도달률 한계 및 이탈에 따른 제품 구매 주기 단축 현상 확인.', html)
html = re.sub(r'<strong class="text-white block mb-1 font-inter tracking-wider">ACTION</strong>\s*발송 채널을 \'알림톡\'으로 전환하여 도달률 개선. 장기 이탈\s*고객과 최근 이탈 고객 그룹을 나누어 마인드맵 타겟 조건에 따른\s*맞춤형 메시지 소구점 제안.',
    '<strong class="text-white block mb-1 font-inter tracking-wider">ACTION</strong> 알림톡 등으로 채널을 최적화하고 이탈 주기 및 마인드맵 타겟 조건에 따른 맞춤형 메시지 소구점을 자동 제안하는 솔루션(리마인드 룻) 기획.', html)
html = re.sub(r'<strong class="text-gray-200 block mb-1 font-inter tracking-wider">IMPACT</strong>\s*전 분기 대비 전체 CRM 광고 성과\s*<strong class="text-white">300% 증가</strong>, 재구매 고객 약\s*<strong class="text-white">8% 증가</strong> 달성.',
    '<strong class="text-gray-200 block mb-1 font-inter tracking-wider">IMPACT</strong> 솔루션 도입 후 전체 프로모션 성과 <strong class="text-white">300% 증가</strong> 및 비즈니스 라이프사이클 연장.', html)

html = re.sub(r'<strong class="text-hd-green font-inter tracking-wider block mb-1">PROBLEM</strong>\s*신규 유입 고객 중 약 60% 이상이 구매 없이 이탈하는 치명적 퍼널\s*병목 발견.',
    '<strong class="text-hd-green font-inter tracking-wider block mb-1">PROBLEM</strong> 신규 유입 대비 구매 전환율이 저하되어 이탈하는 치명적 퍼널 병목 발견.', html)
html = re.sub(r'<strong class="text-white block mb-1 font-inter tracking-wider">ACTION</strong>\s*주문, 상품, 장바구니 등 핵심 이탈 구간을 식별하고, 해당 섹션에\s*타겟팅된 온사이트 팝업 및 알고리즘 기반 상품 추천 로직 설계.',
    '<strong class="text-white block mb-1 font-inter tracking-wider">ACTION</strong> 핵심 이탈 구간을 데이터로 식별하고, 해당 섹션에 타겟팅된 동적 팝업 및 알고리즘 기반 상품 추천 로직 탑재 솔루션 제안.', html)
html = re.sub(r'<strong class="text-gray-200 block mb-1 font-inter tracking-wider">IMPACT</strong>\s*하반기 ROAS 300% →\s*<strong class="text-white">500% 상승</strong>, 신규 고객 전체\s*미구매율 60% →\s*<strong class="text-white">47.5%로 대폭 감소</strong>\(클로징\s*성공\).',
    '<strong class="text-gray-200 block mb-1 font-inter tracking-wider">IMPACT</strong> 신규 고객 미구매 이탈율 <strong class="text-white">47.5%로 대폭 감소</strong> 및 솔루션 기반 ROAS 500% 개선 달성.', html)

html = html.replace('03. Hardcore Efficiency & Start-up DNA</span>', '03. Automation System</span>')
html = html.replace("세일즈 극대화를 위한 '초효율화' 무인 시스템", '시장 조사 및 VOC 수집 자동화 시스템 구축')
html = re.sub(r'세일즈 어드바이저는 고객과 대화하는 데 100%의 시간을 써야 합니다.\s*이를 위해 단순 반복되는 리드 소싱이나 이메일 응대\(VOC\)를\s*<strong class="text-white font-inter">n8n</strong>과\s*<strong class="text-white font-inter">AI Agent</strong>로 완전히\s*자동화시켰습니다. 문제를 기술로 돌파하는\s*<strong>Start-up Mode</strong> 역량입니다.',
    '로봇/자동화 솔루션 기획자는 데이터를 빠르고 정확하게 분석하는 능력이 필수적입니다. 데이터 소싱부터 VOC 분류까지 <strong class="text-white font-inter">n8n</strong>과 <strong class="text-white font-inter">AI Agent</strong>를 결합해 <strong class="text-white font-inter">데이터 파이프라인을 구축하고 업무 리드타임을 혁신적으로 단축한</strong> 시스템 설계 역량입니다.', html)
html = html.replace('무인 수익화 파이프라인', '시장 분석 파이프라인 구축')

html = re.sub(r'<p><strong class="text-hd-green font-inter tracking-wider">PROBLEM:</strong> 수동으로 리뷰 데이터를 소싱하고\s*콘텐츠를 업로드하는 과정의 심각한 리드타임\(비효율\) 발생. AI Agent와 n8n을 활용한 자율화 시스템 도입 필요.</p>\s*<p class="pt-1 border-t border-[#233554]"><strong\s*class="text-white font-inter tracking-wider">PURPOSE:</strong> 글로벌\(영미권\) 이커머스 시장을 타겟으로,\s*아마존 리뷰 데이터를 분석해 다매체 콘텐츠\(YouTube Shorts, Medium\)를 자율 생성 및 배포하는 무인 수익화 파이프라인 구축.</p>',
    '<p><strong class="text-hd-green font-inter tracking-wider">PROBLEM:</strong> 수동으로 제품 리뷰 및 VOC 데이터를 소싱하고 트렌드를 분석하는 과정의 심각한 리드타임 발생.</p>\n<p class="pt-1 border-t border-[#233554]"><strong class="text-white font-inter tracking-wider">PURPOSE:</strong> 상품 기획 및 라인업 로드맵 수립에 필요한 글로벌 시장의 방대한 데이터(리뷰/VOC)를 AI와 n8n으로 자동 수집하고 분석하는 파이프라인 구축.</p>\n<p class="pt-1 border-t border-[#233554]"><strong class="text-white font-inter tracking-wider">IMPACT:</strong> 시장 조사 및 데이터 가공 리드타임 <strong class="text-white">99% 단축</strong>. 주 40시간의 단순 반복 업무를 10분 내로 삭감 완료.</p>', html)

html = re.sub(r'<ul class="space-y-3 text-sm text-gray-400 mt-auto pt-4 border-t border-gray-800">\s*<li>\s*<strong class="text-gray-200 block mb-1">Process \(과정\):</strong>\s*데이터 소싱부터 렌더링, 통합 쇼룸 배포 전 과정을 n8n 기반 100%\s*무인화 설계. 대규모 429 Error는 순차 제어로 돌파.\s*</li>\s*<li>\s*<strong class="text-gray-200 block mb-1">Impact \(결과\):</strong>\s*수동 세일즈 및 콘텐츠 퍼블리싱 업무 99% 삭감 완료. 단점을 분석해\s*신뢰를 구축하는 The 3-Star Truth 전략 달성.\s*</li>\s*</ul>', '', html)

html = re.sub(r'<div>\s*<strong class="text-white block mb-1">LLM 기반 인텐트\(Intent\) 분석</strong>\s*엑셀로 쏟아지는 방대한 고객 문의\(VOC\) 데이터를 AI 에이전트\(GPT-4o\)가 자동 분석합니다. 시스템 내부에 \'CS 전문 최고 행정관\' 페르소나를 부여하고,\s*고객의 <strong>감정 상태\(긍정/부정\) 및 민원 긴급도\(A~C 등급\)</strong>를 판단하도록 프롬프트를 정교하게 설계하여 인텐트\(Intent\)를 정확히\s*분류합니다.\s*</div>\s*<div>\s*<strong class="text-white block mb-1">동적 라우팅 및 퍼스널 응답</strong>\s*분류된 카테고리에 따라 담당 부서로 자동 배정하고, 수신자 맞춤형\s*변수가 포함된 HTML 브랜드 이메일을 즉시 발송.\s*</div>\s*<div class="border-l-2 border-hd-green pl-3 pt-2">\s*<p class="text-gray-200 font-medium">\s*단순 메일 응대와 리드 배정에 낭비되던 시간을 소거하여,\s*<strong class="text-white">세일즈 어드바이저가 \'시승\(Test Drive\) 스케줄링\'과 \'고객\s*대면\'에만 전력을 다할 수 있는 백오피스 환경</strong>\s*구축 증명.\s*</p>\s*</div>',
    '<div>\n<strong class="text-white block mb-1">LLM 기반 인텐트(Intent) 정밀 분석</strong>\n대규모 고객 VOC 분류의 수작업 비효율을 해결하기 위해, 쏟아지는 방대한 고객 문의 데이터를 AI 에이전트가 자동 분석합니다. <strong>감정 상태(긍정/부정) 및 민원 긴급도(A~C 등급)</strong>를 파악하도록 프롬프트를 설계하여 인텐트를 철저히 분류했습니다.\n</div>\n<div>\n<strong class="text-white block mb-1">동적 라우팅 자동 분기</strong>\n분류된 카테고리에 따라 담당 부서로 자동 분기(Routing)하고, 수신자 맞춤형 변수가 포함된 HTML 이메일을 즉시 발송합니다.\n</div>\n<div class="border-l-2 border-hd-green pl-3 pt-2">\n<p class="text-gray-200 font-medium">\n수작업으로 지연되던 초기 대응 리드타임을 <strong class="text-white">90% 이상 단축</strong>하여 현장 운영의 효율성을 제고하고 실시간 고객 반응을 자산화했습니다.\n</p>\n</div>', html)


# We are going to replace pickpilot images in the Phase 1 section to match the logical order:
# 기술 설계 및 데이터 수집 -> AI 분석 -> 미디어 렌더링 -> 배포 단계
# The original images are pickpilot3, pickpilot4, pickpilot1, pickpilot2.
# We want to change the order to: pickpilot3, pickpilot4, pickpilot2, pickpilot1.
# Specifically, we want to swap pickpilot1 and pickpilot2 in this grid list.
# The easiest way:
# find the section `<div class="grid grid-cols-2 md:grid-cols-4 gap-2 h-24">...</div>` under `Phase 1: Process`
pattern_phase1 = re.compile(r'(<h4[^>]*>[\s\n]*기술 설계 및 데이터 수집 ➔ AI 분석 ➔ 미디어 렌더링 ➔ 배포 단계[\s\n]*</h4>\s*<div[^>]*>)(.*?)(</div>\s*</div>\s*<!-- Phase 2: Results -->)', re.DOTALL)
match = pattern_phase1.search(html)
if match:
    grid_content = match.group(2)
    # We replace "pickpilot1.png" -> "TEMP" -> "pickpilot2.png", etc
    grid_content = grid_content.replace('pickpilot1.png', 'pickpilot_TEMP.png')
    grid_content = grid_content.replace('pickpilot2.png', 'pickpilot1.png')
    grid_content = grid_content.replace('pickpilot_TEMP.png', 'pickpilot2.png')
    html = html[:match.start(2)] + grid_content + html[match.end(2):]

# Outro
html = html.replace('Driving the Future of Sales', '현장과 기술을 잇는 자동화 솔루션 기획자')
html = re.sub(r'글로벌 비즈니스 리터러시\(OPIc IH, ITT 비즈니스통번역\)와 기술적 문제\s*해결력을 바탕으로, 테슬라의 비전을 고객에게 가장 완벽하게\s*딜리버리\(Delivery\)하겠습니다.',
    '하드웨어 현장의 니즈를 분석하는 이해도와,<br/>소프트웨어·AI를 아우르는 문제 해결력을 바탕으로<br/>HD현대중공업의 자동화 로드맵을 함께 실현하겠습니다.', html)

html = html.replace('text-tesla-red hover:text-red-700', 'text-[#00C868] hover:text-[#00A858]')
html = html.replace('border-gray-800', 'border-[#233554]')

with codecs.open(out_path, 'w', 'utf-8') as f:
    f.write(html)
