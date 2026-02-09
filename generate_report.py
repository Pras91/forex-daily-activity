import os
import feedparser
from datetime import datetime

def get_news(query):
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    return "\n".join([f"- [{e.title}]({e.link})" for e in feed.entries[:3]])

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = f"# 📈 Forex Daily: {timestamp}\n\n"
report += f"## Gold (XAU/USD)\n{get_news('XAUUSD Gold')}\n\n"
report += f"## Yen (USD/JPY)\n{get_news('USDJPY Yen')}\n"

folder = "Daily Report for Forex"
if not os.path.exists(folder): os.makedirs(folder)
with open(f"{folder}/report_{datetime.now().strftime('%Y-%m-%d')}.md", "w") as f:
    f.write(report)
