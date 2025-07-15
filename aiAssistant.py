from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

##@tool
##def calculator(a: float, b: float) -> str:
##    """
##    Useful for performing basic arithmetic calculations using numbers
##    """
##    return f"The sum of {a} and {b} is {a+b}"
##    

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agentExecutor = create_react_agent(model, tools)

    print("Hello! I'm your AI assistant. Type 'quit' to quit.")
    print("You can ask me to perform calculations or chat with me.")
    
    while 1:
        userInput = input("\nYou: ").strip()

        if userInput == 'quit':
            break

        print("\nAssistant: ", end='')
        for c in agentExecutor.stream(
            {"messages": [HumanMessage(content=userInput)]}
            ):
            if "agent" in c and "messages" in c["agent"]:
                for m in c['agent']['messages']:
                    print(m.content, end='')
        print()

if __name__ == "__main__":
    main()
