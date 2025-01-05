import os
import asyncio
import aiohttp  # pip install aiohttp
import aiofile  # pip install aiofile
import tqdm

REPORTS_FOLDER = "reports"
FILES_PATH = os.path.join(REPORTS_FOLDER, "files")
SIZE_1_KB = 1024 # 1kb = 1024b
SIZE_1_MB = 1024**2 # 1mb = 1024kb
SIZE_1_GB = 1024**3 # 1bg = 1024mb


def download_files_from_report(urls):
    os.makedirs(FILES_PATH, exist_ok=True)
    sema = asyncio.BoundedSemaphore(5)

    async def fetch_file(session, url):
        fname = url.split("/")[-1]
        async with sema:
            async with session.get(url) as resp:
                assert resp.status == 200
                file_size = resp.content_length  # bayt
                print(f"request: {fname}","content-length: ",file_size)
                
                resp2 = resp.content
                async with aiofile.async_open(
                    os.path.join(FILES_PATH, fname), "wb"
                ) as outfile:
                    outfile.write(resp2)
                print(f'saved: {fname}')

    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_file(session, url) for url in urls]
            await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


urls = ["https://www.w3schools.com/html/mov_bbb.mp4",
        "https://i.pinimg.com/originals/15/f6/a3/15f6a3aac562ee0fadbbad3d4cdf47bc.jpg",
        "https://files.uzmovi.club/film9/mrrobot/2-9qism.mp4",
        "https://wallpapers.com/images/featured/nature-4k-background-hdapuxny79ad3rev.jpg",
        "https://i.pinimg.com/originals/eb/49/e5/eb49e5a5ab67740df2b5bed8ddb153de.jpg",
        "https://fayllar1.ru/20/kinolar/65%20my5tv%20480p%20O%27zbek%20tilida%20(asilmedia.net).mp4",

        ]
url = ["https://fayllar1.ru/20/kinolar/65%20my5tv%20480p%20O%27zbek%20tilida%20(asilmedia.net).mp4",]
download_files_from_report(url)
