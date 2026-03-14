# Voz.vn Candidate Tracker

Hệ thống tracking ứng viên từ diễn đàn Voz.vn - Chuyên mục Lập trình CNTT.

## 🎯 Mục tiêu

- Lọc và phân loại ứng viên theo role: AI, Backend/DevOps, QA
- Theo dõi trạng thái và tiến trình liên hệ
- Tạo database có thể search và filter

## 📁 Cấu trúc Repo

```
voz-candidates/
├── README.md                    # File này
├── data/
│   ├── ai/                      # Ứng viên AI/ML
│   ├── backend-devops/          # Ứng viên Backend & DevOps
│   ├── qa/                      # Ứng viên QA/Tester
│   └── raw/                     # Dữ liệu thô chưa phân loại
├── logs/
│   ├── 2026-03/                 # Log theo tháng
│   └── search-queries.md        # Lịch sử tìm kiếm
├── scripts/
│   ├── add-candidate.py         # Script thêm ứng viên
│   ├── search-candidates.py     # Script tìm kiếm
│   └── export-csv.py            # Export ra CSV
├── templates/
│   └── candidate-template.md    # Template ghi thông tin
└── reports/
    └── weekly-summary.md        # Báo cáo hàng tuần
```

## 🚀 Quick Start

### Thêm ứng viên mới

```bash
python3 scripts/add-candidate.py --role ai --name "Nguyen Van A" --source "voz-thread-123"
```

### Tìm kiếm ứng viên

```bash
# Tìm theo skill
python3 scripts/search-candidates.py --skill "python"

# Tìm theo role
python3 scripts/search-candidates.py --role backend

# Tìm theo trạng thái
python3 scripts/search-candidates.py --status contacted
```

## 📊 Categories

| Role | Folder | Keywords |
|------|--------|----------|
| AI/ML | `data/ai/` | ML, Deep Learning, NLP, Computer Vision, Data Science |
| Backend/DevOps | `data/backend-devops/` | Node.js, Python, Java, Docker, K8s, CI/CD |
| QA/Tester | `data/qa/` | Manual Testing, Automation, Selenium, Playwright |

## 🏷️ Status Labels

- `new` - Mới phát hiện, chưa liên hệ
- `contacted` - Đã gửi message/liên hệ
- `responded` - Ứng viên đã phản hồi
- `interested` - Quan tâm, đang trao đổi
- `interviewing` - Đang trong quá trình interview
- `hired` - Đã hire
- `rejected` - Từ chối/Không phù hợp
- `no-response` - Không phản hồi sau 7 ngày

## 📝 Template Ứng viên

Mỗi ứng viên được lưu trong file markdown riêng:

```markdown
---
id: VAI-001
name: Nguyen Van A
role: ai
source: https://voz.vn/t/thread-title.123456/
post_date: 2026-03-14
contacted_date:
status: new
skills:
  - Python
  - TensorFlow
  - PyTorch
  - NLP
experience: "3 năm ML Engineer tại startup AI"
location: "Ho Chi Minh City"
salary_expectation: "30-40tr"
contact_info:
  telegram: @username
  email: email@example.com
notes: "Có kinh nghiệm LLM, đang tìm remote"
---

# Nguyen Van A

## Thông tin từ post

[Copy nội dung post gốc từ Voz]

## Đánh giá

- Technical: ⭐⭐⭐⭐
- Communication: ⭐⭐⭐
- Fit: ⭐⭐⭐⭐

## Timeline liên hệ

- 2026-03-14: Phát hiện post
- 
```

## 🔍 Search Tips

### Trên Voz.vn

1. Truy cập: https://voz.vn/f/lap-trinh-cntt.91/
2. Sử dụng filter theo tag hoặc search keywords
3. Các keywords thường gặp:
   - "Tuyển dụng", "Hiring", "Job", "Opportunity"
   - "Python", "Java", "JavaScript", "Golang"
   - "Remote", "Full-time", "Freelance"
   - "AI", "Machine Learning", "Data"
   - "DevOps", "SRE", "Cloud", "AWS"
   - "QA", "Tester", "Automation"

## 📈 Báo cáo

Xem file `reports/weekly-summary.md` để biết tổng quan hàng tuần.

## 🤝 Đóng góp

1. Fork repo
2. Tạo branch `feature/add-candidates`
3. Commit và push
4. Tạo PR với mô tả chi tiết

## 📞 Liên hệ

Maintainer: trieuvo-web
