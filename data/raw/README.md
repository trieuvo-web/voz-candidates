# Raw Data

Folder này chứa dữ liệu thô chưa được phân loại hoặc đang chờ xử lý.

## Format

Mỗi file JSON chứa thông tin từ một bài post:

```json
{
  "source_url": "https://voz.vn/t/thread-title.123456/",
  "thread_title": "Thread Title",
  "post_date": "2026-03-14",
  "author": "voz_username",
  "content": "Full post content...",
  "extracted_info": {
    "name": "",
    "role": "",
    "skills": [],
    "experience": "",
    "contact_info": {}
  },
  "status": "pending_review",
  "reviewed_by": "",
  "reviewed_at": ""
}
```

## Workflow

1. Lưu raw data vào folder này
2. Review và extract thông tin
3. Chạy script để tạo candidate file chính thức
4. Move raw file sang `processed/`
