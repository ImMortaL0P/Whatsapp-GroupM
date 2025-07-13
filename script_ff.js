const fs = require('fs');
const csv = require('csv-parser');
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const contacts = [];

// Load contacts from CSV
fs.createReadStream('contacts.csv')
  .pipe(csv())
  .on('data', (row) => {
    if (row.Phone) {
      // Clean and push number
      const cleanNumber = row.Phone.replace(/\D/g, '');
      contacts.push(cleanNumber);
    }
  })
  .on('end', () => {
    console.log('✅ Contacts loaded:', contacts);
    startWhatsApp();
  });

// WhatsApp logic
function startWhatsApp() {
  const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
      headless: false,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    },
  });

  client.on('qr', (qr) => {
    console.log('📷 Scan this QR code to log in:');
    qrcode.generate(qr, { small: true });
  });

  client.on('ready', async () => {
    console.log('✅ WhatsApp client is ready');

    const groupName = 'Trial'; // Change this to your group

    // Search group
    const chats = await client.getChats();
    const group = chats.find((chat) => chat.name === groupName && chat.isGroup);

    if (!group) {
      console.log('❌ Group not found.');
      return;
    }

    // Try adding each participant
    for (const number of contacts) {
      const waId = `91${number}@c.us`; // Use your country code
      try {
        await group.addParticipants([waId]);
        console.log(`➕ Added ${number}`);
      } catch (err) {
        console.log(`⚠️ Could not add ${number}: ${err.message}`);
      }
    }

    console.log('🎉 Done adding all participants.');
  });

  client.initialize();
}
