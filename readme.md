
## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Indrane/fastapi_test.git
cd fastapi_test
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start the FastAPI Server
``` bash
uvicorn app.main:app --reload
```

Now, visit **http://127.0.0.1:8000/docs** to explore the API documentation! 🎉



---

## 📚 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/` | Root endpoint |
| **POST** | `/users/register` | Register a new user |
| **POST** | `/users/login` | Login and get JWT token |
| **GET** | `/protected` | Protected route (JWT required) |
| **WS** | `/ws/chat` | Real-time chat using WebSockets |

---

## 🔗 Useful Commands
| Command | Description |
|---------|-------------|
| `uvicorn app.main:app --reload` | Start FastAPI server |


---

## 📌 Troubleshooting
### ❌ Database Connection Issues
- Ensure Neon PostgreSQL is **running and accessible**.
- Check your **`DATABASE_URL`** .
- Try connecting manually using:
  ```bash
  psql "postgresql://your_username:your_password@your_neon_host/your_database"
  ```
- If using Docker, ensure your `.env` file is properly configured.


---

## 🎯 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request 🚀

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 💬 Questions?
For any issues, reach out via GitHub Issues or email at `your-email@example.com`. 🚀

