#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file: tests/model/test_conntectiob.py
@time: 2022/12/06 20:03
@desc:
"""

import requests


def test_connection():
    """refer to xiaofei's friday."""
    inference_parameters = {
        "request_timeout": 10000,
        "engine": "text-davinci-003",  # 这个是选择engine，也就是到底用什么模型，text-davinci-003是最贵最好的
        "temperature": 0.7,  # 控制随机程度
        "max_tokens": 20,  # 最大token数量
        "top_p": 1,  # 控制多样性，目前我们没有多样性，这个和temperature的相互配合还没有测试
        "frequency_penalty": 1,  # 对于频次的惩罚，这个值调高可以降低重复词
        "presence_penalty": 1,  # 这个是对于词是否已经出现过的惩罚，文档上说这个值调高可以增大谈论新topic的概率，和frequency_penalty的关系还没有测试
        "best_of": 1,  # 这个是说从多少个里选最好的，如果这里是10，就会生成10个然后选最好的，但是这样会更贵,
    }

    prompt = "This is a topic classifier.\nFirst, please list key clues and briefly explain the reasoning process for determining the topic of the INPUT sentence (Limit the number of words to 70).\nNext, based on the clues, the reasoning process and the INPUT sentence, classify the topic into one of the eight categories: Money/Foreign Exchange, Acquisitions, Trade, Interest Rates, Shipping, Earnings and Earnings Forecasts, Grain, Crude Oil.\n\nINPUT: yeutter sees u japan trade conflict united states japan brink serious conflict trade especially semiconductors japanese unwillingness public bodies buy u super computers barriers u firms seeking participate eight billion dlr kansai airport project u trade representative clayton yeutter said talking reporters yesterday two day meeting trade ministers review progress made committees set uruguay meeting last september launched new round gatt general agreement tariffs trade talks european community ec commissioner\nClues and the reasoning process: \nTOPIC: Trade\n\nINPUT: yeutter sees u japan trade conflict united states japan brink serious conflict trade especially semiconductors japanese unwillingness public bodies buy u super computers barriers u firms seeking participate eight billion dlr kansai airport project u trade representative clayton yeutter said talking reporters yesterday two day meeting trade ministers review progress made committees set uruguay meeting last september launched new round gatt general agreement tariffs trade talks european community ec commissioner\nClues and the reasoning process: List the words used in the PROCESS (Processed words).\nAdvertisements:\nTOPIC: Trade\n\nINPUT: u official visit japan trade row undersecretary state michael armacost visit tokyo next week meetings high level officials include talks growing trade row japanese semiconductor electronics products first high level u official visit japan since president reagan announced last week plans impose tariffs worth mln dlrs japanese electronic goods april retaliation tokyo alleged failure live pact microchip trade signed last september deputy state department spokeswoman said trip set april u\nClues and the reasoning process: TOPIC: trade \nThe TOPIC category can be set to either \"Trade\" or \"Interdiction\" . Both can be set to the same category.\nThe TOPIC category can be set to either \"Trade\" or \"Interdiction\" . Both can be set to the same category.\n1) The reasoning process for the TOPIC category can be described as follows.\n2) The reasoning process for the two related categories are:\n3) In the TOPIC category the reasoning process for the two related categories can be described as follows.\nTOPIC: Trade\n\nINPUT: japan gatt south korea import plan japan told general agreement tariffs trade south korea five year import diversification plan violated spirit world trade governing body foreign ministry spokesman said notification came japan answer recent gatt unfair trade practices spokesman said five year plan starts year south korea aims reduce dependency japan source imported goods increase imports u europe japan move came several unsuccessful bilateral negotiations plan spokesman said notification represent\nClues and the reasoning process: The case study presented in the analysis is the following.\nThe example below shows the inconsistency of the guidelines in the WTO.\nThe following guidelines are not in the WTO agreement:\nThe following guidelines are not in the WTO agreement:\nThe following guidelines are not in the WTO agreement:\nThe following guidelines are not in the WTO agreement:\nThe following guidelines are not in the WTO agreement:\nThe following guidelines are not in the WTO agreement:\nThe following guidelines are not in the WTO agreement:\nThe following guidelines are\nTOPIC: Trade\n\nINPUT: nakasone conciliatory note chip dispute prime minister yasuhiro nakasone sounded conciliatory note japan increasingly bitter row united states trade computer microchips japan wants resolve issue consultations explaining stance correcting points need corrected quoted news service saying expressing regret america decision impose tariffs imports japanese electrical goods nakasone said tokyo willing send high level official washington help settle dispute government officials said japan would make formal request next week emergency talks\nClues and the reasoning process: Key points and explanations of the reasoning process:\nIn the TOPIC category, the items under the 'clues' are:\nClues are combined with the 'key points' (using the 'choose key points' field) to form a list of the key points that form the TOPIC category.\nThe 'key points' can be any of the items on the list.\nThe 'key points' are the things that make the TOPIC category.\nThe 'key points' are:\nThe 'key points' are:\nTOPIC: Trade\n\nINPUT: nakasone conciliatory note chip dispute prime minister yasuhiro nakasone sounded conciliatory note japan increasingly bitter row united states trade computer microchips japan wants resolve issue consultations explaining stance correcting points need corrected quoted news service saying expressing regret america decision impose tariffs imports japanese electrical goods nakasone said tokyo willing send high level official washington help settle dispute government officials said japan would make formal request next week emergency talks\nClues and the reasoning process: In order to create a TOPIC category, there must be a hint or a hint-like phrase to be used to create a TOPIC category.\nA hint indicates that the phrase or phrase-like phrase that appears in the TOPIC category is a \"hint-like phrase\" (for example, \"hint-like phrase\" for \"hint\").\nThere are two kinds of hints:\nA hint may be used in the same sentence, as in \"cut a deal with the devil\". A hint-like phrase can only be used in the same\nTOPIC: Trade\n\nINPUT: taiwan proposes tariff cuts taiwan said plans another round tariff cuts possibly within month try narrow trade surplus u vice finance minister ronald ho said high level economic committee recommended tariff cuts products requested washington including fruit juice ho said cuts may come effect end next month taiwan trade surplus u widened first two months year billion dlrs billion dlrs period last year reuter\nClues and the reasoning process: There are three steps in determining the INPUT:\nThe INPUT is limited to 50 words. If a word is more than 50 words then it will be placed in a different category.\nOf the 50 words, 50 words are used to limit the number of words.\nOf those words, the words in the 'READING' category are the ones that have not been read.\nIf words have been read but have not been read, or words that have been read but have not been read,\nTOPIC: Trade\n\nINPUT: taiwan proposes tariff cuts taiwan said plans another round tariff cuts possibly within month try narrow trade surplus u vice finance minister ronald ho said high level economic committee recommended tariff cuts products requested washington including fruit juice ho said cuts may come effect end next month taiwan trade surplus u widened first two months year billion dlrs billion dlrs period last year reuter\nClues and the reasoning process: START:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nSTOP:\nTOPIC: Trade\n\nINPUT: china calls better trade deal u china called united states remove curbs exports give favourable trading status ease restrictions exports high technology u embassy replied chinese figures showing years trade deficits u last inaccurate said peking would persuade congress change laws limit exports official international business newspaper today published china demands editorial coincide visit u secretary state george shultz extremely important u market reduce restrictions chinese imports provide needed facilities\nClues and the reasoning process: Key details and the reasoning process:\nA sentence containing two or more words will be considered as two distinct sentences.\nList details and the reasoning process:\nRefer to the TRADE INFORMATION: TRADE COSTS analysis completed previously.\nOral argument:\nLetter:\nThing:\nSpeaker:\nThing:\nSpeaker is a noun or pronoun.\nA sentence containing one or more words will be considered as a noun sentence.\nList details and the reasoning process:\nTwo or more noun\nTOPIC: Trade\n\nINPUT: u stock market tariffs yeutter u trade representative clayton yeutter said stock market u decision last week proceed tariffs japanese computer products speaking reporters prior house agriculture committee hearing yeutter said difficult trade decision affecting mln dlrs goods caused stock market collapse yesterday lot things involved stock market fall including simple profit taking yeutter said yeutter said japan would sending senior official trade ministry washington next week talks computer chip\nClues and the reasoning process: For example, if you want to create a TOPIC category for a product, you can first create a category of that product, then list the products that are listed in that category, then list the products in the category to which that product belongs. You can then list the products that are in that category and those products that are not listed in that category.\nThe reasoning process is straightforward, but it is important to note that the reasoning process is\nTOPIC: Trade\n\nINPUT: taiwan plans new tariff cuts taiwan plans another round deep tariff cuts year help narrow trade surplus u senior economic said wang vice chairman council economic planning development told reuters taiwan would reduce import tariffs products sometime second half year cuts pct items made last year wang said cuts would go much speed liberalisation cut import tariffs faster substantially said united states taiwan main trading partner said island import tariffs\nClues and the reasoning process: List the words of the TOPIC category.\nList the words of the TOPIC category in the following language:\nList the words of the TOPIC category as follows:\nList the words of the TOPIC category in the following language:\nList the words of the TOPIC category as follows:\nList the words of the TOPIC category in the following language:\nList the words of the TOPIC category as follows:\nList the words of the TOPIC category in the following language:\nList the words of the TOPIC category\nTOPIC: Trade\n\nINPUT: baldrige predicts end u japan trade dispute united states japan soon settle trade dispute semiconductors u commerce secretary malcolm baldrige said television baldrige referring u japan trade agreement semiconductors said government wants live industries think good settlement spare sides think japanese understand full well lived commitment said added think trade war friday washington announced plans put much mln dlrs tariffs japanese electronic goods april tokyo failure agreement officials said tariffs\nClues and the reasoning process: 1. is the TOPIC category in the INPUT a) an economic topic b) a \"underlying\" topic c) a \"referent\" topic d) both b) and c)\n2. the TOPIC category in the INPUT is a) a \"romantic subject\" b) a \"political topic\" c) an economic topic d) both b) and c)\n3. the TOPIC category in the INPUT is a) an economic topic b) a \"subject\" subject c) an economic topic d) both b) and c\nTOPIC: Trade\n\nINPUT: baldrige predicts end u japan trade dispute united states japan soon settle trade dispute semiconductors u commerce secretary malcolm baldrige said television baldrige referring u japan trade agreement semiconductors said government wants live industries think good settlement spare sides think japanese understand full well lived commitment said added think trade war friday washington announced plans put much mln dlrs tariffs japanese electronic goods april tokyo failure agreement officials said tariffs\nClues and the reasoning process: This article gives a valuable insight into the reasoning process of the system.\n1. \n2. \n3. \n4. \n5. \n6. \n7. \n8. \n9. \n10. \nhttp://www.amazon.com/gp/product/B00C5V5Y4Y/ref=cm_cr_pr_pr_p_1\nhttp://www.amazon.com/gp/product/B00CH6E8BVY\nhttp://\nTOPIC: Trade\n\nINPUT: reagan ready impose trade curbs japan president reagan ready impose retaliatory trade action japan breaking semiconductor agreement united states white house officials said immediate indication reagan might act recommendations economic policy council curb japanese exports united states officials said move could come today early next week trade sources said actions reagan include tariffs wide variety japanese exports use semiconductors sources said tariffs could personal computers television laser printers aim japan\nClues and the reasoning process: If an item is not in the TO-DO list, then it should be in the TO-DO list.\nIf an item is in the TO-DO list, then it should be in the INPUT list.\nIf items are in the TO-DO list, then they can be moved to the TO-DO list.\nIf items are not in the INPUT list, then they can be moved to the INPUT list.\nIf items are in the INPUT list, then they can be moved to the INPUT list.\nIf\nTOPIC: Trade\n\nINPUT: u trade official says japan action high level u trade official said would japan strike back united states sanctions japanese semiconductor electronics products asked reporters japan expected retaliate u exports deputy secretary commerce bruce smart replied would addition doubted japan could show enough progress meeting conditions agreement avoid actual imposition mln dlrs tariffs april japan billion dlr trade surplus united states last year come fire congress concerned loss jobs foreign\nClues and the reasoning process: Then, list the reasons for the decision on the basis of the clues.\nList the TOPIC category given the INPUT.\nLIST THE TOPIC INDICATOR (TO take the definitive decision on the highest-priority problem) and then break out the TOPIC category.\nList the TOPIC INDICATOR (TO take the definitive decision on the highest-priority problem) and then break out the TOPIC category.\nList the TOPIC INDICATOR (TO take the definitive decision on the highest-priority problem) and then break out the TOPIC category.\nTOPIC: Trade\n\nINPUT: japan ask companies boost imports japan minister international trade industry hajime tamura meet representatives nation largest companies next week appeal best increase imports ministry officials said meeting unveiled part plan boost imports help head protectionist legislation u senior officials ministry international trade industry told reporters personal appeals appeared paid past japanese imports manufactured goods climbed leading domestic semiconductor makers boost imports cut production key memory microchips next month attempt help\nClues and the reasoning process: A note that you can use is the \"Highest amount\" (40) means that the number of words has to be higher than the limit.\nThe key clue is:\nThe reasoning process is as follows:\nFor example:\nThe reason for the TOPIC category is as follows:\nTOPIC: Trade\n\nINPUT: asian exporters fear damage u japan mounting trade friction u japan raised fears among many asia exporting nations row could far reaching economic damage businessmen officials said told reuter correspondents asian u move japan might boost protectionist sentiment u lead curbs american imports products exporters said conflict would hurt long run short term tokyo loss might gain u said impose mln dlrs tariffs imports japanese electronics goods april retaliation japan\n"
    
    response = requests.post(
        "http://47.251.43.109:31021/api/generate",
        json={
            "prompt_list": [prompt],
            "inference_parameters": inference_parameters,
            "api_key_list": ["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"],
            "max_sleep_time": 100,
            "max_retries": 100,
            "version": "v1.1"
        }
    )

    print(response.json())
    result = response.json()["results_list"]
    print(result)


