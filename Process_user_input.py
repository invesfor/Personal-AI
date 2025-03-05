import Time
import Weather

Search_information_weather = Weather.Search_information_weather
Get_current_time = Time.Get_current_time

def process_user_input():
    user_input = input("You: ")
    # messages.append({"role": "user", "content": user_input})
    if "thời tiết" in user_input.lower(): 
        return f"\nThông tin thời tiết: {Search_information_weather}"
    elif "thời gian" in user_input.lower(): 
        return f"\nThời gian hiện tại: {Get_current_time}"
    else:
        return user_input
