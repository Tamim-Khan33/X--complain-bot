# 📡 Twitter (X) Internet Speed Complaint Bot

This Python bot uses Selenium to:
- Test your internet speed via [Speedtest.net](https://www.speedtest.net)
- Log into [Twitter (X)](https://x.com)
- Tweet a message if your internet speed is lower than what was promised

---

## 📂 Project Structure

twitter-complaint-bot/
│
├── main.py # Main script with bot logic
├── .env # Environment variables (not shared)
├── .gitignore # Excludes sensitive files from Git
├── requirements.txt # List of Python packages
└── README.md # Documentation

yaml
Copy
Edit

---

## 🛠️ Step 1: Requirements

You’ll need:
- Python 3.7 or newer
- Google Chrome
- ChromeDriver (matching your Chrome version)
- Python packages:
  - `selenium`
  - `python-dotenv`

---

## 📥 Step 2: Installation

### 2.1. Clone the Repository

```bash
git clone https://github.com/Tamim-Khan33/twitter-complaint-bot.git
cd twitter-complaint-bot
2.2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔐 Step 3: Environment Variables
3.1. Create a .env file in your project root:
env
Copy
Edit
PROMISED_DOWN=150
PROMISED_UP=10
YOUR_EMAIL=your_email@example.com
YOUR_PASSWORD=your_secure_password
3.2. ⚠️ Important Notes:
Never share your .env file or upload it to GitHub

Your credentials are loaded securely using python-dotenv

▶️ Step 4: Running the Script
Simply run:

bash
Copy
Edit
python main.py
The bot will:

Open Chrome

Run a speed test

Log into Twitter (X)

Post a tweet with your current internet speeds

📝 Example Tweet Output
makefile
Copy
Edit
download_speed_value: 83.24 Mbps
upload_speed_value: 6.82 Mbps
🚧 Future Improvements
Tweet only when speed is below threshold

Improve login error handling

Schedule script with cron or Task Scheduler

Store logs of each tweet

⚠️ Disclaimer
This project is for educational purposes only.

Using automation on platforms like Twitter may violate their terms of service. Use responsibly and at your own risk.
