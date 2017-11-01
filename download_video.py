import os
import time

from urllib import request

import instagram


def download_single_file(url, new_name):
    """
    downloads single file by url as new_name
    :param url: global link as atr
    :param new_name: global name as str
    :return: fail or success as str
    """
    try:
        request.urlretrieve(url, new_name)
        result = "success"
    except:
        result = "fail"
    finally:
        return result




def download_video_files(urls, account):
    """
    simple download files in ~/Downlads/profile_folder
    saves log file ~/Downlaods/insta_downloader_log_file.txt
    with urls on videos and result of downloading
    sometimes there is a 404error happen unexpectedly, if so,
    it will be possible to download it manually.
    :param urls: str list
    :return: nothing
    """
    folder = os.path.join(os.path.expanduser("~"), "Downloads")
    acc_folder = os.path.join(folder, account)
    os.mkdir(acc_folder)

    log_file = os.path.join(folder, "insta_downloader_log_file.txt")

    with open(log_file, "a") as fp:
        for numb, link in enumerate(urls):
            file_name = os.path.join(acc_folder, f"{account}_{numb}.mp4")
            result = download_single_file(link, file_name)
            fp.write(f"{time.ctime()}: {link} - {result}\n")


if __name__ == "__main__":

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    new_file_name = os.path.join(downloads_folder, NEEDED_ACCOUNT + "_video_urls.txt")

    agent = instagram.AgentAccount(TEST_LOGIN, TEST_PASSWORD)

    account = instagram.Account(NEEDED_ACCOUNT)
    agent.update(account)

    media = agent.getMedia(account, count=account.media_count)

    total_amount = account.media_count
    videos = []
    v_count = 0
    for m in media:
        agent.update(m)
        total_amount -= 1
        if m.is_video:
            print("*", end="")
            v_count += 1
            videos.append(m.video_url)
    print("\n", v_count)

    download_video_files(videos, NEEDED_ACCOUNT)
