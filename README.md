# Grand K Hotel Suites Hanoi — Redesign prototype

Prototype giao diện website mới cho Grand K Hotel Suites Hanoi: **3 phương án × 20 trang = 60 trang**, cùng một trang index tổng hợp. Viết bằng HTML/CSS/JavaScript thuần, không cần cài framework.

| Phương án | Tên | Ref tham khảo |
| --- | --- | --- |
| 01 | Grand Classic | Larita Luxury Hotel |
| 04 | Modern Grid | Lucomoria Resort |
| 05 | Bento Studio | Lumóra, Everlake, Stayli |

Mỗi phương án gồm: Trang chủ · Hạng phòng · 6 trang chi tiết phòng · Tin tức · 10 trang chi tiết bài viết · Liên hệ.

## Chạy trên máy

```bash
python3 -m http.server 5173
```

Mở http://localhost:5173 để vào trang index. Cần internet khi xem vì font (Google Fonts) và thư viện animation (GSAP, Lenis) tải từ CDN. Nếu mất mạng, trang vẫn hiển thị đầy đủ nhưng không có animation.

Mẹo khi demo:
- Thanh ở góc phải dưới mỗi trang dùng để chuyển giữa 3 phương án (giữ nguyên loại trang) và giữa các trang của cùng một phương án.
- Nhấn phím **G** để bật/tắt lưới cột 12/8/4.

## Cấu trúc thư mục

```
index.html                  Trang tổng hợp 3 phương án + design system
option-{1,4,5}.html         Trang chủ (viết tay)
option-{n}-rooms|news|contact.html      Trang danh sách (sinh tự động)
option-{n}-room-*.html, option-{n}-news-*.html   Trang chi tiết (sinh tự động)
assets/css/base.css         Design system: token, grid, type scale, nút, form…
assets/css/pages.css        Component cho trang con và trang chi tiết
assets/css/theme-{1,4,5}.css  Giao diện riêng từng phương án
assets/js/base.js           Icon, menu, slider, tab, thanh chuyển phương án, lưới (G)
assets/js/motion.js         Hệ thống animation (GSAP + ScrollTrigger + SplitText + Lenis)
assets/js/pages.js          Bộ lọc, form liên hệ, lightbox, mục lục bài viết
assets/img/                 Ảnh lấy từ grandkhanoi.com (đã nén)
tools/build_pages.py        Sinh 9 trang danh sách từ một nguồn nội dung
tools/build_details.py      Sinh 48 trang chi tiết (phòng + bài viết)
_v1/                        Bản trước khi chuẩn hoá design system, để đối chiếu
```

## Sửa nội dung trang con

Nội dung phòng, bài viết, FAQ, thông tin liên hệ nằm trong `tools/build_pages.py` và `tools/build_details.py`. Sau khi sửa, chạy:

```bash
python3 tools/build_pages.py
```

Lệnh này sinh lại toàn bộ 57 trang con của cả 3 phương án. Trang chủ (`option-1.html`, `option-4.html`, `option-5.html`) được viết tay, sửa trực tiếp.

## Design system

| Breakpoint | Khoảng rộng | Cột | Gutter | Lề |
| --- | --- | --- | --- | --- |
| XL | ≥ 1280px | 12 | 24px | 48px (nội dung 1200px) |
| LG | 1024–1279px | 12 | 24px | 40px |
| MD | 768–1023px | 8 | 20px | 32px |
| SM | 576–767px | 4 | 16px | 20px |
| XS | ≤ 575px | 4 | 16px | 16px |

Thang cỡ chữ (375 → 1440px): Display 44→96 · H1 40→72 · H2 32→52 · H3 22→28 · H4 18→20 · Lead 17→20 · Body 16 · Small 14 · Caption 12.

Màu: petrol `#0F4A4C`, petrol 900 `#082C2E`, gold `#B8965A`, cream `#F5F1E9`. Font: Tangerine (chữ trang trí tiếng Anh, vì không hỗ trợ dấu tiếng Việt) và Inter.

## Lưu ý

- Đây là prototype trình bày, chưa phải website chạy thật: form liên hệ, đặt phòng và đăng ký nhận tin chưa gửi dữ liệu đi đâu.
- Bài viết, ưu đãi, quyền lợi đặt trực tiếp, FAQ, tiện nghi và chính sách phòng là **nội dung mẫu**, cần khách sạn xác nhận.
- Hình ảnh và logo thuộc về Grand K Hotel Suites Hanoi.
