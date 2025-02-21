const fs = require('fs');
const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.goto(process.env.SCRAPE_URL);

    // Capture a screenshot as an image
    const imageBuffer = await page.screenshot();

    // Encode the image data in base64 format
    const imageData = imageBuffer.toString('base64');

    // Save the image data in JSON format
    const data = { image: imageData };
    fs.writeFileSync('scraped_data.json', JSON.stringify(data));

    await browser.close();
})();





















