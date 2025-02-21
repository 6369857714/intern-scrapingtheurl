# Build Stage
FROM node:18-slim as build-stage
WORKDIR /app

# Skip Chromium download
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

# Copy package files and install dependencies
COPY package*.json ./
RUN apt-get update && apt-get install -y \
    chromium \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libnss3 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libexpat1 \
    libxshmfence1 \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libnspr4 \
    lsb-release \
    xdg-utils \
    wget \
    && ln -s /usr/bin/chromium /usr/bin/chromium-browser \
    && npm install

# Set Puppeteer executable path
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

# Accept build argument for SCRAPE_URL and set it as an environment variable
ARG SCRAPE_URL
ENV SCRAPE_URL=${SCRAPE_URL}

# Copy the rest of the application code
COPY scrape.js ./
RUN node scrape.js

# Verify file creation
RUN ls -l /app

# Hosting Stage
FROM python:3.10-slim as host-stage
WORKDIR /app

# Copy the scraped data and server file
COPY --from=build-stage /app/scraped_data.json /app/scraped_data.json
COPY server.py ./

# Install Flask and Pillow
RUN pip install Flask Pillow

# Expose the Flask server port
EXPOSE 5000

# Run the Flask server
CMD ["python", "server.py"]


