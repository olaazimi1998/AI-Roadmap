from langchain_core.messages import HumanMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_API_KEY
from tools import calculator


def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0,
    )

    model_with_tools = model.bind_tools([calculator])

    messages = [HumanMessage(content="7 * 6 چند می‌شود؟")]

    response = model_with_tools.invoke(messages)
    messages.append(response)

    for tool_call in response.tool_calls:
        result = calculator.invoke(tool_call["args"])
        messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"],
            )
        )

    final_response = model_with_tools.invoke(messages)
    print(final_response.content)


if __name__ == "__main__":
    main()