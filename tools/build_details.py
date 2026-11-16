#!/usr/bin/env python3
"""Detail pages for Option 01 / 04 / 05: one page per room and per article.

Run via `python3 tools/build_pages.py` (it calls main() here) or directly.
Outputs: option-{o}-room-{id}.html (6 × 3) and option-{o}-news-{slug}.html (10 × 3).
"""
import re
from urllib.parse import quote
from build_pages import (ROOT, OPTS, ROOMS, NEWS, PHONE, PHONE_TEL, href, page, sec, shead, cta_band, ROOM_AMEN)

# ------------------------------------------------------------------ article bodies (sample copy)
# blocks: ('lead', text) · ('h2', text) · ('p', text) · ('list', [..]) · ('quote', text, cite) · ('fig', img, caption)
BODIES = {
    'hoang-hon-sky-45': [
        ('lead', 'Khi nắng chiều phía Tây buông xuống các tòa nhà Cầu Giấy, SKY 45 bắt đầu giờ đẹp nhất trong ngày. Mùa này, quầy bar trên tầng thượng ra mắt thực đơn cocktail mới lấy cảm hứng từ những gia vị quen thuộc của ẩm thực Việt.'),
        ('h2', 'Một thực đơn kể chuyện bằng hương vị'),
        ('p', 'Mỗi ly cocktail bắt đầu từ một nguyên liệu bản địa: quế, sả, trà sen hay vỏ bưởi. Đội ngũ pha chế cân bằng chúng với nền rượu quen thuộc để tạo ra những hương vị vừa lạ vừa gần gũi.'),
        ('p', 'Thực đơn được thiết kế ngắn gọn để khách dễ lựa chọn, kèm gợi ý món ăn nhẹ phù hợp với từng ly.'),
        ('fig', 'skybar.jpg', 'Không gian SKY 45 Outdoor nhìn về phía Tây thành phố.'),
        ('h2', 'Thời điểm đẹp nhất để ghé'),
        ('p', 'Khung giờ hoàng hôn là lúc SKY 45 đông khách nhất. Nếu đi theo nhóm, bạn nên đặt bàn trước qua lễ tân hoặc form liên hệ trên website.'),
        ('list', ['Đặt bàn trước cho nhóm từ 4 khách', 'Chọn bàn sát lan can để ngắm toàn cảnh', 'Hỏi bartender gợi ý ly cocktail theo khẩu vị']),
        ('quote', 'Quầy bar trên tầng thượng yên tĩnh với những ly cocktail ngon miệng.', 'Mr. Steven — Google Review'),
        ('h2', 'Ưu đãi cho khách lưu trú'),
        ('p', 'Khách lưu trú tại Grand K nhận một ly cocktail chào mừng tại SKY 45 khi đặt phòng trực tiếp trên website. Điều kiện chi tiết được gửi kèm email xác nhận đặt phòng.'),
    ],
    'buffet-sang-ba-mien': [
        ('lead', 'Bữa sáng là khoảnh khắc khách lưu trú nhắc đến nhiều nhất. Tại Grand K, buffet sáng là một vòng ẩm thực ba miền trước giờ làm việc.'),
        ('h2', 'Từ phở Hà Nội đến bánh mì'),
        ('p', 'Quầy món Việt có phở, bún và các món nước nóng. Bên cạnh là bánh mì, xôi và những món quen thuộc của bữa sáng Việt Nam.'),
        ('fig', 'dining.jpg', 'Khu buffet sáng tại nhà hàng của khách sạn.'),
        ('h2', 'Lựa chọn Âu và món nhẹ'),
        ('p', 'Với khách quốc tế hoặc người thích bữa sáng nhẹ, quầy Âu có bánh ngọt, trứng chế biến theo yêu cầu, trái cây và nước ép tươi.'),
        ('quote', 'Buffet sáng phong phú và đa dạng.', 'Mr. Scott — Tripadvisor'),
    ],
    'hoi-nghi-tron-goi-2026': [
        ('lead', 'Nằm gần Trung tâm Hội nghị Quốc gia, Grand K là lựa chọn thuận tiện cho doanh nghiệp tổ chức sự kiện tại khu vực phía Tây Hà Nội.'),
        ('h2', 'Không gian 175 m² linh hoạt'),
        ('p', 'Phòng hội nghị có hệ thống âm thanh, sân khấu và màn hình LED, phù hợp cho hội thảo, đào tạo nội bộ hay tiệc công ty.'),
        ('fig', 'meeting.jpg', 'Phòng hội nghị bố trí theo kiểu sự kiện.'),
        ('h2', 'Gói trọn gói gồm những gì'),
        ('list', ['Thuê phòng hội nghị theo buổi hoặc theo ngày', 'Tea-break và bữa trưa cho đoàn', 'Phòng nghỉ cho khách mời ở xa', 'Hỗ trợ kỹ thuật âm thanh, màn hình']),
        ('p', 'Để nhận báo giá theo quy mô sự kiện, hãy gửi yêu cầu với chủ đề “Hội nghị & sự kiện” trên trang Liên hệ.'),
    ],
    'diem-den-van-hoa-cau-giay': [
        ('lead', 'Một buổi chiều rảnh giữa chuyến công tác là đủ để khám phá vài điểm văn hoá gần khách sạn.'),
        ('h2', 'Bảo tàng Lịch sử Quân sự Việt Nam'),
        ('p', 'Không gian trưng bày ngoài trời và trong nhà kể lại lịch sử quân sự Việt Nam qua hiện vật, phù hợp cho cả gia đình.'),
        ('fig', 'loc-museum.jpg', 'Bảo tàng Lịch sử Quân sự Việt Nam.'),
        ('h2', 'Những điểm đến khác'),
        ('list', ['Trung tâm Hội nghị Quốc gia và khu vực xung quanh', 'Sân vận động Quốc gia Mỹ Đình', 'Hồ Gươm và khu Phố cổ, khoảng 8 km']),
        ('p', 'Lễ tân có thể gợi ý lộ trình và đặt xe cho bạn.'),
    ],
    'can-ho-dich-vu-cong-tac-dai-ngay': [
        ('lead', 'Với những chuyến công tác kéo dài nhiều tuần, một căn hộ dịch vụ mang lại sự riêng tư của ngôi nhà và tiện nghi của khách sạn.'),
        ('h2', 'Bếp riêng và phòng khách rộng'),
        ('p', 'Các hạng căn hộ từ 70 đến 95 m² có bếp riêng và phòng khách, giúp bạn chủ động sinh hoạt và tiếp khách.'),
        ('fig', 'room-2br-exec.jpg', 'Two Bedroom Executive Suite.'),
        ('h2', 'Dịch vụ khách sạn đi kèm'),
        ('list', ['Dọn phòng định kỳ', 'Hồ bơi nước nóng trong nhà', 'Buffet sáng tại nhà hàng', 'Đưa đón sân bay theo yêu cầu']),
        ('quote', 'Ngay cả phòng rẻ nhất cũng có bếp và phòng khách rộng rãi.', 'Mr. Zahabiya — Tripadvisor'),
    ],
    'cuoi-tuan-cho-gia-dinh': [
        ('lead', 'Không cần đi xa, một kỳ nghỉ cuối tuần ngay giữa Hà Nội cũng đủ để cả gia đình thư giãn.'),
        ('h2', 'Hồ bơi nước nóng quanh năm'),
        ('p', 'Hồ bơi trong nhà dưới mái kính cho phép cả nhà bơi thoải mái bất kể thời tiết.'),
        ('fig', 'pool.jpg', 'Hồ bơi nước nóng trong nhà.'),
        ('h2', 'Không gian cho các bé'),
        ('p', 'Khu vui chơi trẻ em an toàn giúp bố mẹ có thêm thời gian nghỉ ngơi.'),
        ('quote', 'Hồ bơi trong nhà ở đây là đẹp nhất Hà Nội.', 'Mr. Zahabiya — Tripadvisor'),
    ],
    'mua-su-kien-my-dinh': [
        ('lead', 'Mỗi mùa giải và mỗi đêm nhạc lớn, khu vực Mỹ Đình lại đông người. Lưu trú gần sân vận động giúp bạn chủ động thời gian.'),
        ('h2', 'Vài phút tới Sân vận động Quốc gia'),
        ('p', 'Từ Grand K, bạn có thể di chuyển nhanh tới Mỹ Đình trước giờ sự kiện và về nghỉ ngơi ngay sau đó.'),
        ('fig', 'loc-mydinh.jpg', 'Sân vận động Quốc gia Mỹ Đình.'),
        ('h2', 'Gợi ý cho ngày sự kiện'),
        ('list', ['Đặt phòng sớm vì mùa sự kiện thường kín phòng', 'Hỏi lễ tân về phương án di chuyển', 'Ăn tối tại khách sạn trước giờ diễn ra sự kiện']),
    ],
    'bua-toi-nhin-ra-thanh-pho': [
        ('lead', 'Kỷ niệm, sinh nhật hay một buổi hẹn: có những bữa tối cần thêm một khung cảnh đẹp.'),
        ('h2', 'Khi Cầu Giấy lên đèn'),
        ('p', 'Từ các tầng cao, thành phố về đêm trở thành phông nền cho bữa tối. Hãy cho chúng tôi biết dịp đặc biệt của bạn khi đặt bàn.'),
        ('fig', 'hotel-night.jpg', 'Toàn cảnh khu vực Cầu Giấy về đêm.'),
        ('p', 'Đặt bàn qua form liên hệ với chủ đề “Nhà hàng & SKY 45” hoặc gọi trực tiếp cho lễ tân.'),
    ],
    'panoramic-suite': [
        ('lead', 'Two Bedroom Panoramic Suite là căn hộ có tầm nhìn rộng nhất của Grand K: 95 m², hai phòng ngủ và ô kính lớn nhìn về phía Tây Hà Nội.'),
        ('h2', 'Không gian cho cả gia đình'),
        ('p', 'Hai phòng ngủ riêng biệt, phòng khách và bếp đầy đủ giúp căn hộ phù hợp cho gia đình hoặc nhóm bạn lưu trú dài ngày.'),
        ('fig', 'room-2br-pano.jpg', 'Two Bedroom Panoramic Suite.'),
        ('h2', 'Đẹp nhất khi thành phố lên đèn'),
        ('p', 'Buổi tối, ô kính lớn biến phòng khách thành nơi ngắm thành phố. Đây là lựa chọn được nhiều khách đặt cho các dịp đặc biệt.'),
        ('quote', 'Phòng sạch sẽ, rộng và có tầm nhìn toàn cảnh Tây Hà Nội.', 'Mr. Akumar — Google Review'),
    ],
    'tu-grand-k-den-pho-co': [
        ('lead', 'Phố cổ cách Grand K khoảng 8 km. Dưới đây là những cách di chuyển thuận tiện nhất.'),
        ('h2', 'Taxi và xe công nghệ'),
        ('p', 'Đây là lựa chọn linh hoạt nhất. Thời gian di chuyển phụ thuộc vào giờ cao điểm, nên hãy dự trù thêm thời gian vào buổi chiều.'),
        ('fig', 'loc-oldquarter.jpg', 'Hồ Gươm và khu vực Phố cổ.'),
        ('h2', 'Dịch vụ xe của khách sạn'),
        ('p', 'Nếu đi theo nhóm hoặc cần lịch trình cố định, hãy đặt xe qua lễ tân. Chúng tôi có thể gợi ý điểm dừng phù hợp.'),
        ('list', ['Tránh giờ cao điểm 17:00 – 19:00', 'Mang theo danh thiếp khách sạn để quay về dễ dàng', 'Hỏi lễ tân về các điểm tham quan buổi tối']),
    ],
}


