#!/usr/bin/env python3
"""Build the Grand K sub-pages (Hạng phòng · Tin tức · Liên hệ) for Option 01 / 04 / 05.

One content source, three skins. Run from the grandk-redesign folder:
    python3 tools/build_pages.py
Outputs: option-{1,4,5}-{rooms,news,contact}.html
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPTS = (1, 4, 5)
PAGES = {'rooms': 'Hạng phòng', 'news': 'Tin tức', 'contact': 'Liên hệ'}
NAMES = {1: 'Grand Classic', 4: 'Modern Grid', 5: 'Bento Studio'}

PHONE, PHONE_TEL, EMAIL = '+84 24 3205 2299', '+842432052299', 'info@grandkhanoi.com'
ADDRESS = 'Số 2 Phạm Văn Bạch, phường Cầu Giấy, Hà Nội'
MAPS_Q = 'Grand+K+Hotel+Suites+Hanoi,+2+Pham+Van+Bach,+Cau+Giay,+Ha+Noi'

# ------------------------------------------------------------------ content
ROOMS = [
    dict(id='deluxe', cat='room', kind='Phòng', name='Deluxe', size=30, bed='King / Twin', view='Thành phố', bedrooms='—', kitchen=False,
         img='room-deluxe.jpg', desc='Không gian ấm cúng, hiện đại với đầy đủ tiện nghi thiết yếu — lựa chọn gọn gàng cho chuyến công tác hay kỳ nghỉ ngắn ngày giữa lòng Cầu Giấy.'),
    dict(id='premium', cat='room', kind='Phòng', name='Premium', size=45, bed='King', view='Thành phố', bedrooms='—', kitchen=False,
         img='room-premium.jpg', desc='Rộng rãi hơn với khu vực tiếp khách riêng, ánh sáng tự nhiên tràn ngập và tầm nhìn thoáng đãng ra thành phố.'),
    dict(id='junior-suite', cat='suite', kind='Suite', name='Junior Suite', size=45, bed='Giường đôi', view='Thành phố', bedrooms='—', kitchen=False,
         img='room-junior.jpg', desc='Thiết kế dạng suite với không gian sinh hoạt liền mạch — phù hợp cho cặp đôi hoặc khách lưu trú dài ngày.'),
    dict(id='one-bedroom', cat='apt', kind='Căn hộ', name='One Bedroom Suite', size=70, bed='King', view='Thành phố', bedrooms='1', kitchen=True,
         img='room-1br.jpg', desc='Căn hộ một phòng ngủ với phòng khách và bếp riêng — cảm giác như ở nhà, ngay giữa trung tâm phía Tây Thủ đô.'),
    dict(id='two-bedroom-executive', cat='apt', kind='Căn hộ', name='Two Bedroom Executive Suite', size=95, bed='King + Twin', view='Thành phố', bedrooms='2', kitchen=True,
         img='room-2br-exec.jpg', desc='Hai phòng ngủ, phòng khách rộng và bếp đầy đủ — lựa chọn hoàn hảo cho gia đình hoặc nhóm công tác.'),
    dict(id='two-bedroom-panoramic', cat='apt', kind='Căn hộ', name='Two Bedroom Panoramic Suite', size=95, bed='King + Twin', view='Toàn cảnh', bedrooms='2', kitchen=True,
         img='room-2br-pano.jpg', desc='Căn hộ góc với tầm nhìn toàn cảnh phía Tây Hà Nội — đẹp nhất khi thành phố lên đèn.'),
]
ROOM_AMEN = ['Wifi tốc độ cao', 'Smart TV', 'Minibar', 'Két an toàn', 'Máy pha trà & cà phê', 'Đồ dùng phòng tắm cao cấp']
APT_AMEN = ['Bếp riêng', 'Phòng khách']

NEWS = [
    dict(cat='offer', label='Ưu đãi', date='12.11.2026', read='3 phút', img='skybar.jpg',
         title='Hoàng hôn trên tầng 45: mùa cocktail mới tại SKY 45',
         ex='Thực đơn cocktail lấy cảm hứng từ những gia vị Việt, phục vụ trên sân thượng tầng 45 mỗi chiều — kèm ưu đãi cho khách lưu trú.'),
    dict(cat='dining', label='Ẩm thực', date='08.11.2026', read='4 phút', img='dining.jpg',
         title='Buffet sáng ba miền — khởi đầu ngày mới tại Grand K',
         ex='Từ phở Hà Nội, bánh mì đến các món Âu: một vòng ẩm thực trước giờ làm việc.'),
    dict(cat='event', label='Sự kiện', date='02.11.2026', read='5 phút', img='meeting.jpg',
         title='Hội nghị trọn gói 2026 cho doanh nghiệp phía Tây Hà Nội',
         ex='175 m² không gian hội nghị, tea-break và lưu trú cho đoàn — gần Trung tâm Hội nghị Quốc gia.'),
    dict(cat='explore', label='Khám phá Hà Nội', date='28.10.2026', read='6 phút', img='loc-museum.jpg',
         title='5 điểm đến văn hoá trong bán kính 10 km từ Cầu Giấy',
         ex='Bảo tàng, di tích và những góc phố đáng ghé khi bạn có một buổi chiều rảnh.'),
    dict(cat='stay', label='Lưu trú', date='21.10.2026', read='4 phút', img='room-2br-exec.jpg',
         title='Vì sao căn hộ dịch vụ là lựa chọn cho kỳ công tác dài ngày',
         ex='Bếp riêng, phòng khách rộng và dịch vụ khách sạn — sự cân bằng giữa riêng tư và tiện nghi.'),
    dict(cat='offer', label='Ưu đãi', date='15.10.2026', read='3 phút', img='pool.jpg',
         title='Cuối tuần cho gia đình: hồ bơi nước nóng & khu vui chơi trẻ em',
         ex='Gói nghỉ dưỡng hai ngày một đêm với hồ bơi trong nhà và không gian vui chơi an toàn cho bé.'),
    dict(cat='explore', label='Khám phá Hà Nội', date='09.10.2026', read='4 phút', img='loc-mydinh.jpg',
         title='Mùa sự kiện tại Mỹ Đình: lưu trú thuận tiện cho người hâm mộ',
         ex='Chỉ vài phút tới Sân vận động Quốc gia — gợi ý lịch trình trước và sau mỗi trận đấu, đêm nhạc.'),
    dict(cat='dining', label='Ẩm thực', date='01.10.2026', read='3 phút', img='hotel-night.jpg',
         title='Bữa tối nhìn ra thành phố: gợi ý cho những dịp đặc biệt',
         ex='Kỷ niệm, sinh nhật hay một buổi hẹn — những bàn ăn đẹp nhất khi Cầu Giấy lên đèn.'),
    dict(cat='stay', label='Lưu trú', date='24.09.2026', read='3 phút', img='room-2br-pano.jpg',
         title='Panoramic Suite — căn hộ đẹp nhất khi thành phố lên đèn',
         ex='95 m², hai phòng ngủ và ô kính lớn nhìn toàn cảnh phía Tây Hà Nội.'),
    dict(cat='explore', label='Khám phá Hà Nội', date='18.09.2026', read='5 phút', img='loc-oldquarter.jpg',
         title='Từ Grand K đến Phố cổ: ba cách di chuyển nhanh nhất',
         ex='Khoảng 8 km tới Hồ Gươm — taxi, xe công nghệ hay dịch vụ đưa đón của khách sạn.'),
]
SLUGS = ['hoang-hon-sky-45', 'buffet-sang-ba-mien', 'hoi-nghi-tron-goi-2026', 'diem-den-van-hoa-cau-giay', 'can-ho-dich-vu-cong-tac-dai-ngay',
         'cuoi-tuan-cho-gia-dinh', 'mua-su-kien-my-dinh', 'bua-toi-nhin-ra-thanh-pho', 'panoramic-suite', 'tu-grand-k-den-pho-co']
for _n, _s in zip(NEWS, SLUGS):
    _n['slug'] = _s

NEWS_CATS = [('all', 'Tất cả'), ('offer', 'Ưu đãi'), ('dining', 'Ẩm thực'), ('event', 'Sự kiện'), ('explore', 'Khám phá Hà Nội'), ('stay', 'Lưu trú')]

FAQ_ROOMS = [
    ('Giờ nhận và trả phòng là khi nào?', 'Nhận phòng từ 14:00 và trả phòng trước 12:00. Nhận phòng sớm hoặc trả phòng muộn tuỳ tình trạng phòng — vui lòng báo trước cho lễ tân.'),
    ('Căn hộ có phù hợp cho kỳ lưu trú dài ngày không?', 'Có. Các hạng căn hộ có bếp riêng và phòng khách, rất phù hợp cho gia đình hoặc chuyên gia công tác dài ngày. Liên hệ để nhận báo giá theo tuần, theo tháng.'),
    ('Khách sạn có dịch vụ đưa đón sân bay không?', 'Có dịch vụ đưa đón sân bay Nội Bài theo yêu cầu. Vui lòng đặt trước ít nhất 24 giờ.'),
    ('Tôi có thể huỷ hoặc thay đổi đặt phòng không?', 'Điều kiện huỷ, đổi phụ thuộc vào từng gói giá. Thông tin chi tiết hiển thị ở bước đặt phòng và trong email xác nhận.'),
]
FAQ_CONTACT = [
    ('Tôi nên liên hệ kênh nào để được hỗ trợ nhanh nhất?', f'Với yêu cầu gấp, vui lòng gọi {PHONE}. Với yêu cầu báo giá hội nghị hoặc lưu trú dài ngày, hãy gửi form bên trên để bộ phận phụ trách liên hệ lại.'),
    ('Khách sạn có hỗ trợ tổ chức hội nghị, sự kiện không?', 'Có. Khách sạn có không gian hội nghị 175 m² với âm thanh, sân khấu và màn hình LED, cùng các gói tea-break và lưu trú cho đoàn.'),
    ('Có thể đặt bàn tại nhà hàng hoặc SKY 45 không?', 'Có. Chọn chủ đề “Nhà hàng & SKY 45” trong form hoặc gọi trực tiếp cho lễ tân để giữ bàn.'),
    ('Khách sạn cách sân bay Nội Bài bao xa?', 'Khách sạn kết nối nhanh với tuyến cao tốc đi Nội Bài. Bạn có thể đặt dịch vụ đưa đón khi xác nhận đặt phòng.'),
]

# ------------------------------------------------------------------ helpers
MOTION_HEAD = """<script>(function(r){if(!/[?&]shot/.test(location.search)&&!matchMedia('(prefers-reduced-motion: reduce)').matches){r.classList.add('motion');setTimeout(function(){if(!window.gsap)r.classList.remove('motion')},3500)}})(document.documentElement)</script>"""
SCRIPTS = """<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.20/dist/lenis.min.js"></script>
<script src="assets/js/base.js"></script>
<script src="assets/js/motion.js"></script>
<script src="assets/js/pages.js"></script>"""
STARS = '<i data-icon="star"></i>' * 5


def href(o, key):
    if key == 'home':
        return f'option-{o}.html'
    if key.startswith('home#'):
        return f'option-{o}.html#{key[5:]}'
    return f'option-{o}-{key}.html'


NAV = {
    1: [('Hạng phòng', 'rooms'), ('Ẩm thực', 'home#facilities'), ('Hội nghị', 'home#facilities'), ('Tiện ích', 'home#facilities'), ('Tin tức', 'news'), ('Liên hệ', 'contact')],
    4: [('Hạng phòng', 'rooms'), ('Dịch vụ', 'home#services'), ('Vị trí', 'home#location'), ('Tin tức', 'news'), ('Liên hệ', 'contact')],
    5: [('Hạng phòng', 'rooms'), ('Dịch vụ', 'home#services'), ('Ưu đãi', 'home#offers'), ('Tin tức', 'news'), ('Liên hệ', 'contact')],
}


def nav_links(o, active):
    act = ' class="active" aria-current="page"'
    return ''.join(f'<a href="{href(o, k)}"{act if k == active else ""}>{t}</a>' for t, k in NAV[o])


def head_html(o, page, title=None, bodycls=None):
    title = f'{title or PAGES[page]} — Grand K Hotel Suites Hanoi · Option 0{o} {NAMES[o]}'
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{MOTION_HEAD}
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Tangerine:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/base.css">
<link rel="stylesheet" href="assets/css/pages.css">
<link rel="stylesheet" href="assets/css/theme-{o}.css">
</head>
<body class="t{o} page-{bodycls or page}">
<div class="loader" aria-hidden="true"><img src="assets/img/logo.png" alt=""><span class="bar"><i></i></span></div>
'''


def drawer(o, active):
    script = {1: 'Welcome home', 4: 'Stay a while', 5: 'Hotel Suites'}[o]
    return f'''<div class="drawer">
  <div class="drawer-top"><img src="assets/img/logo.png" alt="" style="height:36px"><button class="menu-btn" style="display:inline-flex" data-menu-toggle aria-label="Đóng menu"><i data-icon="close"></i></button></div>
  <nav><a href="{href(o, 'home')}">Trang chủ</a>{nav_links(o, active)}</nav>
  <span class="script">{script}</span>
</div>
'''


def header(o, active):
    small = ' style="height:34px"' if o == 5 else ''
    logo = f'<a href="{href(o, "home")}" class="logo"><img src="assets/img/logo.png" alt="Grand K Hotel Suites Hanoi"{small}></a>'
    nav = f'<nav class="nav" aria-label="Điều hướng chính">{nav_links(o, active)}</nav>'
    book = href(o, 'rooms') + '#book'
    if o == 1:
        return f'''<header class="hdr" data-header>
  <div class="container">
    {logo}
    {nav}
    <div style="display:flex;align-items:center;gap:8px"><a href="{book}" class="btn btn-outline-light hide-tablet"><i data-icon="calendar"></i>Đặt phòng</a><button class="menu-btn" data-menu-toggle aria-label="Mở menu"><i data-icon="menu"></i></button></div>
  </div>
</header>
'''
    if o == 4:
        return f'''<header class="hdr">
  <div class="container">
    {logo}
    {nav}
    <div style="display:flex;align-items:center;gap:16px"><span class="lang t-xs hide-tablet"><b>VI</b> <span>/ EN / JP / KR / CN</span></span><button class="menu-btn" data-menu-toggle aria-label="Mở menu"><i data-icon="menu"></i></button></div>
  </div>
</header>
'''
    return f'''<header class="hdr">
      {logo}
      {nav}
      <div class="actions"><a href="{book}" class="btn btn-dark btn-pill btn-sm hide-tablet">Đặt phòng</a><button class="menu-btn" style="display:inline-flex" data-menu-toggle aria-label="Mở menu"><i data-icon="menu"></i></button></div>
    </header>'''


def crumbs(o, page, trail=None):
    trail = trail or [(PAGES[page], None)]
    parts = [f'<a href="{href(o, "home")}">Trang chủ</a>']
    for label, link in trail:
        parts.append(f'<a href="{link}">{label}</a>' if link else f'<span class="cur" aria-current="page">{label}</span>')
    sep = '<span aria-hidden="true">/</span>'
    return f'<nav class="crumbs t-xs t-caps" aria-label="Breadcrumb" data-hero>{sep.join(parts)}</nav>'


def page_hero(o, page, h):
    """h: dict(eyebrow, script, title, lead, img, side)"""
    if o == 1:
        return f'''<section class="p-hero">
  <div class="hm px" data-hero="media" style="position:absolute;inset:0"><img src="assets/img/{h['img']}" alt="" data-parallax="10"></div>
  <div class="container inner">
    {crumbs(o, page, h.get('crumbs'))}
    <span class="t-script-xl" data-hero="script">{h['script']}</span>
    <h1 data-hero="split">{h['title']}</h1>
    <p class="t-lead" data-hero>{h['lead']}</p>
  </div>
</section>
'''
    if o == 4:
        return f'''<section class="p-hero">
  <div class="hm px" data-hero="media" style="position:absolute;inset:0"><img src="assets/img/{h['img']}" alt="" data-parallax="8"></div>
  <div class="container crumbs-wrap" style="position:absolute;z-index:2;top:116px;left:0;right:0">{crumbs(o, page, h.get('crumbs')).replace('class="crumbs', 'style="color:rgba(255,255,255,.85)" class="crumbs')}</div>
  <div class="bot">
    <div class="container g12">
      <div class="ttl">
        <span class="eyebrow" data-hero>{h['eyebrow']}</span>
        <span class="t-script" data-hero="script">{h['script']}</span>
        <h1 data-hero="split">{h['title']}</h1>
      </div>
      <p class="side t-sm" data-hero>{h['lead']}</p>
    </div>
  </div>
</section>
'''
    return f'''<section class="card p-hero">
    <div class="container">
    {header(o, page)}
      <div class="g12 p-top">
        <div class="ttl">
          {crumbs(o, page, h.get('crumbs'))}
          <div style="position:relative"><span class="mark-script t-script" data-hero="script">{h['script']}</span><h1 data-hero="split">{h['title']}</h1></div>
        </div>
        <p class="note t-sm" data-hero>{h['lead']}</p>
      </div>
    </div>
    <div class="p-media px" data-hero="media"><img src="assets/img/{h['img']}" alt="" data-parallax="8"></div>
  </section>
'''


def sec(o, inner, cls='', alt=False, sid=''):
    idattr = f' id="{sid}"' if sid else ''
    if o == 5:
        return f'<section class="card {cls}"{idattr}>\n  <div class="container">\n{inner}\n  </div>\n</section>\n'
    return f'<section class="section {"pg-alt " if alt else ""}{cls}"{idattr}>\n  <div class="container">\n{inner}\n  </div>\n</section>\n'


def shead(o, num, eyebrow, script, title, text='', center=False):
    p = f'<p data-fade>{text}</p>' if text else ''
    if o == 4:
        return f'''<div class="pg-head">
  <span class="label eyebrow" data-fade><i>{num}</i>{eyebrow}</span>
  <div class="body"><h2 class="pg-h2" data-split><span class="t-script">{script}</span> {title}</h2>{p}</div>
</div>'''
    if o == 5:
        return f'''<div class="pg-head">
  <span class="kicker eyebrow" data-fade>{eyebrow}</span>
  <h2 class="pg-h2" style="margin-top:var(--s2)" data-split>{title} <span class="t-script">{script}</span></h2>{p}
</div>'''
    return f'''<div class="pg-head{" center" if center else ""}">
  <span class="eyebrow" data-fade>{eyebrow}</span>
  <span class="t-script" data-script>{script}</span>
  <h2 class="pg-h2" data-split>{title}</h2>{p}
</div>'''


def footer(o):
    if o == 1:
        return f'''<footer class="ftr" id="footer">
  <div class="container">
    <div class="g12 ftr-top t-sm" data-stagger>
      <div><img src="assets/img/logo.png" alt="Grand K" style="height:52px"><span class="t-script-sm">See you soon</span><p>Chào mừng bạn đến với Grand K Hotel Suites Hà Nội.</p></div>
      <div><h4 class="eyebrow">Khám phá</h4><ul><li><a href="{href(o,'rooms')}">Hạng phòng</a></li><li><a href="{href(o,'home#facilities')}">Ẩm thực</a></li><li><a href="{href(o,'home#facilities')}">Hội nghị</a></li><li><a href="{href(o,'news')}">Tin tức</a></li><li><a href="{href(o,'contact')}">Liên hệ</a></li></ul></div>
      <div><h4 class="eyebrow">Liên hệ</h4><ul class="contact"><li><i data-icon="pin"></i>{ADDRESS}</li><li><i data-icon="phone"></i><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><i data-icon="mail"></i><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
      <div><h4 class="eyebrow">Nhận ưu đãi</h4><p>Đăng ký để nhận ưu đãi đặt phòng trực tiếp sớm nhất.</p><form class="news" onsubmit="event.preventDefault()"><input type="email" placeholder="Email của bạn" aria-label="Email"><button aria-label="Đăng ký"><i data-icon="arrow"></i></button></form></div>
    </div>
    <div class="ftr-line" data-line></div>
    <div class="ftr-bot t-xs"><span>© 2026 Grand K Hotel Suites Hanoi</span><span>Điều khoản · Chính sách bảo mật · Facebook · Instagram · LinkedIn</span></div>
  </div>
</footer>
'''
    if o == 4:
        return f'''<footer class="ftr" id="footer">
  <div class="container">
    <div class="g12 t-sm" data-stagger>
      <div class="brand"><img src="assets/img/logo.png" alt="Grand K" style="height:48px"><p style="margin-top:var(--s2)">Hotel Suites Hanoi</p></div>
      <div class="cols">
        <div><h4 class="t-h4">Dịch vụ</h4><ul><li><a href="{href(o,'rooms')}">Hạng phòng</a></li><li><a href="{href(o,'home#services')}">Ẩm thực</a></li><li><a href="{href(o,'home#services')}">SKY 45</a></li><li><a href="{href(o,'home#services')}">Hội nghị</a></li></ul></div>
        <div><h4 class="t-h4">Khách lưu trú</h4><ul><li><a href="{href(o,'news')}">Tin tức &amp; ưu đãi</a></li><li><a href="{href(o,'home#location')}">Vị trí</a></li><li><a href="{href(o,'contact')}">Liên hệ</a></li></ul></div>
        <div><h4 class="t-h4">Liên hệ</h4><ul><li>{ADDRESS}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
      </div>
    </div>
    <div class="ftr-line" data-line></div>
    <div class="ftr-bot t-xs"><span>© 2026 Grand K Hotel Suites Hanoi. All rights reserved.</span><span>Facebook · Instagram · LinkedIn</span></div>
  </div>
</footer>
'''
    return f'''<footer class="card ftr" id="footer">
    <div class="container">
      <div class="g12 ftr-top t-sm" data-stagger>
        <div><p>Sẵn sàng cho kỳ lưu trú tiếp theo? Hãy để chúng tôi chuẩn bị mọi thứ.</p><a href="mailto:{EMAIL}" class="mail">{EMAIL}</a></div>
        <div><h4 class="eyebrow">Khám phá</h4><ul><li><a href="{href(o,'rooms')}">Hạng phòng</a></li><li><a href="{href(o,'home#services')}">Dịch vụ</a></li><li><a href="{href(o,'news')}">Tin tức</a></li><li><a href="{href(o,'contact')}">Liên hệ</a></li></ul></div>
        <div><h4 class="eyebrow">Liên hệ</h4><ul><li>{ADDRESS}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li></ul></div>
        <div><h4 class="eyebrow">Mạng xã hội</h4><ul><li><a href="#">Facebook</a></li><li><a href="#">Instagram</a></li><li><a href="#">LinkedIn</a></li></ul></div>
      </div>
      <div class="giant" aria-hidden="true"><span data-fade>Grand K</span><span class="t-script" data-script>see you soon</span></div>
      <div class="ftr-line" data-line></div>
      <div class="ftr-bot t-xs"><span>© 2026 Grand K Hotel Suites Hanoi</span><span>Điều khoản · Chính sách bảo mật</span></div>
    </div>
  </footer>
'''


def page(o, key, hero, body, title=None, bodycls=None):
    mbar = f'<div class="mbar"><a href="tel:{PHONE_TEL}" aria-label="Gọi"><i data-icon="phone"></i></a><a href="{href(o, "rooms")}#book">Đặt phòng ngay</a></div>'
    if o == 5:
        main = f'<div class="wrap">\n  {page_hero(o, key, hero)}<main>\n{body}</main>\n  {footer(o)}</div>\n'
        top = ''
    else:
        top = header(o, key)
        main = f'<main>\n{page_hero(o, key, hero)}{body}</main>\n{footer(o)}'
    return head_html(o, key, title, bodycls) + top + drawer(o, key) + main + mbar + '\n' + SCRIPTS + '\n</body>\n</html>\n'


# ------------------------------------------------------------------ ROOMS page
def specs(r):
    third = ('bed', 'Phòng ngủ', r['bedrooms']) if r['cat'] == 'apt' else ('bed', 'Giường', r['bed'])
    items = [('area', 'Diện tích', f"{r['size']} m²"), ('view', 'Hướng nhìn', r['view']), third,
             ('kitchen' if r['kitchen'] else 'building', 'Loại', r['kind'] + (' · bếp riêng' if r['kitchen'] else ''))]
    return ''.join(f'<li><i data-icon="{ic}"></i><span><small>{lab}</small>{val}</span></li>' for ic, lab, val in items)


def room_row(o, i, r):
    amen = (APT_AMEN + ROOM_AMEN[:4]) if r['kitchen'] else ROOM_AMEN[:5]
    return f'''<article class="g12 room-row" id="{r['id']}" data-cat="{r['cat']}">
  <a href="option-{o}-room-{r['id']}.html" class="media px" data-img aria-label="Xem chi tiết {r['name']}"><img src="assets/img/{r['img']}" alt="{r['name']}" data-parallax="6"><span class="no eyebrow">{i:02d} / {len(ROOMS):02d}</span></a>
  <div class="info">
    <span class="tagline eyebrow" data-fade>{r['kind']} · {r['size']} m²</span>
    <h3 class="pg-h2" data-split><a href="option-{o}-room-{r['id']}.html">{r['name']}</a></h3>
    <p data-fade>{r['desc']}</p>
    <ul class="specs t-sm" data-stagger>{specs(r)}</ul>
    <div class="amen-mini" data-fade>{''.join(f'<span>{a}</span>' for a in amen)}</div>
    <div class="actions" data-fade><a href="#book" class="btn btn-primary{' btn-pill' if o != 1 else ''}"><i data-icon="calendar"></i>Đặt phòng</a><a href="option-{o}-room-{r['id']}.html" class="btn btn-outline{' btn-pill' if o != 1 else ''}">Xem chi tiết <i data-icon="arrow"></i></a></div>
  </div>
</article>'''


def rooms_page(o):
    img = {1: 'room-2br-pano.jpg', 4: 'room-1br.jpg', 5: 'room-premium.jpg'}[o]
    hero = dict(eyebrow='Hạng phòng & Căn hộ', script='Rooms & Suites', img=img,
                title='Hạng phòng &amp; Căn hộ' if o != 1 else 'Hạng phòng<br>&amp; Căn hộ',
                lead='Sáu hạng phòng — từ 30 m² ấm cúng đến căn hộ hai phòng ngủ 95 m² với tầm nhìn toàn cảnh phía Tây Hà Nội.')
    chips = ''.join(f'<button class="chip{" on" if f == "all" else ""}" data-f="{f}">{t}</button>' for f, t in [('all', 'Tất cả'), ('room', 'Phòng'), ('suite', 'Suite'), ('apt', 'Căn hộ')])
    filt = f'''<div class="filter-bar">
  <div class="container">
    <div class="chips-bar" data-filter-for="#roomList" data-count="#roomCount" role="group" aria-label="Lọc hạng phòng">{chips}</div>
    <span class="count t-sm" id="roomCount" aria-live="polite">{len(ROOMS)} kết quả</span>
  </div>
</div>
'''
    rows = '\n'.join(room_row(o, i + 1, r) for i, r in enumerate(ROOMS))
    s1 = sec(o, shead(o, '01', 'Bộ sưu tập', 'Stay', 'Chọn không gian phù hợp với bạn',
                      'Mỗi hạng phòng được thiết kế cho một nhịp sống — công tác ngắn ngày, nghỉ dưỡng cặp đôi hay kỳ lưu trú dài cùng gia đình.')
             + f'\n<div class="room-list" id="roomList">\n{rows}\n</div>', sid='list')

    amen_items = [('wifi', 'Wifi tốc độ cao', 'Kết nối ổn định cho công việc và giải trí.'), ('bed', 'Giường cao cấp', 'Chăn ga gối nệm tiêu chuẩn khách sạn 5 sao.'),
                  ('view', 'Tầm nhìn thành phố', 'Ô kính lớn đón ánh sáng tự nhiên.'), ('kitchen', 'Bếp riêng ở căn hộ', 'Trang bị cho kỳ lưu trú dài ngày.'),
                  ('spa', 'Dọn phòng hằng ngày', 'Không gian luôn gọn gàng, thư thái.'), ('car', 'Đưa đón sân bay', 'Đặt trước cùng phòng của bạn.'),
                  ('pool', 'Hồ bơi nước nóng', 'Bơi quanh năm dưới mái kính.'), ('bar', 'SKY 45 Bar', 'Cocktail trên tầng thượng mỗi tối.')]
    amen = ''.join(f'<div><i data-icon="{ic}"></i><div><h3 class="t-h4">{t}</h3><p class="t-sm">{d}</p></div></div>' for ic, t, d in amen_items)
    s2 = sec(o, shead(o, '02', 'Tiện nghi', 'Comfort', 'Tiện nghi trong mọi hạng phòng') + f'\n<div class="g12 amen-grid" data-stagger>{amen}</div>', alt=True)

    trs = ''.join(f'''<tr><th scope="row"><a href="option-{o}-room-{r['id']}.html">{r['name']}</a></th><td>{r['kind']}</td><td>{r['size']} m²</td><td>{r['bedrooms'] if r['cat'] == 'apt' else r['bed']}</td><td>{'<span class="yes">✓ Có</span>' if r['kitchen'] else '<span class="no-x">—</span>'}</td><td>{r['view']}</td><td><a href="#book" class="link-arrow" style="color:var(--petrol)">Đặt <i data-icon="arrow"></i></a></td></tr>''' for r in ROOMS)
    table = f'''<div class="compare-wrap" data-fade><table class="compare">
  <thead><tr><th scope="col">Hạng phòng</th><th scope="col">Loại</th><th scope="col">Diện tích</th><th scope="col">Giường / phòng ngủ</th><th scope="col">Bếp riêng</th><th scope="col">Hướng nhìn</th><th scope="col"><span class="sr-only">Đặt phòng</span></th></tr></thead>
  <tbody>{trs}</tbody>
</table></div>'''
    s3 = sec(o, shead(o, '03', 'So sánh', 'Compare', 'So sánh nhanh các hạng phòng') + '\n' + table, sid='compare')

    perks = [('star', 'Giá tốt nhất', 'Mức giá tốt nhất khi đặt trực tiếp trên website chính thức.'),
             ('calendar', 'Linh hoạt giờ giấc', 'Ưu tiên nhận phòng sớm, trả phòng muộn tuỳ tình trạng phòng.'),
             ('bar', 'Đồ uống chào mừng', 'Một ly cocktail chào mừng tại SKY 45 cho mỗi kỳ lưu trú.')]
    pk = ''.join(f'<div class="perk"><i data-icon="{ic}"></i><h3 class="t-h4">{t}</h3><p class="t-sm">{d}</p></div>' for ic, t, d in perks)
    s4 = sec(o, shead(o, '04', 'Đặt trực tiếp', 'Direct', 'Quyền lợi khi đặt trên website') + f'\n<div class="g12 perks" data-stagger>{pk}</div>\n<p class="t-xs t-muted" style="margin-top:var(--s3)">* Quyền lợi minh hoạ cho prototype — cần khách sạn xác nhận.</p>', alt=True)

    s5 = sec(o, faq_block(o, FAQ_ROOMS, 'Câu hỏi thường gặp', 'Những điều khách lưu trú thường hỏi trước khi đặt phòng.'))
    return page(o, 'rooms', hero, filt + s1 + s2 + s3 + s4 + s5 + cta_band(o))


def faq_block(o, items, title, text):
    det = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q}<span class="pm" aria-hidden="true"></span></summary><p class="ans">{a}</p></details>' for i, (q, a) in enumerate(items))
    eyebrow = '<span class="label eyebrow" data-fade><i>05</i>FAQ</span>' if o == 4 else ('<span class="kicker eyebrow" data-fade>FAQ</span>' if o == 5 else '<span class="eyebrow" data-fade style="color:var(--gold)">FAQ</span>')
    return f'''<div class="g12">
  <div class="faq-head">{eyebrow}<h2 class="pg-h2" style="margin-top:var(--s2)" data-split>{title}</h2><p class="t-muted" style="margin-top:var(--s3)" data-fade>{text}</p></div>
  <div class="faq" data-fade>{det}</div>
</div>'''


def cta_band(o):
    form = '''<form class="booking">
        <div class="field"><label for="ci">Nhận phòng</label><input id="ci" type="date" data-checkin></div>
        <div class="field"><label for="co">Trả phòng</label><input id="co" type="date" data-checkout></div>
        <div class="field"><label for="gu">Số khách</label><select id="gu"><option>2 người lớn · 1 phòng</option><option>1 người lớn · 1 phòng</option><option>2 người lớn, 1 trẻ em</option><option>4 người lớn · 2 phòng</option></select></div>
        <button type="submit" class="btn btn-primary">Kiểm tra phòng trống <i data-icon="arrow"></i></button>
      </form>'''
    inner = f'''<div class="container">
      <span class="t-script" data-script>Reserve</span>
      <h2 class="pg-h2" data-split>Sẵn sàng cho kỳ lưu trú của bạn?</h2>
      <div data-fade>{form}</div>
    </div>'''
    cls = 'card cta-band px' if o == 5 else 'cta-band px'
    return f'''<section class="{cls}" id="book">
  <img src="assets/img/hotel-night.jpg" alt="" data-parallax="10">
  {inner}
</section>
'''


# ------------------------------------------------------------------ NEWS page
def news_card(n, o):
    return f'''<a href="option-{o}-news-{n['slug']}.html" class="news-card" data-cat="{n['cat']}">
  <figure class="media zoom"><img class="cover" src="assets/img/{n['img']}" alt=""><span class="badge-cat t-xs t-caps">{n['label']}</span></figure>
  <div class="meta-line t-xs t-caps"><time>{n['date']}</time><span class="dot"></span><span>{n['read']} đọc</span></div>
  <h3 class="pg-h3">{n['title']}</h3>
  <p class="t-sm">{n['ex']}</p>
  <span class="link-arrow">Đọc tiếp <i data-icon="arrow"></i></span>
</a>'''


def news_page(o):
    img = {1: 'dining.jpg', 4: 'skybar.jpg', 5: 'lobby.jpg'}[o]
    hero = dict(eyebrow='Tin tức & Ưu đãi', script='Journal', img=img, title='Tin tức &amp; Ưu đãi',
                lead='Câu chuyện, sự kiện và ưu đãi mới nhất từ Grand K Hotel Suites — cùng những gợi ý khám phá phía Tây Hà Nội.')
    f = NEWS[0]
    feat = f'''<article class="g12 news-featured">
  <a href="option-{o}-news-{f['slug']}.html" class="media px" data-img aria-label="Đọc bài viết"><img src="assets/img/{f['img']}" alt="" data-parallax="6"></a>
  <div class="info">
    <div class="meta-line t-xs t-caps" data-fade><span class="cat">Nổi bật · {f['label']}</span><span class="dot"></span><time>{f['date']}</time><span class="dot"></span><span>{f['read']} đọc</span></div>
    <h2 class="pg-h2" data-split>{f['title']}</h2>
    <p data-fade>{f['ex']}</p>
    <div data-fade><a href="option-{o}-news-{f['slug']}.html" class="btn btn-primary{' btn-pill' if o != 1 else ''}">Đọc bài viết <i data-icon="arrow"></i></a></div>
  </div>
</article>'''
    s1 = sec(o, shead(o, '01', 'Nổi bật', 'Featured', 'Câu chuyện mới nhất') + '\n' + feat)
    chips = ''.join(f'<button class="chip{" on" if k == "all" else ""}" data-f="{k}">{t}</button>' for k, t in NEWS_CATS)
    filt = f'''<div class="filter-bar">
  <div class="container">
    <div class="chips-bar" data-filter-for="#newsList" data-count="#newsCount" role="group" aria-label="Lọc chuyên mục">{chips}</div>
    <span class="count t-sm" id="newsCount" aria-live="polite">{len(NEWS) - 1} kết quả</span>
  </div>
</div>
'''
    grid = '\n'.join(news_card(n, o) for n in NEWS[1:])
    pag = '<nav class="pagination" aria-label="Phân trang"><a href="#" aria-label="Trang trước">‹</a><a href="#" class="on" aria-current="page">1</a><a href="#">2</a><a href="#">3</a><a href="#" aria-label="Trang sau">›</a></nav>'
    s2 = sec(o, shead(o, '02', 'Tất cả bài viết', 'Stories', 'Ưu đãi, ẩm thực &amp; khám phá') + f'\n<div class="g12 news-grid" id="newsList" data-stagger>\n{grid}\n</div>\n{pag}', alt=(o != 5), sid='all')
    nl = f'''<div class="g12 newsletter">
  <div class="copy"><span class="t-script" data-script style="color:var(--gold)">Stay in touch</span><h2 class="pg-h2" data-split>Nhận tin &amp; ưu đãi sớm nhất</h2><p class="t-muted" data-fade style="margin-top:var(--s2)">Mỗi tháng một email: ưu đãi đặt trực tiếp, sự kiện và gợi ý khám phá Hà Nội.</p></div>
  <form data-fade onsubmit="event.preventDefault();this.querySelector('button').textContent='Đã đăng ký ✓'"><input type="email" required placeholder="Email của bạn" aria-label="Email"><button class="btn btn-primary{' btn-pill' if o != 1 else ''}">Đăng ký</button></form>
</div>'''
    s3 = sec(o, nl, alt=(o == 5))
    note = sec(o, '<p class="t-xs t-muted center">* Bài viết, ngày đăng và ưu đãi là nội dung mẫu cho prototype.</p>', cls='tight') if o == 5 else '<p class="t-xs t-muted center" style="padding-bottom:var(--s5)">* Bài viết, ngày đăng và ưu đãi là nội dung mẫu cho prototype.</p>'
    return page(o, 'news', hero, s1 + filt + s2 + s3 + note)


# ------------------------------------------------------------------ CONTACT page
def contact_page(o):
    img = {1: 'entrance.jpg', 4: 'facade.jpg', 5: 'entrance.jpg'}[o]
    hero = dict(eyebrow='Liên hệ', script='Get in touch', img=img, title='Liên hệ với chúng tôi',
                lead='Đội ngũ Grand K luôn sẵn sàng hỗ trợ đặt phòng, hội nghị và mọi yêu cầu cho kỳ lưu trú của bạn.')
    pill = ' btn-pill' if o != 1 else ''
    cards = [('pin', 'Địa chỉ', ADDRESS, '<a href="#map" class="link-arrow t-xs" style="color:var(--petrol);margin-top:8px">Chỉ đường <i data-icon="arrow"></i></a>'),
             ('phone', 'Điện thoại', f'<a href="tel:{PHONE_TEL}">{PHONE}</a>', '<span class="t-sm t-muted">Lễ tân &amp; đặt phòng</span>'),
             ('mail', 'Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>', '<span class="t-sm t-muted">Báo giá hội nghị, lưu trú dài ngày</span>'),
             ('globe', 'Mạng xã hội', '<span><a href="#">Facebook</a> · <a href="#">Instagram</a> · <a href="#">LinkedIn</a></span>', '')]
    info = ''.join(f'<div class="info-card"><i data-icon="{ic}"></i><div><span class="eyebrow">{t}</span><div style="margin-top:4px">{v}</div>{x}</div></div>' for ic, t, v, x in cards)
    form = f'''<div class="contact-form-wrap" id="form" data-fade>
  <span class="eyebrow" style="color:var(--gold)">Gửi yêu cầu</span>
  <h2 class="pg-h3" style="margin-top:var(--s1)">Để lại lời nhắn, chúng tôi sẽ liên hệ lại sớm nhất</h2>
  <form class="cform" novalidate>
    <div class="fld"><label for="f-name">Họ và tên <i>*</i></label><input id="f-name" name="name" autocomplete="name"><span class="err" aria-live="polite"></span></div>
    <div class="fld"><label for="f-email">Email <i>*</i></label><input id="f-email" name="email" type="email" autocomplete="email"><span class="err" aria-live="polite"></span></div>
    <div class="fld"><label for="f-phone">Số điện thoại</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"><span class="err" aria-live="polite"></span></div>
    <div class="fld"><label for="f-topic">Chủ đề <i>*</i></label><select id="f-topic" name="topic"><option value="">Chọn chủ đề</option><option>Đặt phòng</option><option>Căn hộ lưu trú dài ngày</option><option>Hội nghị &amp; sự kiện</option><option>Nhà hàng &amp; SKY 45</option><option>Khác</option></select><span class="err" aria-live="polite"></span></div>
    <div class="fld"><label for="f-date">Ngày dự kiến</label><input id="f-date" name="date" type="date"><span class="err"></span></div>
    <div class="fld"><label for="f-guests">Số khách</label><select id="f-guests" name="guests"><option>1 – 2 khách</option><option>3 – 4 khách</option><option>5 – 10 khách</option><option>Đoàn trên 10 khách</option></select><span class="err"></span></div>
    <div class="fld full"><label for="f-msg">Lời nhắn <i>*</i></label><textarea id="f-msg" name="message" placeholder="Hãy cho chúng tôi biết yêu cầu của bạn…"></textarea><span class="err" aria-live="polite"></span></div>
    <label class="consent full"><input type="checkbox" name="consent"> Tôi đồng ý để Grand K Hotel Suites liên hệ lại theo thông tin đã cung cấp.</label>
    <div class="form-foot full"><span class="t-xs t-muted">* Thông tin bắt buộc</span><button type="submit" class="btn btn-primary{pill}">Gửi yêu cầu <i data-icon="arrow"></i></button></div>
  </form>
  <div class="form-ok" role="status"><i data-icon="mail"></i><h3 class="pg-h3">Cảm ơn <span data-name></span>!</h3><p class="t-muted" style="margin:var(--s2) auto var(--s4);max-width:40ch">Yêu cầu của bạn đã được ghi nhận. Đây là prototype nên chưa có dữ liệu nào được gửi đi.</p><button class="btn btn-outline{pill}" data-form-reset>Gửi yêu cầu khác</button></div>
</div>'''
    s1 = sec(o, shead(o, '01', 'Thông tin liên hệ', 'Hello', 'Chúng tôi luôn sẵn sàng hỗ trợ bạn') + f'\n<div class="g12 contact-grid"><div class="contact-info" data-stagger>{info}</div>{form}</div>')

    mapbox = f'''<div class="map-wrap" id="map" data-img>
  <iframe title="Bản đồ Grand K Hotel Suites Hanoi" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={MAPS_Q}&output=embed"></iframe>
  <div class="map-card"><img src="assets/img/logo.png" alt="" style="height:30px"><p class="t-sm">{ADDRESS}</p><a class="btn btn-primary btn-sm{pill}" href="https://maps.google.com/?q={MAPS_Q}" target="_blank" rel="noopener">Mở Google Maps <i data-icon="arrow"></i></a></div>
</div>'''
    dirs = [('plane', 'Sân bay Quốc tế Nội Bài', 'Kết nối nhanh qua tuyến cao tốc — đặt đưa đón cùng phòng.'),
            ('landmark', 'Trung tâm Hội nghị Quốc gia', 'Vài phút di chuyển — thuận tiện cho khách dự sự kiện.'),
            ('stadium', 'Sân vận động Mỹ Đình', 'Vài phút di chuyển từ khách sạn.'),
            ('building', 'Phố cổ Hà Nội', 'Khoảng 8 km về phía trung tâm.')]
    dr = ''.join(f'<div class="dir"><i data-icon="{ic}"></i><h3 class="t-h4">{t}</h3><p class="t-sm">{d}</p></div>' for ic, t, d in dirs)
    s2 = sec(o, shead(o, '02', 'Vị trí & đường đi', 'Find us', 'Trái tim của khu vực Tây Hà Nội') + f'\n{mapbox}\n<div class="g12 directions" data-stagger>{dr}</div>', alt=(o != 5), sid='location')
    s3 = sec(o, faq_block(o, FAQ_CONTACT, 'Câu hỏi thường gặp', 'Chưa tìm thấy câu trả lời? Gọi cho chúng tôi hoặc gửi yêu cầu bằng form phía trên.'))
    return page(o, 'contact', hero, s1 + s2 + s3)


if __name__ == '__main__':
    builders = {'rooms': rooms_page, 'news': news_page, 'contact': contact_page}
    for o in OPTS:
        for key, fn in builders.items():
            out = ROOT / f'option-{o}-{key}.html'
            out.write_text(fn(o), encoding='utf-8')
            print('wrote', out.name)
    import build_details
    build_details.main()
