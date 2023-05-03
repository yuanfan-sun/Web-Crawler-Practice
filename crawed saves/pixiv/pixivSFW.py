import requests
from lxml import etree
import re
import os

if __name__ == '__main__':
    if not os.path.exists('./pixiv/pixiv_hot_SFW'):
        os.makedirs('./pixiv/pixiv_hot_SFW')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'cookie': 'first_visit_datetime_pc=2021-03-15+03:19:21; p_ab_id=2; p_ab_id_2=1; p_ab_d_id=157666725; yuid_b=NgkVKFQ; c_type=23; a_type=0; b_type=1; ki_s=214027:0.0.0.0.2; _ga=GA1.2.2052610937.1615745991; ki_t=1615745980509;1615745980509;1615752052547;1;3; ki_r=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8=; __cfduid=d11281556f21599fd1c78d6b981c6e2201618398776; _gid=GA1.2.63259721.1618398951; login_ever=yes; __cf_bm=51b97f9b2e2e03ec505ff321bb4c18d48144fd8e-1618434298-1800-Ac9aZLFLHV1C9M6FvurpCwZlrHU43zdcw9xoELCXZY7/DdNgHnpEoJFy0vo4uTLIItRV+pEb/r6HFsx83U5Ad32D5EhQ4sp6CjuhAkNEtHAOBx1Ct2r1WZhRhBP/yMwJ3mHNFwiaKSupM6vBSuYLs/4hyXIRCC5yOBQhoOhqu+loIiEuP7avNyUTx1drzNDAMw==; tag_view_ranking=EZQqoW9r8g~0xsDLqCEW6~eFs6si-q7J~faHcYIP1U0~2R7RYffVfj~Lt-oEicbBr~d2FncN8CBI~yqPUQRcWeb~qWFESUmfEs~iFcW6hPGPU~Hjx7wJwsUT~WcIcGAgRIK~B_OtVkMSZT~MM6RXH_rlN~5oPIfUbtd6~KN7uxuR89w~nf2nMUUZFU~1n-RsNEFpK~RTJMXD26Ak~gpglyfLkWs~CiSfl_AE0h~28gdfFXlY7~eVxus64GZU~VMjn4VzDLQ~tgP8r-gOe_~-98s6o2-Rp~azESOjmQSV~JBFbzljAuI~13HpD_lYAn~EGefOqA6KB~K8esoIs2eW~_RfiUqtsxe~qadCPKe0Fl~2kpvX0L5nu~ADMBPKfY5n~RybylJRnhJ~CAH-OfIs-U~9zcPibj6VK~EWJG2DcRyX~8cMNTf_lvu~P5-w_IbJrm~JM7vfxKDmx~udkRh_mjvd~kxn0BdkcW5~QcneKFYI8h~PlA_M1Z8tl~CztRgmi8vs~OJ3Bxo1Xfn~-_xRkJ5N3r~MmXTpQaDvv~Kv3rJH_PbC~C9iRb0VTwK~TcgCqYbydo~rIC2oNFqzh~GACl-vLazK~CrFcrMFJzz~HFX-xbTwCV~WlKkwEuUi0~KC--pudNUr~TWrozby2UO~jk9IzfjZ6n~HY55MqmzzQ~LJo91uBPz4~UIfHbi0qTk~wmxKAirQ_H~Ie2c51_4Sp~BU9SQkS-zU~R8LJXFI4V3~E8plmQ7kUK~Js5EBY4gOW~Hh52hrn0oF~hEuKWOJ6dp~nW7EMOuPvx~ZmBaQpwChs~F4f0UIjqZv~w8ffkPoJ_S~T8AkHNylGZ~t6fkfIQnjP~s3i_irjAJg~lOoByuwkMh~e6DJejypJg~Et8qKXA3LZ~eVBXl1t9y6~VEWLVR2U9i~Acf27EJzsC~QzKFCsGzn-~_kLUzfSDqN~7H3YOcbzOl~iacT4zaFWi~Aw_dznQmg1~_RZumrVuci~mLrrjwTHBm~kym2Z4vnZu~nQRrj5c6w_~j547Ftwyuu~n7YxiukgPF~KOnmT1ndWG~xJsg2eui8K~BtXd1-LPRH~jS8TGx1n0i; _gat=1; PHPSESSID=25103980_gsoQ2p3yPHpD7p9q6MHQwrEw5c7w1ix0; device_token=a1b1976b5f8f694cf172544cb0c82834; privacy_policy_agreement=2'
    }

    detail_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'referer': 'https://www.pixiv.net/ranking.php?mode=daily'
    }

    hot_url = 'https://www.pixiv.net/ranking.php?mode=daily'
    response = requests.get(url=hot_url, headers=headers)

    tree = etree.HTML(response.text)
    li_list = tree.xpath('//*[@id="wrapper"]/div[1]/div/div[3]/div[1]/section')
    for li in li_list:
        title = li.xpath('./@data-title')[0]
        detail_page = 'https://www.pixiv.net' + li.xpath('./div[2]/a/@href')[0]
        detail_response = requests.get(url=detail_page, headers=detail_headers)

        detail_tree = etree.HTML(detail_response.text)
        ex = ',"regular":"(.*?)","original":"'
        img_src_list = re.findall(ex, detail_response.text, re.S)
        for img in img_src_list:
            img_name = img.split('/')[-1]
            imgPath = './pixiv/pixiv_hot_SFW/' + img_name
            img_data = requests.get(url=img, headers=detail_headers).content
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
        fp.close()

