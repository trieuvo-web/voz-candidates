# Hướng dẫn sử dụng Voz Candidate Tracker

## ✅ Repo đã tạo

**GitHub Repo**: https://github.com/trieuvo-web/voz-candidates

## 🚧 Hạn chế

Voz.vn có Cloudflare protection nên **không thể crawl tự động**. Bạn cần:
1. Truy cập thủ công https://voz.vn/f/lap-trinh-cntt.91/
2. Copy thông tin từ các post tuyển dụng/tìm việc
3. Dùng script để thêm vào database

## 🚀 Quick Start

### 1. Clone repo
```bash
git clone https://github.com/trieuvo-web/voz-candidates.git
cd voz-candidates
```

### 2. Thêm ứng viên mới
```bash
# AI/ML candidate
python3 scripts/add-candidate.py \
  --role ai \
  --name "Nguyen Van A" \
  --source "https://voz.vn/t/thread-title.123456/"

# Backend/DevOps candidate  
python3 scripts/add-candidate.py \
  --role backend-devops \
  --name "Tran Van B" \
  --source "https://voz.vn/t/another-thread.789/"

# QA candidate
python3 scripts/add-candidate.py \
  --role qa \
  --name "Le Thi C" \
  --source "https://voz.vn/t/qa-thread.456/"
```

### 3. Tìm kiếm ứng viên
```bash
# Theo skill
python3 scripts/search-candidates.py --skill python

# Theo role
python3 scripts/search-candidates.py --role ai

# Theo trạng thái
python3 scripts/search-candidates.py --status new

# Xem tất cả
python3 scripts/search-candidates.py --all
```

### 4. Export ra CSV
```bash
python3 scripts/export-csv.py --output candidates_2026-03-14.csv
```

## 📁 Cấu trúc

```
voz-candidates/
├── data/
│   ├── ai/              # Ứng viên AI/ML
│   ├── backend-devops/  # Ứng viên Backend & DevOps
│   ├── qa/              # Ứng viên QA/Tester
│   └── raw/             # Dữ liệu thô
├── scripts/
│   ├── add-candidate.py     # Thêm ứng viên
│   ├── search-candidates.py # Tìm kiếm
│   └── export-csv.py        # Export CSV
├── templates/
│   └── candidate-template.md  # Template
├── reports/
│   └── weekly-summary.md      # Báo cáo
└── logs/
    └── search-queries.md      # Lịch sử tìm kiếm
```

## 🏷️ Status

- `new` - Mới phát hiện
- `contacted` - Đã liên hệ
- `responded` - Đã phản hồi
- `interested` - Quan tâm
- `interviewing` - Đang interview
- `hired` - Đã hire
- `rejected` - Từ chối

## 🔍 Keywords tìm kiếm trên Voz

### AI/ML
- Machine Learning, Data Science
- Deep Learning, NLP, Computer Vision
- Python, TensorFlow, PyTorch

### Backend/DevOps
- Backend Developer, API, Microservices
- Node.js, Python, Java, Go
- Docker, Kubernetes, AWS, DevOps

### QA
- QA Engineer, Tester
- Automation Testing, Selenium
- Manual Testing

## 📝 Workflow đề xuất

1. **Daily**: Browse Voz.vn CNTT forum 15-30 phút
2. **Phát hiện post**: Copy link và nội dung chính
3. **Phân loại**: Xác định role (AI/BE/QA)
4. **Thêm vào DB**: Chạy `add-candidate.py`
5. **Cập nhật chi tiết**: Mở file md và điền thông tin
6. **Liên hệ**: PM trên Voz hoặc contact info có sẵn
7. **Update status**: Cập nhật sau khi liên hệ

## 📊 Tracking

Mỗi ứng viên có file riêng với metadata:
- ID, Name, Role
- Skills, Experience, Location
- Salary expectation
- Contact info
- Status + timeline

Xem file `templates/candidate-template.md` để biết format đầy đủ.

## 💡 Tip

Nên bookmark các thread quan trọng và check định kỳ vì Voz không có notification tốt.
