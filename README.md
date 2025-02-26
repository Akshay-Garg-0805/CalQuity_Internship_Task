# **CalQuity Internship Task** 🚀  

---

## **🎯 Objective**  

Welcome to the **AI Engineering Internship Task**! This project demonstrates the creation of a **financial AI agent** that:  
✅ Fetches **real-time stock prices** 📈  
✅ Plots **historical stock trends** 📊  
✅ Uses a **local LLM (Mistral-7B-Instruct)** 🤖  

---

## **⚙️ How It Works**  

- The agent listens to **user queries** and processes them intelligently.  
- It fetches stock prices using **yfinance API**.  
- It generates **trend plots** and saves them as images.  
- It runs on a **local LLM** using `llama.cpp`, ensuring full privacy and efficiency.  

### **Example Queries:**  
✅ `"What is the stock price of AAPL?"`  
✅ `"Plot stock price of TSLA from 2023-01-01 to 2023-12-31"`  

---

## **🛠️ Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Akshay-Garg-0805/CalQuity_Internship_Task.git
cd CalQuity_Internship_Task
```

---

### **2️⃣ Set Up Virtual Environment**  
Create and activate a **Python virtual environment**:  
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows (PowerShell)
```

---

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

### **4️⃣ Clone & Build `llama.cpp`**  
```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
mkdir build && cd build
cmake ..
cmake --build .
cd ../..
```
---

### **5️⃣ Download the LLM Model**  
Download the **Mistral-7B-Instruct GGUF** model:  
```bash
mkdir -p models
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q6_K.gguf -O models/mistral-7b-instruct-v0.1.Q6_K.gguf
```

---

### **6️⃣ Run the Agent**  
```bash
python main.py
```


---

## **📂 Project Files**  

📌 **`agent.py`** → Core logic of the financial agent.  
📌 **`main.py`** → CLI interaction with the agent.  
📌 **`tools/finance_tool.py`** → Fetches stock prices & generates plots.  

---

## **📊 Example Outputs**  

### **1️⃣ Stock Price Query**  
Query:  
```bash
What is the stock price of AAPL?
```
**Response:**  
```json
{
  "Open": 248.0,
  "High": 249.9799,
  "Low": 244.9100,
  "Close": 249.2799,
  "Volume": 23740521
}
```

---

### **2️⃣ Stock Trend Plot**  
Query:  
```bash
Plot stock price of AAPL from 2023-01-01 to 2023-12-31
```
**Response:**  
```bash
Plot saved to AAPL_stock_trend_2023-01-01_to_2023-12-31.png
```
**Generated Plot (Saved, Not Shown)**  

---

## **🔄 Instructions to Replicate Output**  

1️⃣ Clone the repository.  
2️⃣ Set up the virtual environment.  
3️⃣ Install the dependencies.  
4️⃣ Clone & build `llama.cpp`.  
5️⃣ Download the LLM model.  
6️⃣ Run the agent using `python main.py`.  
7️⃣ Try queries like:  
   - `"What is the stock price of AAPL?"`  
   - `"Plot stock price of AAPL from 2023-01-01 to 2023-12-31"`  

---

## **🛠️ Tools & Technologies Used**  

- 🐍 **Python** → Core programming language.  
- 📈 **yfinance** → Fetches real-time stock prices.  
- 🎨 **Matplotlib** → Generates stock trend visualizations.  
- 🔍 **Regex** → Extracts user intent from queries.  
- 🤖 **llama.cpp** → Runs the local LLM (Mistral-7B).  

---

## **👨‍💻 Author**  

- **Name**: Akshay Garg  
- **Email**: gargakshay0805@gmail.com  

---

## **📽️ Video Demo**  

🔗 [Watch Demo](https://drive.google.com/file/d/1SzlcfdtaZVp4bHDY2eJK_PYa5X6dQeKD/view?usp=sharing)  

---

## **📜 License**  

This project is licensed under the **MIT License**.  

---
