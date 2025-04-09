import feedparser

feed = feedparser.parse("https://news.google.com/rss/search?q=India&hl=en-IN&gl=IN&ceid=IN:en")

for entry in feed.entries[:5]:
    print()
    print("\nTitle :", entry.title)
    print()
    print("Link  :", entry.link)
    print()
    print("Summary :", entry.summary)