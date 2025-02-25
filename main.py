from agent import financial_agent

def main():
    print("💡 Financial Agent is running... Type 'exit' to quit.\n")
    print("💹 For getting the current day stock price, Enter 'What is the stock price of (Stock symbol)\n")
    print("📊 For getting the plot of historical trends, Enter 'Plot stock price of (Stock symbol) from (Start date) to (End date), Where date is in 'YYYY-MM-DD'.\n")
    while True:
        user_input = input("📝 Ask me something: ")
        if user_input.lower() == "exit":
            break
        response = financial_agent(user_input)
        print(f"🤖 Agent: {response}")

if __name__ == "__main__":
    main()