def test_connection_list():
    """refer to xiaofei's friday."""
    inference_parameters = {
        "request_timeout": 10000,
        "engine": "text-davinci-003",  # 这个是选择engine，也就是到底用什么模型，text-davinci-003是最贵最好的
        "temperature": 0.7,  # 控制随机程度
        "max_tokens": 20,  # 最大token数量
        "top_p": 1,  # 控制多样性，目前我们没有多样性，这个和temperature的相互配合还没有测试
        "frequency_penalty": 1,  # 对于频次的惩罚，这个值调高可以降低重复词
        "presence_penalty": 1,  # 这个是对于词是否已经出现过的惩罚，文档上说这个值调高可以增大谈论新topic的概率，和frequency_penalty的关系还没有测试
        "best_of": 1,  # 这个是说从多少个里选最好的，如果这里是10，就会生成10个然后选最好的，但是这样会更贵,
        "logprobs": 5
    }

    response = requests.post(
        "http://47.251.43.109:31021/api/generate_list_list",
        json={
            "prompt_list_list": [["I like cates"], ["I like cates"]],
            "inference_parameters": inference_parameters,
            "api_key_list": ["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",
                             "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"],
            "max_sleep_time": 100,
            "max_retries": 100,
            "version": "v1.1"
        }
    )

    print(response.json())


