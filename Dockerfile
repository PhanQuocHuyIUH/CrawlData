FROM python:3.11-slim
WORKDIR /app
# Cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy source code
COPY . .
# Command mặc định
CMD ["scrapy", "crawl", "mobileCrawler"]