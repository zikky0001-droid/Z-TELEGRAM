# 🤖 DEV•ZIKKY Telegram Bot

> ⚠️ **WARNING: This bot is currently in TESTING PHASE**
> 
> - Features may be unstable
> - Database may be reset
> - APIs may change without notice
> - Use at your own risk

## 🚀 Quick Deployment on Render

### **Step 1: Get Bot Token**
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Copy your bot token (format: `1234567890:ABCdefGhIJKlmNoPQRsTUVwxyZ`)

### **Step 2: Deploy on Render**
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository: `zikky0001-droid/Z-TELEGRAM`
4. Configure settings:
   - **Name:** `zikky-bot` (or your choice)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
5. Add environment variable:
   - **Key:** `TOKEN`
   - **Value:** Your bot token from @BotFather
6. Click **"Create Web Service"**

## 📁 Project Structure