# class pixiv:
#     def __init__(self):
#         self.default_headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
#             'cookie': 'first_visit_datetime_pc=2021-03-15+03:19:21; p_ab_id=2; p_ab_id_2=1; p_ab_d_id=157666725; yuid_b=NgkVKFQ; c_type=23; a_type=0; b_type=1; ki_s=214027:0.0.0.0.2; _ga=GA1.2.2052610937.1615745991; ki_t=1615745980509;1615745980509;1615752052547;1;3; ki_r=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8=; __cfduid=d11281556f21599fd1c78d6b981c6e2201618398776; _gid=GA1.2.63259721.1618398951; login_ever=yes; __cf_bm=51b97f9b2e2e03ec505ff321bb4c18d48144fd8e-1618434298-1800-Ac9aZLFLHV1C9M6FvurpCwZlrHU43zdcw9xoELCXZY7/DdNgHnpEoJFy0vo4uTLIItRV+pEb/r6HFsx83U5Ad32D5EhQ4sp6CjuhAkNEtHAOBx1Ct2r1WZhRhBP/yMwJ3mHNFwiaKSupM6vBSuYLs/4hyXIRCC5yOBQhoOhqu+loIiEuP7avNyUTx1drzNDAMw==; tag_view_ranking=EZQqoW9r8g~0xsDLqCEW6~eFs6si-q7J~faHcYIP1U0~2R7RYffVfj~Lt-oEicbBr~d2FncN8CBI~yqPUQRcWeb~qWFESUmfEs~iFcW6hPGPU~Hjx7wJwsUT~WcIcGAgRIK~B_OtVkMSZT~MM6RXH_rlN~5oPIfUbtd6~KN7uxuR89w~nf2nMUUZFU~1n-RsNEFpK~RTJMXD26Ak~gpglyfLkWs~CiSfl_AE0h~28gdfFXlY7~eVxus64GZU~VMjn4VzDLQ~tgP8r-gOe_~-98s6o2-Rp~azESOjmQSV~JBFbzljAuI~13HpD_lYAn~EGefOqA6KB~K8esoIs2eW~_RfiUqtsxe~qadCPKe0Fl~2kpvX0L5nu~ADMBPKfY5n~RybylJRnhJ~CAH-OfIs-U~9zcPibj6VK~EWJG2DcRyX~8cMNTf_lvu~P5-w_IbJrm~JM7vfxKDmx~udkRh_mjvd~kxn0BdkcW5~QcneKFYI8h~PlA_M1Z8tl~CztRgmi8vs~OJ3Bxo1Xfn~-_xRkJ5N3r~MmXTpQaDvv~Kv3rJH_PbC~C9iRb0VTwK~TcgCqYbydo~rIC2oNFqzh~GACl-vLazK~CrFcrMFJzz~HFX-xbTwCV~WlKkwEuUi0~KC--pudNUr~TWrozby2UO~jk9IzfjZ6n~HY55MqmzzQ~LJo91uBPz4~UIfHbi0qTk~wmxKAirQ_H~Ie2c51_4Sp~BU9SQkS-zU~R8LJXFI4V3~E8plmQ7kUK~Js5EBY4gOW~Hh52hrn0oF~hEuKWOJ6dp~nW7EMOuPvx~ZmBaQpwChs~F4f0UIjqZv~w8ffkPoJ_S~T8AkHNylGZ~t6fkfIQnjP~s3i_irjAJg~lOoByuwkMh~e6DJejypJg~Et8qKXA3LZ~eVBXl1t9y6~VEWLVR2U9i~Acf27EJzsC~QzKFCsGzn-~_kLUzfSDqN~7H3YOcbzOl~iacT4zaFWi~Aw_dznQmg1~_RZumrVuci~mLrrjwTHBm~kym2Z4vnZu~nQRrj5c6w_~j547Ftwyuu~n7YxiukgPF~KOnmT1ndWG~xJsg2eui8K~BtXd1-LPRH~jS8TGx1n0i; _gat=1; PHPSESSID=25103980_gsoQ2p3yPHpD7p9q6MHQwrEw5c7w1ix0; device_token=a1b1976b5f8f694cf172544cb0c82834; privacy_policy_agreement=2'
#         }
#
#     def start_request(self, url, headers):
#         res = requests.get(url, headers=headers)
#         return res
#
#     hot_url = 'https://www.pixiv.net/ranking.php?mode=daily_r18'
#
#     def get_img_id(self, res_text):
#         tree = etree.HTML(res_text)
#         img_id_list = tree.xpath('//div[class="ranking-items adjust"]/section')
#         for img in img_id_list:
#             img_id = img.xpath('./@data-id')[0]
#             img_name = img.xpath('./@data-title')[0]
#             return img_id, img_name
#
#     def get_detail_page(self, res):
#         response = self.res(self.hot_url, self.default_headers).text
#         detail_page = self.get_img_id(response)
#         print(detail_page)