def test_local_connection():
    """refer to xiaofei's friday."""
    inference_parameters = {
        "request_timeout": 10000,
        "engine": "text-davinci-003",  # 这个是选择engine，也就是到底用什么模型，text-davinci-003是最贵最好的
        "temperature": 0.7,  # 控制随机程度
        "max_tokens": 20,  # 最大token数量
        "top_p": 1,  # 控制多样性，目前我们没有多样性，这个和temperature的相互配合还没有测试
        "frequency_penalty": 1,  # 对于频次的惩罚，这个值调高可以降低重复词
        "presence_penalty": 1,  # 这个是对于词是否已经出现过的惩罚，文档上说这个值调高可以增大谈论新topic的概率，和frequency_penalty的关系还没有测试
        "best_of": 1,  # 这个是说从多少个里选最好的，如果这里是10，就会生成10个然后选最好的，但是这样会更贵,
        "logprobs": 5
    }

    response = requests.post(
        "http://172.32.0.13:31022/api/generate",
        json={
            "prompt_list": ["I like cates"],
            "inference_parameters": inference_parameters,
            "api_key_list": ["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"],
            "max_sleep_time": 100,
            "max_retries": 100,
            "version": "v1.1"
        }
    )

    print(response.json())
    result = response.json()["results_list"]
    print(result)


if __name__ == "__main__":
    test_connection()
    # print("=" * 20)
    # test_connection_list()
    # test_local_connection()
