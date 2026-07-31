# 📁 Secure Cloud Document Management System on AWS

A secure, cloud-based web application that enables users to upload, manage, and access documents from anywhere using Amazon Web Services (AWS). The project emphasizes data security, scalability, and ease of use through cloud storage and user authentication.

---

## 🚀 Features

- 🔐 User Registration & Login Authentication
- ☁️ Secure File Upload to AWS S3
- 📥 Download Documents Anytime
- 🗑️ Delete Documents
- 📂 User Dashboard
- 👤 User Session Management
- 📱 Responsive User Interface
- 🔒 Secure Cloud Storage
- ⚡ Fast and Reliable File Access

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Flask

### Database
- MySQL

### Cloud Services
- Amazon S3
- AWS IAM
- Amazon EC2 (Optional Deployment)
- AWS CLI

---

## ☁️ AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon S3 | Secure document storage |
| AWS IAM | User access management |
| Amazon EC2 | Application deployment |
| AWS CLI | AWS resource management |

---

## 📂 Project Structure

```
SecureCloudDocumentSystem/
│
├── app.py
├── requirements.txt
├── .env
├── uploads/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── upload.html
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/SecureCloudDocumentSystem.git
cd SecureCloudDocumentSystem
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file.

```env
AWS_ACCESS_KEY=YOUR_ACCESS_KEY
AWS_SECRET_KEY=YOUR_SECRET_KEY
AWS_REGION=YOUR_REGION
S3_BUCKET=YOUR_BUCKET_NAME

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=documentdb

SECRET_KEY=your_secret_key
```

### 6. Run Application

```bash
python app.py
```

---

## 💻 Usage

1. Register a new account.
2. Login securely.
3. Upload documents.
4. Files are stored securely in AWS S3.
5. Download or delete documents anytime.
6. Logout securely.

---

## 🔒 Security Features

- Password Authentication
- Session Management
- AWS IAM Access Control
- Secure Cloud Storage
- Protected User Dashboard
- Environment Variables for Credentials

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Login Page
- Registration Page
- Dashboard
- Upload Page
- AWS S3 Bucket

---

## 🔄 Workflow

```
User
   │
   ▼
Login/Register
   │
   ▼
Authentication
   │
   ▼
Dashboard
   │
   ▼
Upload Document
   │
   ▼
AWS S3 Storage
   │
   ▼
Download/Delete
```

---

## 🎯 Future Enhancements

- Email Verification
- OTP Authentication
- AI-based Document Search
- OCR Support
- File Versioning
- Mobile Application
- Multi-user Collaboration
- Document Sharing with Permissions

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kunal Solanki**

B.Tech – Computer Science & Engineering (Data Science)

ABES Engineering College, Ghaziabad
![Uploading Screenshot 2026-07-15 222626.png…]()
<img width="935" height="485" alt="Screenshot 2026-07-15 222640" src="https://github.com/user-attachments/assets/2919d7e7-a939-4d64-9634-de7033af16c4" />
<img width="101" height="33" alt="Screenshot 2026-07-15 222648" src="https://github.com/user-attachments/assets/c46ee23c-ee8f-4089-8019-7d06a58852f8" />

<img width="935" height="364" alt="Screenshot 2026-07-15 222659" src="https://github.com/user-attachments/assets/b5266585-706b-47ce-a6e3-653a5e5c2404" />
<img width="428" height="80" alt="Screenshot 2026-07-15 222729" src="https://github.com/user-attachments/assets/efbad465-04bd-40b0-b194-f1d0d4e56cad" />
<img width="428" height="80" alt="Screenshot 2026-07-15 222729" src="https://github.com/user-attachments/assets/c25d2c5b-a174-4fc2-8030-db97779e0829" />









---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

