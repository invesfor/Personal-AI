from openai import OpenAI
import Process_user_input

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)
messages = []

# PERSONAL_ASSISTANT_PROMPT = """Bạn là một trợ lý ảo cá nhân thông minh.
# Luôn luôn trả lời ngắn gọn, đầy đủ thông tin, dễ hiểu, đi đúng trọng tâm câu hỏi.
# Khi được hỏi về các vấn đề về thời tiết, ... bằng các dữ liệu mà tôi cung cấp, 
# không được trả lời kiểu như thông tin thời tiết hiện tại ko được cung cấp, hay ko thể truy cập vào thông tin thời tiết.
# Hãy trả lời bằng kết quả được tìm kiếm nhiều nhất, bao gồm: nhiệt độ tối đa và tối thiểu trong ngày; thời gian mưa(nếu có) và không cần phải trả lời thêm bất cứ điều gì nữa.

# Luôn luôn trả lời bằng tiếng việt.
# """
# messages = [{"role": "system","content": PERSONAL_ASSISTANT_PROMPT}]
while True:
    user_input = Process_user_input.process_user_input()
    
    messages.append({"role": "user", "content": user_input})

    if user_input == "Exit":
        break

    try:
        response = client.chat.completions.create(
            model="gemma2:9b",
            stream=True,
            messages=messages
        )
        bot_reply = ""
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            bot_reply += content
            print(content, end="", flush=True)
        print()  # New line after response

        messages.append({"role": "assistant", "content": bot_reply})

    except KeyboardInterrupt:
        print("\nĐã dừng câu trả lời!")
        continue