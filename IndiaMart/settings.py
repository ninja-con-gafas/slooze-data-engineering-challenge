BOT_NAME = "IndiaMart"

SPIDER_MODULES = ["IndiaMart.spiders"]
NEWSPIDER_MODULE = "IndiaMart.spiders"

# Disable obeying robots.txt rules
ROBOTSTXT_OBEY = False

# Set a fixed delay between requests to prevent overloading servers
DOWNLOAD_DELAY = 2.0

# Enable AutoThrottle to manage crawl rate dynamically
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1.0
AUTOTHROTTLE_MAX_DELAY = 5.0

# Export feed encoding
FEED_EXPORT_ENCODING = "utf-8"

# Default headers for all requests
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com"
}

# Use updated request fingerprinting and async reactor
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
