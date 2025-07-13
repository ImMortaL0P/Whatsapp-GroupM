import pandas as pd
import pywhatkit as kit
import time

# Step 1: Read numbers from Excel file
def read_numbers_from_excel(file_path):
    df = pd.read_excel(file_path)
    numbers = df['Phone'].dropna().astype(str).tolist()
    return numbers

# Step 2: Send group invite link to each number
def send_group_invites(numbers, invite_link, delay=15):
    for number in numbers:
        # Add country code if not present
        if not number.startswith('+'):
            number = '+91' + number  # Default: India
        print(f"Sending invite to: {number}")
        try:
            # Send message via WhatsApp Web
            kit.sendwhatmsg_instantly(number, f"Hey! Join our WhatsApp group using this link:\n{invite_link}", wait_time=10)
            time.sleep(delay)  # wait before sending to next
        except Exception as e:
            print(f"Failed to send to {number}: {e}")

# Main execution
if __name__ == "__main__":
    excel_file = "contacts.xlsx"  # Excel file path
    group_invite_link = "https://chat.whatsapp.com/EXAMPLEINVITELINK"  # Replace with your real link
    contacts = read_numbers_from_excel(excel_file)
    send_group_invites(contacts, group_invite_link)