def slugify(t):
    t = re.sub(r'<[^>]+>', '', t).lower()
    table = str.maketrans('àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ',
                          'aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyd')
    return re.sub(r'[^a-z0-9]+', '-', t.translate(table)).strip('-')[:48]


# ------------------------------------------------------------------ ROOM DETAIL
GALLERY_EXTRA = [('lobby.jpg', 'Sảnh khách sạn'), ('pool.jpg', 'Hồ bơi nước nóng trong nhà'), ('skybar.jpg', 'SKY 45 Outdoor'), ('dining.jpg', 'Nhà hàng & buffet sáng')]


def amen_groups(r):
    groups = [
        ('bed', 'Phòng ngủ', [f"Giường {r['bed']}", 'Chăn ga gối cao cấp', 'Rèm cản sáng', 'Bàn làm việc']),
        ('spa', 'Phòng tắm', ['Vòi sen', 'Đồ dùng phòng tắm cao cấp', 'Áo choàng & dép đi trong phòng', 'Máy sấy tóc']),
        ('wifi', 'Công nghệ', ['Wifi tốc độ cao', 'Smart TV', 'Điều hoà nhiệt độ', 'Két an toàn']),
        ('kitchen' if r['kitchen'] else 'dining', 'Ăn uống', (['Bếp riêng', 'Bàn ăn'] if r['kitchen'] else []) + ['Minibar', 'Máy pha trà & cà phê', 'Nước uống miễn phí']),
    ]
    return ''.join(f'<div><h3 class="t-h4"><i data-icon="{ic}"></i>{t}</h3><ul class="t-sm">{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for ic, t, items in groups)


def room_detail(o, idx):
    r = ROOMS[idx]
    pill = ' btn-pill' if o != 1 else ''
    hero = dict(eyebrow=f"{r['kind']} · {r['size']} m²", script='Your stay', img=r['img'], title=r['name'],
                lead=r['desc'], crumbs=[('Hạng phòng', href(o, 'rooms')), (r['name'], None)])
    pics = [(r['img'], r['name'])] + GALLERY_EXTRA
    gal = ''.join(f'<a href="assets/img/{im}" data-caption="{cap}"><img src="assets/img/{im}" alt="{cap}" loading="lazy"><span class="cap t-xs t-caps">{cap}</span></a>' for im, cap in pics)
    gallery = f'<div class="gallery" data-lightbox data-fade>{gal}<button class="all t-sm" data-lightbox-open><i data-icon="view"></i>Xem {len(pics)} ảnh</button></div>'

    specs = [('area', 'Diện tích', f"{r['size']} m²"), ('bed', 'Phòng ngủ' if r['cat'] == 'apt' else 'Giường', r['bedrooms'] if r['cat'] == 'apt' else r['bed']),
             ('view', 'Hướng nhìn', r['view']), ('kitchen' if r['kitchen'] else 'building', 'Loại', r['kind'])]
    spec_html = ''.join(f'<li><i data-icon="{ic}"></i><span class="eyebrow t-muted">{lab}</span><b>{val}</b></li>' for ic, lab, val in specs)
    policy = '''<table class="policy t-sm"><tbody>
<tr><th scope="row">Nhận phòng / Trả phòng</th><td>Từ 14:00 / Trước 12:00</td></tr>
<tr><th scope="row">Nhận phòng sớm, trả phòng muộn</th><td>Tuỳ tình trạng phòng, vui lòng báo trước cho lễ tân</td></tr>
<tr><th scope="row">Huỷ / thay đổi đặt phòng</th><td>Theo điều kiện của từng gói giá, hiển thị ở bước đặt phòng</td></tr>
<tr><th scope="row">Đưa đón sân bay</th><td>Có, đặt trước ít nhất 24 giờ</td></tr>
</tbody></table>'''
    main = f'''<div class="rd-main">
  <section>
    <span class="eyebrow" style="color:var(--pg-accent)" data-fade>Tổng quan</span>
    <h2 class="pg-h2" style="margin-top:var(--s2)" data-split>{r['name']} — {r['size']} m² {'căn hộ' if r['kitchen'] else 'tinh tế'} giữa lòng Cầu Giấy</h2>
    <p class="t-lead" data-fade>{r['desc']} Không gian được hoàn thiện với tông màu ấm, ánh sáng tự nhiên và những tiện nghi cần thiết cho cả công việc lẫn nghỉ ngơi.</p>
    <ul class="rd-specs t-sm" data-stagger>{spec_html}</ul>
  </section>
  <section>
    <span class="eyebrow" style="color:var(--pg-accent)" data-fade>Tiện nghi</span>
    <h2 class="pg-h3" style="margin-top:var(--s2)" data-split>Mọi thứ bạn cần cho kỳ lưu trú</h2>
    <div class="amen-groups" data-stagger>{amen_groups(r)}</div>
  </section>
  <section>
    <span class="eyebrow" style="color:var(--pg-accent)" data-fade>Chính sách</span>
    <h2 class="pg-h3" style="margin-top:var(--s2)" data-split>Thông tin cần biết</h2>
    <div data-fade>{policy}</div>
    <p class="t-xs t-muted" style="margin-top:var(--s2)">* Tiện nghi và chính sách là nội dung mẫu cho prototype — cần khách sạn xác nhận.</p>
  </section>
</div>'''
    aside = f'''<aside class="rd-aside" data-fade>
  <form class="book-card booking-lite" onsubmit="event.preventDefault();alert('Prototype: bước này sẽ chuyển sang công cụ đặt phòng (Booking Engine).')">
    <span class="t-script-sm">Reserve</span>
    <h2 class="pg-h3">Đặt {r['name']}</h2>
    <div class="rows">
      <div class="two"><div class="field"><label for="rci">Nhận phòng</label><input id="rci" type="date" data-checkin></div><div class="field"><label for="rco">Trả phòng</label><input id="rco" type="date" data-checkout></div></div>
      <div class="field"><label for="rgu">Số khách</label><select id="rgu"><option>2 người lớn</option><option>1 người lớn</option><option>2 người lớn · 1 trẻ em</option>{'<option>4 người lớn</option>' if r['cat'] == 'apt' else ''}</select></div>
    </div>
    <button type="submit" class="btn btn-primary{pill}">Kiểm tra phòng trống <i data-icon="arrow"></i></button>
    <ul class="t-sm"><li><i data-icon="star"></i>Giá tốt nhất khi đặt trực tiếp</li><li><i data-icon="bar"></i>Đồ uống chào mừng tại SKY 45</li><li><i data-icon="calendar"></i>Ưu tiên nhận phòng sớm</li></ul>
    <div class="help t-sm"><span class="t-muted">Cần hỗ trợ?</span><a href="tel:{PHONE_TEL}" class="link-arrow" style="color:var(--petrol)">{PHONE}</a></div>
  </form>
</aside>'''
    s1 = sec(o, gallery + f'\n<div class="g12 rd-grid" style="margin-top:var(--s7)">{main}{aside}</div>')
    others = [ROOMS[(idx + k) % len(ROOMS)] for k in (1, 2, 3)]
    rel = ''.join(f'''<a href="option-{o}-room-{x['id']}.html" class="rel-card"><figure class="zoom"><img class="cover" src="assets/img/{x['img']}" alt="{x['name']}"></figure><div class="row"><h3 class="pg-h3">{x['name']}</h3><span class="t-xs t-caps">{x['size']} m²</span></div><p class="t-sm t-muted">{x['kind']} · {x['view']}</p></a>''' for x in others)
    s2 = sec(o, shead(o, '02', 'Khám phá thêm', 'More rooms', 'Các hạng phòng khác') + f'\n<div class="g12 related" data-stagger>{rel}</div>\n<div style="margin-top:var(--s5)" data-fade><a href="{href(o, "rooms")}" class="btn btn-outline{pill}">Xem tất cả hạng phòng <i data-icon="arrow"></i></a></div>', alt=(o != 5))
    return page(o, 'rooms', hero, s1 + s2 + cta_band(o), title=r['name'], bodycls='room')


# ------------------------------------------------------------------ ARTICLE DETAIL
def prose(blocks):
    out, toc = [], []
    for b in blocks:
        k = b[0]
        if k == 'lead':
            out.append(f'<p class="standfirst" data-fade>{b[1]}</p>')
        elif k == 'h2':
            sid = slugify(b[1]); toc.append((sid, b[1]))
            out.append(f'<h2 id="{sid}" data-split>{b[1]}</h2>')
        elif k == 'p':
            out.append(f'<p data-fade>{b[1]}</p>')
        elif k == 'list':
            out.append('<ul data-stagger>' + ''.join(f'<li>{x}</li>' for x in b[1]) + '</ul>')
        elif k == 'quote':
            out.append(f'<blockquote data-fade>“{b[1]}”<cite>{b[2]}</cite></blockquote>')
        elif k == 'fig':
            out.append(f'<figure><div class="frame px" data-img><img src="assets/img/{b[1]}" alt="{b[2]}" data-parallax="5"></div><figcaption>{b[2]}</figcaption></figure>')
    return '\n'.join(out), toc


def article(o, idx):
    n = NEWS[idx]
    pill = ' btn-pill' if o != 1 else ''
    hero = dict(eyebrow=f"{n['label']} · {n['date']}", script='Journal', img=n['img'], title=n['title'],
                lead=f"{n['label']} · {n['date']} · {n['read']} đọc", crumbs=[('Tin tức', href(o, 'news')), (n['label'], None)])
    body, toc = prose(BODIES[n['slug']])
    url = f'option-{o}-news-{n["slug"]}.html'
    meta = f'''<div class="art-meta">
  <div class="by"><img src="assets/img/logo.png" alt=""><div><b class="t-sm">Biên tập Grand K</b><div class="t-xs t-muted">{n['date']} · {n['read']} đọc</div></div></div>
  <div class="share" aria-label="Chia sẻ"><span class="eyebrow t-muted" style="margin-right:8px">Chia sẻ</span><a href="https://www.facebook.com/sharer/sharer.php" target="_blank" rel="noopener" aria-label="Chia sẻ Facebook">Fb</a><a href="mailto:?subject={quote(n['title'])}" aria-label="Gửi email">@</a><button type="button" data-copy-link aria-label="Sao chép liên kết">⧉</button></div>
</div>'''
    toc_html = '<nav class="toc" aria-label="Mục lục"><span class="eyebrow t-muted">Trong bài viết</span><ol>' + ''.join(f'<li><a href="#{sid}">{t}</a></li>' for sid, t in toc) + '</ol></nav>'
    prev_n, next_n = NEWS[(idx - 1) % len(NEWS)], NEWS[(idx + 1) % len(NEWS)]
    foot = f'''<div class="art-foot"><div class="tags"><a href="{href(o, 'news')}">{n['label']}</a><a href="{href(o, 'news')}">Grand K Hotel Suites</a><a href="{href(o, 'news')}">Cầu Giấy</a></div><a href="{href(o, 'news')}" class="link-arrow" style="color:var(--petrol)">Tất cả bài viết <i data-icon="arrow"></i></a></div>
<nav class="prevnext" aria-label="Bài viết trước và sau"><a href="option-{o}-news-{prev_n['slug']}.html"><span class="eyebrow">← Bài trước</span><span class="t-h4">{prev_n['title']}</span></a><a class="next" href="option-{o}-news-{next_n['slug']}.html"><span class="eyebrow">Bài tiếp →</span><span class="t-h4">{next_n['title']}</span></a></nav>'''
    s1 = sec(o, meta + f'\n<div class="g12 art-body">{toc_html}<article class="prose">{body}{foot}</article></div>')
    same = [x for x in NEWS if x['cat'] == n['cat'] and x is not n]
    rel = (same + [x for x in NEWS if x not in same and x is not n])[:3]
    cards = ''.join(f'''<a href="option-{o}-news-{x['slug']}.html" class="rel-card"><figure class="zoom"><img class="cover" src="assets/img/{x['img']}" alt=""></figure><div class="meta-line t-xs t-caps"><span class="cat">{x['label']}</span><span class="dot"></span><time>{x['date']}</time></div><h3 class="pg-h3" style="margin-top:var(--s1)">{x['title']}</h3></a>''' for x in rel)
    s2 = sec(o, shead(o, '02', 'Đọc tiếp', 'More stories', 'Bài viết liên quan') + f'\n<div class="g12 related" data-stagger>{cards}</div>', alt=(o != 5))
    nl = f'''<div class="g12 newsletter">
  <div class="copy"><span class="t-script" data-script style="color:var(--gold)">Stay in touch</span><h2 class="pg-h2" data-split>Nhận tin &amp; ưu đãi sớm nhất</h2></div>
  <form data-fade onsubmit="event.preventDefault();this.querySelector('button').textContent='Đã đăng ký ✓'"><input type="email" required placeholder="Email của bạn" aria-label="Email"><button class="btn btn-primary{pill}">Đăng ký</button></form>
</div>
<p class="t-xs t-muted" style="margin-top:var(--s4)">* Bài viết là nội dung mẫu cho prototype.</p>'''
    s3 = sec(o, nl)
    return page(o, 'news', hero, s1 + s2 + s3, title=n['title'], bodycls='article')


def main():
    n = 0
    for o in OPTS:
        for i, r in enumerate(ROOMS):
            (ROOT / f'option-{o}-room-{r["id"]}.html').write_text(room_detail(o, i), encoding='utf-8'); n += 1
        for i, a in enumerate(NEWS):
            (ROOT / f'option-{o}-news-{a["slug"]}.html').write_text(article(o, i), encoding='utf-8'); n += 1
    print('wrote', n, 'detail pages')


if __name__ == '__main__':
    main()
