from TikTokApi import TikTokApi
import random

# If playwright doesn't work for you try to use selenium
verifyFp="verify_klx5xh3o_nlqX32yV_KusN_4BW3_943p_q9cUZCRRbQXH"

results = 100
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
did = str(random.randint(10000, 999999999))


johnMayerTikToks = api.byUsername(username="johnmayer", custom_did=did)


for tiktok in johnMayerTikToks:
    #gets the videobytes for all John Mayer TikToks
    video_bytes=api.get_Video_By_TikTok(tiktok, custom_did=did)
    
    with open(tiktok['id']+".mp4", 'wb') as o:
        o.write(video_bytes)


#print(johnMayerTikToks)
print("success")
