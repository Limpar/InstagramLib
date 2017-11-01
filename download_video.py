import os
import time
import threading

from urllib import request

import instagram


def download_video(url, new_name):
    """
    downloads single file by url as new_name
    :param url: global link as atr
    :param new_name: global name as str
    :return: None
    """
    try:
        request.urlretrieve(url, new_name)
        result = "success"
    except:
        result = "fail"
    finally:
        print(f"{time.ctime()}: {url} - {result}\n")


def download_video_files(urls, instgram_account):
    """
    simple download files in ~/Downlads/profile_folder
    saves log file ~/Downlaods/insta_downloader_log_file.txt
    with urls on videos and result of downloading
    sometimes there is a 404error happen unexpectedly, if so,
    it will be possible to download it manually.
    :param urls: str list
    :return: nothing
    """
    user_downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    account_folder = os.path.join(user_downloads_folder, instgram_account)
    os.mkdir(account_folder)

    threads = []

    for numb, link in enumerate(urls):
        file_name = os.path.join(account_folder, f"{account}_{numb}.mp4")
        thread = threading.Thread(target=download_video, args=(link, file_name))
        # download_video(link, os.path.join(account_folder, f"{account}_{numb}.mp4"))
        threads.append(thread)
        thread.start()

    [thread.join() for thread in threads]


if __name__ == "__main__":

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    new_file_name = os.path.join(downloads_folder, NEEDED_ACCOUNT + "_video_urls.txt")

    agent = instagram.AgentAccount(TEST_LOGIN, TEST_PASSWORD)

    account = instagram.Account(NEEDED_ACCOUNT)
    agent.update(account)

    media = agent.getMedia(account, count=account.media_count)

    total_amount = account.media_count

    videos = []
    for m in media:
        agent.update(m)
        if m.is_video:
            videos.append(m.video_url)

    download_video_files(videos, NEEDED_ACCOUNT)
