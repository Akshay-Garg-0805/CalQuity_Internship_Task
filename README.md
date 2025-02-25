# CalQuity Internship Task

## 🚀 Objective

Welcome to the **AI Engineering Internship Task**! This project demonstrates the creation of a basic AI agent that interacts with the **yfinance API** to fetch real-time stock prices and visualize stock trends. The agent was built using Python, and the goal was to showcase the agent's ability to execute predefined tasks with a custom tool.

## ⚙️ How It Works

The agent can perform two key functionalities:
1. **Fetch Stock Price**: Query the current stock price of a given stock symbol.
2. **Plot Stock Trend**: Fetch and plot the stock price trend over a specific date range.

### Example Use Cases
- **What is the stock price of AAPL?**
- **Plot stock price of AAPL from 2023-01-01 to 2023-12-31**

---

## 🔧 Installation & Setup

To replicate the output of this project, follow the steps below:

### **1. Clone the Repository**
First, clone this repository to your local machine:
```bash
git clone https://github.com/Akshay-Garg-0805/CalQuity_Internship_Task.git
cd CalQuity_Internship_Task
```

---

### **2. Set Up Virtual Environment**
Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows (if using PowerShell)
```

---

### **3. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

### **4. Clone and Build `llama.cpp`**
Clone and build `llama.cpp` for running the local LLM:
```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
mkdir build && cd build
cmake ..
cmake --build .
cd ../..
```

---

### **5. Download the LLM Model**
Download the **Mistral-7B-Instruct GGUF** model file:
```bash
mkdir -p models
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q6_K.gguf -O models/mistral-7b-instruct-v0.1.Q6_K.gguf
```

---

### **6. Run the Agent**
Run the agent using:
```bash
python main.py
```

---

## 📂 Project Files

### `agent.py`
Contains the core logic for the financial agent.

### `main.py`
The main script to interact with the agent through the command line.

### `tools/finance_tool.py`
Contains the code to fetch stock data and generate plots using the yfinance API.

---

## 🖼️ Example Outputs

### **1. Stock Price Query**
When you ask for a stock price like:
```bash
What is the stock price of AAPL?
```
The agent will respond with the latest stock price, like so:

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

### **2. Stock Trend Plot**
When you ask to plot the stock trend for a date range:
```bash
Plot stock price of AAPL from 2023-01-01 to 2023-12-31
```
The agent will fetch historical data and **save the plot** to a file.

---

## 📋 Instructions to Replicate the Output

### 1. Clone the repository as mentioned above.
### 2. Set up the virtual environment.
### 3. Install the dependencies.
### 4. Clone and build `llama.cpp`.
### 5. Download the LLM model.
### 6. Run the financial agent:
```bash
python main.py
```
### 7. Try these queries to see the agent in action:
- `"What is the stock price of AAPL?"`
- `"Plot stock price of AAPL from 2023-01-01 to 2023-12-31"`

---

## 🛠️ Tools & Technologies

- **Python**: The core language for implementing the agent.
- **yfinance**: To fetch stock prices and historical data.
- **Matplotlib**: To visualize stock trends.
- **Regex**: For extracting the user's query and executing relevant actions.
- **llama.cpp**: Running the local LLM for agent responses.

---

## 🧑‍💻 Author

- **Name**: Akshay Garg
- **Email**: gargakshay0805@gmail.com

---

## 🎥 Video Demo

Watch the demo of the project in action:

[🔗 Link to Demo Video](#)

---
