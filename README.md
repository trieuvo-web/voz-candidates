# Voz.vn Candidate Tracker

Hệ thống tracking ứng viên từ diễn đàn Voz.vn - Chuyên mục Lập trình CNTT.

## 🎯 Mục tiêu

Tìm kiếm và tracking ứng viên cho **Startup Việt Nam**:
- 💰 Salary: 30-50 triệu VND/tháng
- 👨‍💻 Prefer: Trẻ (22-30 tuổi), adaptable
- 🎓 Accept: Fresher có trình độ cao, self-taught
- 📍 Location: Hybrid/Remote (HCMC/Hanoi)
- 🚀 Environment: Startup (tốc độ cao, flexible)

---

## 📊 Current Status

| Category | New | Contacted | Responded | Total |
|----------|-----|-----------|-----------|-------|
| **AI/ML** | 2 | 0 | 0 | 2 |
| **Backend/DevOps** | 5 | 0 | 0 | 5 |
| **QA** | 0 | 0 | 0 | 0 |
| **Total** | **7** | **0** | **0** | **7** |

### Top Matches cho JD (30-50M, Startup VN):

| Priority | Candidate | Role | Match Score | Salary Fit |
|----------|-----------|------|-------------|------------|
| **P1** | PhuThoDien | AI Educator | ⭐⭐⭐⭐⭐ | ✅ 35-45M |
| **P1** | odkjabqpmzvmz | DevOps/Observability | ⭐⭐⭐⭐⭐ | ✅ 30-35M |
| **P2** | vozer9 | AI Engineer | ⭐⭐⭐⭐ | ✅ 35-45M |
| **P2** | s29311 | Backend Engineer | ⭐⭐⭐⭐ | ✅ 35-45M |
| **P2** | nkciam | DevOps/Referral | ⭐⭐⭐⭐ | ✅ 40-50M |
| **P3** | baodang359 | Backend (Junior) | ⭐⭐⭐ | ⚠️ 25-35M |
| **Special** | lechuck | Senior Backend | ⭐⭐⭐⭐⭐ | ❌ Overqualified |

---

## 📁 Repository Structure

```
voz-candidates/
├── README.md                          # File này
├── JOB_DESCRIPTIONS.md                # JD cho các vị trí
├── CANDIDATE_JD_MATCHING.md           # Phân tích match với JD
├── GUIDELINES.md                      # Hướng dẫn đánh giá
├── TRACKING_CHECKLIST.md              # Checklist theo dõi
├── VOZ_THREADS_SUMMARY.md             # Tổng hợp threads
├── data/
│   ├── ai/                            # Ứng viên AI/ML
│   ├── backend-devops/                # Backend & DevOps
│   ├── qa/                            # QA/Tester
│   └── raw/                           # Dữ liệu thô
├── scripts/
│   ├── add-candidate.py               # Thêm ứng viên
│   ├── search-candidates.py           # Tìm kiếm
│   ├── export-csv.py                  # Export CSV
│   └── monitor_thread.py              # Scan thread
├── templates/
│   └── candidate-template.md          # Template
└── reports/
    └── weekly-summary.md              # Báo cáo
```

---

## 🚀 Quick Start

### 1. Xem JD và Matching Analysis

```bash
# Xem JD cho các vị trí
cat JOB_DESCRIPTIONS.md

# Xem phân tích matching với candidates
cat CANDIDATE_JD_MATCHING.md

# Xem checklist hành động
cat TRACKING_CHECKLIST.md
```

### 2. Tìm kiếm candidates

```bash
# Theo role
python3 scripts/search-candidates.py --role ai

# Theo skill
python3 scripts/search-candidates.py --skill kubernetes

# Theo status
python3 scripts/search-candidates.py --status new

# Xem tất cả
python3 scripts/search-candidates.py --all
```

### 3. Export danh sách

```bash
python3 scripts/export-csv.py --output candidates.csv
```

### 4. Monitor thread mới

```bash
python3 scripts/monitor_thread.py \
  --url "https://voz.vn/t/THREAD_URL" \
  --name "Thread Name" \
  --deep-scan
```

---

## 🎯 Chiến lược Contact (Theo JD Matching)

### Week 1 - Contact Priority 1 (High Match):

**PhuThoDien (VAI-001) - AI Technical Educator:**
- **JD Match:** AI Educator/Content Creator
- **Offer:** 35-45M + equity
- **Why:** Proven content creator (66K views), unique skillset
- **Contact:** PM trên Voz, nhấn mạnh opportunity xây dựng AI education program

**odkjabqpmzvmz (VBD-003) - DevOps/Observability Engineer:**
- **JD Match:** DevOps/Observability
- **Offer:** 30-35M + learning budget
- **Why:** Fresher nhưng có modern stack (OTel, Jaeger), production experience
- **Contact:** PM về opportunity với modern observability stack

### Week 1 - Contact Priority 2 (Good Match):

**vozer9 (VAI-002) - AI Engineer:**
- **JD Match:** AI Engineer
- **Offer:** 35-45M
- **Why:** Có sản phẩm riêng (9Router), product mindset

**nkciam (VBD-001) - DevOps Community Leader:**
- **JD Match:** Network/Referral
- **Action:** Xin referral network, không hire trực tiếp
- **Offer:** Referral bonus

### Week 2 - Research trước khi contact:

**s29311 (VBD-005) - Backend Engineer:**
- **JD Match:** Backend (Mid-level)
- **Action:** Research profile trước

**baodang359 (VBD-004) - Backend (Junior):**
- **JD Match:** Backend (Junior)
- **Action:** Contact nếu cần fresher role

### Special Case:

**lechuck (VBD-002) - Senior Backend:**
- **Status:** Overqualified cho 30-50M range
- **Action:** Contact chỉ nếu có senior role + equity (CTO/VP Eng)
- **Note:** 10+ YOE, đã làm US, interview Amazon/Microsoft

---

## 📋 JD Chi tiết

Xem file `JOB_DESCRIPTIONS.md` cho chi tiết:

1. **Backend Engineer (Python/Node.js)** - 30-50M
2. **DevOps/Platform Engineer** - 30-50M
3. **AI/ML Engineer** - 30-50M
4. **AI Technical Educator** - 30-50M
5. **Observability/SRE Engineer** - 30-50M

---

## 🔍 Keywords đã dùng để tìm threads

- tuyển, hiring, job, tìm việc, freelance, remote
- opportunity, ai, ml, backend, devops, qa, tester
- engineer, developer, lập trình, kỹ sư

---

## 📝 Best Practices

Xem `GUIDELINES.md` cho:
- 5-phase assessment framework
- Green/Red flags checklist
- Role matching matrix
- Contact templates
- Timeline tracking

---

## 📈 Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Candidates discovered | 5-10/week | 7 |
| JD Match Score >4⭐ | >50% | 5/7 (71%) |
| Contact rate | >70% | 0% (starting) |
| Response rate | >30% | - |

---

## 🔗 Links

- **GitHub Repo:** https://github.com/trieuvo-web/voz-candidates
- **Voz CNTT Forum:** https://voz.vn/f/lap-trinh-cntt.91/

---

## 🎯 Next Actions

**Ngay lập tức:**
1. Review JD và Matching Analysis
2. Contact PhuThoDien và odkjabqpmzvmz (P1)
3. Prepare offer packages

**This Week:**
4. Contact vozer9 và nkciam (P2)
5. Setup thread monitoring schedule
6. Scan more thread pages for additional candidates

**Ongoing:**
7. Weekly monitoring của active threads
8. Update candidate statuses
9. Generate progress reports
