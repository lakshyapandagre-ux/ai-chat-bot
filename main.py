import pyautogui
import time
import pyperclip
import google.genai as genai
import random

# --- Initialize Gemini Client ---
client = genai.Client(api_key="GEMINI_API_KEY")  
print("✅ Gemini Client initialized")

time.sleep(2)

pyautogui.click(1059, 1160)
time.sleep(1)

# --- Select and copy text ---
pyautogui.moveTo(1107, 166)
pyautogui.dragTo(1118, 1086, duration=1, button="left")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# --- Get copied text ---
text_data = pyperclip.paste().strip()
if not text_data:
    print("⚠ No text captured from screen.")
    exit()

print("📋 Captured text:\n", text_data)

# --- Prepare human-like prompt ---
prompt = f"""
You are chatting casually with a friend. 
Read the following message and reply naturally as a human would.
Use friendly, casual, and human-like tone. Keep it short and conversational. and talk in common hinglish language. and use humour also.b ko bhi kharidine ka sapna dekhne de. 


Message: {text_data}
"""

# --- Send text to Gemini ---
try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # ya 'gemini-2.0-large' agar creative chahiye
        contents=prompt
    )

    print("\n✅ Response received from Gemini API!")

    # --- Extract AI reply safely ---
    ai_text = ""
    if hasattr(response, "text"):
        ai_text = response.text
    elif hasattr(response, "output_text"):
        ai_text = response.output_text
    elif hasattr(response, "candidates"):
        try:
            ai_text = response.candidates[0].content.parts[0].text
        except:
            ai_text = ""
    else:
        ai_text = ""

    if ai_text:
        print("\n🤖 Gemini Reply:\n", ai_text)
    else:
        print("⚠ Gemini gave empty/filtered reply.")

except Exception as e:
    print("\n❌ Gemini API Error:", e)
    exit()

# --- Auto Reply Typing (human-like) ---
if ai_text:
    pyautogui.click(1100, 1090)  # chat input box
    time.sleep(random.uniform(0.5, 1.2))  # thinking pause

    # Type each character with human-like speed
    for char in ai_text:
        pyautogui.write(char, interval=random.uniform(0.03, 0.1))

    time.sleep(random.uniform(0.3, 0.8))  # short pause before sending
    pyautogui.press("enter")

print("\n✅ Task completed.")
