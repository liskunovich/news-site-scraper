# <b>What is this?</b>
This is my first experience with AsyncIO, AIOHTTP and ABC libraries in python. <br>
Those scrapers made for my project in "Google Solution Challenge 2023" - Garbage Collector.

<h1><b> How to use it? </b></h1>

●The first thing is you need to clone the repository to your device. <br>
<pre><code>git clone https://github.com/liskunovich/news-site-scraper.git</code></pre>
●Then install all requirements that written in the "requirements.txt" <br>
<pre><code>pip install -r requirements.txt</code></pre>


In the lines below you can see example of usage for the existing scraper - "baigenews.py" <br>
<pre><code>def scrap_baigenews() -> List[dict]:
    instance = Baigenews(
      base_url='https://baigenews.kz',
      news_url='https://baigenews.kz/teg/ekologiya/'
    )
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(instance.get_posts())
    return data</code></pre>
