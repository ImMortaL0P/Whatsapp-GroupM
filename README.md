# 📲 Automated WhatsApp Group Member Adder (CSV-Based)

A simple Node.js-based automation tool that reads phone numbers from a CSV file and directly adds them to a specified WhatsApp group using `whatsapp-web.js`. This solution is ideal for organizations, communities, or admins who need to manage WhatsApp group memberships efficiently without sending manual invites.

---

## 🚀 Features

- ✅ Reads phone numbers from a CSV file (`contacts.csv`)
- ✅ Adds participants directly to an existing WhatsApp group
- ✅ QR-based login (only once per machine)
- ✅ No Selenium or ChromeDriver required
- ✅ Lightweight dependencies and fast execution
- ✅ Easy to use via `.bat` scripts on Windows

---

## 📁 Project Structure

your-folder/
│
├── contacts.csv # Your list of phone numbers
├── index.js # Main automation script
├── dependencies.bat # Installs all required libraries
└── installer.bat # Runs installation + automation



---

## 📦 Dependencies

Installed automatically by `dependencies.bat`:

- [`whatsapp-web.js`](https://github.com/pedroslopez/whatsapp-web.js)
- `puppeteer`
- `csv-parser`
- `qrcode-terminal`

---

## 📄 CSV Format

Ensure your `contacts.csv` file is in the following format:

CSV
Name,Phone
John Doe,9876543210
Jane Smith,9812345678


Do not add country code in CSV (it's added in the script).

Format must be clean, without spaces or special characters in numbers.

🛠️ Setup Instructions (Windows)
Install Node.js (v14+ recommended) from https://nodejs.org

Place your contacts in contacts.csv

Double-click installer.bat

Scan the QR code (first time only)

The script will find your group and add all valid contacts

✏️ Modify Group Name
Open index.js and edit this line:

const groupName = 'YourGroupName';

Replace 'YourGroupName' with the exact name of your WhatsApp group.

⚠️ Important Notes
You must already be an admin of the target group.

You can only add people who:

Exist on WhatsApp

Haven’t restricted group invitations

Haven’t blocked your number

You must keep the session active (or rescan QR if deleted)

🔐 Security & Safe Practices
Uses csv-parser instead of XLSX to avoid known prototype pollution vulnerabilities

All libraries are installed at runtime using trusted sources

Session is stored locally and securely using LocalAuth

🧪 Troubleshooting
❌ "Group not found" → Check that the group name in the script exactly matches WhatsApp

❌ "Could not add participant" → Contact may not be on WhatsApp, may have privacy restrictions, or you are not an admin

If QR does not show: Delete the .wwebjs_auth folder and rerun

📌 To Do (Optional Future Enhancements)
 Create WhatsApp group programmatically

 Export logs of added/failed numbers

 GUI interface for contact upload and execution

🤝 License
MIT License. Free to use and modify.

🙌 Acknowledgements
Built using the awesome whatsapp-web.js library and the Node.js ecosystem.
