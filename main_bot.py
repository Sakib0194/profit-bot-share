#!/usr/bin/env python3
#find me at t.me/Sakib0194 if you are looking to create a bot
import requests, json, random, string, time, requests, mysql.connector, sys
import database
from datetime import datetime

class BoilerPlate:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=0, timeout=2):         #FOR GETTING UPDATES
        function = 'getUpdates'
        fieldss = {'timeout' : timeout, 'offset': offset}
        send = requests.get(self.api_url + function, fieldss)
        #print(send.json())
        result_json = send.json()['result']
        return result_json

    def send_message(self, chat_id, text, disable_web_page_preview=False, parse_mode='HTML'):                  #FOR SENDING NORMAL MESSAGE
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'disable_web_page_preview':disable_web_page_preview}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send

    def send_message_two(self, chat_id, text, reply_markup, one_time_keyboard=False, resize_keyboard=True, disable_web_page_preview=True, parse_mode='HTML'):         #FOR SENDING MESSAGE WITH KEYBOARD INCLUDED
        reply_markup = json.dumps({'keyboard': reply_markup, 'one_time_keyboard': one_time_keyboard, 'resize_keyboard': resize_keyboard, 'disable_web_page_preview':disable_web_page_preview})
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'reply_markup': reply_markup}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss).json()
        #print(send)
        return send

    def send_message_three(self, chat_id, text, remove_keyboard, parse_mode='HTML'):               #FOR SENDING MESSAGES AND TO REMOVE KEYBOARD
        reply_markup = json.dumps({'remove_keyboard': remove_keyboard})
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'reply_markup': reply_markup}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss).json()
        return send   

    def send_message_four(self, chat_id, text, reply_markup, disable_web_page_preview=True, parse_mode='HTML'):               #FOR SENDING MESSAGES WITH INLINE KEYBOARD
        reply_markup = json.dumps({'inline_keyboard': reply_markup})
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'reply_markup': reply_markup, 'disable_web_page_preview':disable_web_page_preview}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss)
        #print(send)
        #print(send.json)
        return send.json()

    def send_photo(self, chat_id, photo):
        fieldss = {'chat_id':chat_id, 'photo':photo}
        function = 'sendPhoto'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send 

    def send_video(self, chat_id, video):
        fieldss = {'chat_id':chat_id, 'video':video}
        function = 'sendVideo'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send 
    
    def send_document(self, chat_id, document):
        fieldss = {'chat_id':chat_id, 'document':document}
        function = 'sendDocument'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send 

    def send_sticker(self, chat_id, sticker):
        fieldss = {'chat_id':chat_id, 'sticker':sticker}
        function = 'sendSticker'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send 
    
    def InLineAnswer(self, inline_query_id, results):                   #FOR MANAGING INLINE REPLIES
        fieldss = {"inline_query_id": inline_query_id, "results" : results}
        function = 'answerInlineQuery'
        send = requests.post(self.api_url + function, fieldss)
        return send   

    def deleteWebhook(self):                #FOR DELETING WEBHOOK
        function = 'deleteWebhook'
        send = requests.post(self.api_url + function)
        return send

    def delete_message(self, group_id, message_id):         #FOR DELETING MESSAGES FROM GROUP
        fieldss = {'chat_id': group_id, 'message_id': message_id}
        function = 'deleteMessage'
        send = requests.post(self.api_url + function, fieldss)
        return send

    def get_admins(self, chat_id):              #ADMIN LIST IN A GROUP
        function = 'getChatAdministrators'
        fieldss = {'chat_id':chat_id}
        send = requests.get(self.api_url + function, fieldss)
        return send.json()['result']

    def edit_message (self, chat_id, message_id, text):
        fieldss = {'chat_id': chat_id, 'message_id': message_id, 'text': text, 'parse_mode':'MarkdownV2'}
        function = 'editMessageText'
        send = requests.post(self.api_url + function, fieldss)
        return send

    def edit_message_two (self, chat_id, message_id, text, reply_markup, disable_web_page_preview=True, parse_mode='HTML'):
        reply_markup = json.dumps({'inline_keyboard': reply_markup})
        fieldss = {'chat_id': chat_id, 'message_id': message_id, 'text': text, 'parse_mode':parse_mode, 'reply_markup':reply_markup, 'disable_web_page_preview':disable_web_page_preview}
        function = 'editMessageText'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send

    def restrict_everyone(self, chat_id):
        Chat = {'can_send_messages':False, 'can_send_media_messages':False, 'can_send_polls':False, 'can_send_other_messages':False, 'can_add_web_page_previews':False, 'can_change_info':False, 'can_invite_users':False, 'can_pin_messages':False}
        permissions = json.dumps(Chat)
        fieldss = {'chat_id': chat_id, 'permissions':permissions}
        function = 'setChatPermissions'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send

    def enable_everyone(self, chat_id):
        Chat = {'can_send_messages':True, 'can_send_media_messages':True, 'can_send_polls':True, 'can_send_other_messages':True, 'can_add_web_page_previews':True, 'can_change_info':False, 'can_invite_users':True, 'can_pin_messages':False}
        permissions = json.dumps(Chat)
        fieldss = {'chat_id': chat_id, 'permissions':permissions}
        function = 'setChatPermissions'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send

    def ban(self, chat_id, user_id):
        function = 'kickChatMember'
        fieldss = {'chat_id': chat_id, 'user_id':user_id}
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send

details = sys.argv[1:]
conn = mysql.connector.connect(host=details[0],user=details[1],database=details[2],password=details[3], autocommit=True)
cur = conn.cursor()

token = database.special('API', cur)
offset = 0

change_address = []
with_amount = []


special = ['[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']

bot = BoilerPlate(token)

def starter():
    global offset, conn, cur
    while True:
        try:
            if conn.is_connected() == True:
                pass
            else:
                conn = mysql.connector.connect(host=details[0],user=details[1],database=details[2],password=details[3], autocommit=True)
                cur = conn.cursor()
            all_updates = bot.get_updates(offset)
            for current_updates in all_updates:
                print(current_updates, '\n')
                update_id = current_updates['update_id']
                #bot.get_updates(offset = update_id+1)
                try:
                    if 'callback_query' in current_updates:
                        #print('inline keyboard detected')
                        sender_id = current_updates['callback_query']['from']['id']
                        group_id = current_updates['callback_query']['message']['chat']['id']
                        message_id = current_updates['callback_query']['message']['message_id']
                        callback_data = current_updates['callback_query']['data']
                        bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, 0, cur, callback_data=callback_data, callback=True)
                    else:
                        group_id = current_updates['message']['chat']['id']
                        sender_id = current_updates['message']['from']['id']
                        message_id = current_updates['message']['message_id']
                        dict_checker = []
                        for keys in current_updates.get('message'):
                            dict_checker.append(keys)
                        #for i in dict_checker:
                        #    print(i)
                        #if sender_id != group_id:
                        #    group_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, cur)
                        if sender_id == group_id:
                            bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, cur)
                except:
                    bot.get_updates(offset = update_id+1)
        except Exception as e:
            print(e)
            print('got an error')
            pass

def bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, cur, callback_data=0, callback=False):
    try:
        if callback == True:
            print(callback_data)

            if callback_data == 'Deposit':
                depo_add = database.get_depo(cur)
                bot.send_message(sender_id, depo_add)
                bot.send_message_four(sender_id, 'Send your Deposit to the address above and paste the Transaction Hash. Minimum Deposit 0.005 BTC', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Withdraw':
                cu_add = database.with_add(sender_id, cur)
                with_add = database.with_add(sender_id, cur)
                if with_add == 'Nothing':
                    bot.edit_message_two(sender_id, message_id, 'No Withdrawal Address Found. Send your wallet address now', [[{'text':'Back', 'callback_data':'Back'}]])
                    change_address.append(sender_id)
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.edit_message_two(sender_id, message_id, f'Current Wallet Address\n\n{cu_add}\n\nEnter the amount of BTC to withdraw', [[{'text':'Back', 'callback_data':'Back'}]])
                    with_amount.append(sender_id)
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Terms':
                for i in range(1, 9):
                    terms = database.get_term(i, cur)
                    bot.send_message(sender_id, terms)
                last_term = database.get_term(9, cur)
                bot.send_message_four(sender_id, last_term, [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Performance':
                profit = database.get_profit(cur)
                cu_bal = database.find_bala(sender_id, cur)
                bot.edit_message_two(sender_id, message_id, f'Current Balance: {cu_bal}\n24 hour profit: {profit}%', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Referral':
                ref_link = f'https://t.me/simplifiedcryptobot?start={sender_id}'
                bot.edit_message_two(sender_id, message_id, f'Your referral link:\n{ref_link}', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Change Address':
                cu_add = database.with_add(sender_id, cur)
                bot.edit_message_two(sender_id, message_id, f'Current Withdrawal Address\n\n{cu_add}\n\nSend your new address now to change it', [[{'text':'Back', 'callback_data':'Back'}]])
                change_address.append(sender_id)
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Back':
                if sender_id in with_amount:
                    with_amount.remove(sender_id)
                if sender_id in change_address:
                    change_address.remove(sender_id)
                bot.send_message_four(sender_id, 'Select an option from below', [[{'text':'Performance','callback_data':'Performance'}, {'text':'Deposit', 'callback_data':'Deposit'}],
                                                                        [{'text':'Withdraw','callback_data':'Withdraw'}, {'text':'Change Address', 'callback_data':'Change Address'}],
                                                                        [{'text':'Referral', 'callback_data':'Referral'}],
                                                                        [{'text':'Terms', 'callback_data':'Terms'}, {'text':'History', 'callback_data':'History'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'History':
                depo_his = database.find_history(sender_id, 'Deposit', cur)
                with_his = database.find_history(sender_id, 'Withdraw', cur)
                full_text = ''
                if depo_his == 'Nothing':
                    full_text += 'Deposit History\n\nNoting\n\n'
                else:
                    full_text += f'Deposit History\n\n'
                    for i in depo_his:
                        if len(full_text) > 3800:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        da_ti = datetime.fromtimestamp(float(i[3]))
                        full_text += f'Transaction Hash: {i[0]}, Amount: {i[2]} BTC, Time: {da_ti}\n\n'
                if with_his == 'Nothing':
                    full_text += 'Withdraw History\n\nNothing'
                else:
                    full_text += f'Withdraw History\n\n'
                    for i in with_his:
                        if len(full_text) > 3800:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        da_ti = datetime.fromtimestamp(float(i[3]))
                        full_text += f'Transaction Hash: {i[0]}, Wallet: {i[1]}, Amount: {i[2]} BTC, Time: {da_ti}\n\n'
                bot.send_message_four(sender_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

        else:
            text = current_updates['message']['text']
            print(text)

            if text.startswith('/start'):
                if sender_id in with_amount:
                    with_amount.remove(sender_id)
                if sender_id in change_address:
                    change_address.remove(sender_id)
                if database.find_user(sender_id, cur) == 'Nothing':
                    database.add_user(sender_id, cur)
                if database.find_ref(sender_id, cur) == 0:
                    try:
                        data = text.split(' ')[1]
                        database.update_ref(sender_id, data, cur)
                    except:
                        pass
                bot.send_message_four(sender_id, 'Select an option from below', [[{'text':'Performance','callback_data':'Performance'}, {'text':'Deposit', 'callback_data':'Deposit'}],
                                                                        [{'text':'Withdraw','callback_data':'Withdraw'}, {'text':'Change Address', 'callback_data':'Change Address'}],
                                                                        [{'text':'Referral', 'callback_data':'Referral'}],
                                                                        [{'text':'Terms', 'callback_data':'Terms'}, {'text':'History', 'callback_data':'History'}]])
                bot.get_updates(offset = update_id+1)

            elif sender_id in change_address:
                if len(text) < 20:
                    bot.send_message_four(sender_id, 'Invalid Address. Try Again', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    database.update_with(sender_id, text, cur)
                    bot.send_message_four(sender_id, 'Wallet Address Updated', [[{'text':'Back', 'callback_data':'Back'}]])
                    change_address.remove(sender_id)
                    bot.get_updates(offset = update_id+1)

            elif sender_id in with_amount:
                try:
                    amount = float(text)
                    cu_bal = float(database.find_bala(sender_id, cur))
                    cu_add = database.with_add(sender_id, cur)
                    if amount < 0.005:
                        bot.send_message_four(sender_id, 'Amount too small. Minimum withdraw 0.005 BTC. Press Back to Cancel or enter a new Amount', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                    else:
                        if amount <= cu_bal:
                            bot.send_message_four(sender_id, f'Request Sent to withdraw {amount} BTC. Withdrawal will be processed soon!', [[{'text':'Done', 'callback_data':'Back'}]])
                            with_amount.remove(sender_id)
                            database.with_trans(sender_id, cu_add, amount, time.time(), cur)
                            cu_bal -= amount
                            database.update_bala(sender_id, cu_bal, cur)
                            bot.get_updates(offset = update_id+1)
                        elif amount > cu_bal:
                            bot.send_message_four(sender_id, 'Not Enough Balance. Press Back to Cancel or enter a new Amount', [[{'text':'Back', 'callback_data':'Back'}]])
                            bot.get_updates(offset = update_id+1)
                except:
                    bot.send_message_four(sender_id, 'Invalid Number to Withdraw. Enter a Valid BTC Amount', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)

            elif len(text) > 60:
                try:
                    bot.send_message(sender_id, 'Transaction Hash Detected')
                    if database.get_trans(text, cur) == 'Nothing':
                        depo_add = database.get_depo(cur)
                        a = requests.get(f'https://blockchain.info/rawtx/{text}').json()
                        data = a['out']
                        outputs = {}
                        for i in data:
                                try:
                                    outputs[i['addr']] = i['value']
                                except:
                                    pass
                        if depo_add in outputs:
                            amount = float(int(outputs[depo_add])/100000000)
                            if amount < 0.005:
                                bot.send_message_four(sender_id, 'Deposit amount too small. Deposit failed. Contact @dashe79 to resolve it', [[{'text':'Back', 'callback_data':'Back'}]])
                                bot.get_updates(offset = update_id+1)
                            else:
                                bot.send_message_four(sender_id, f'Deposit successful. {amount} Deposited', [[{'text':'Back', 'callback_data':'Back'}]])
                                database.depo_trans(sender_id, text, amount, time.time(), cur)
                                cu_bal = float(database.find_bala(sender_id, cur))+ amount
                                database.update_bala(sender_id, cu_bal, cur)
                                bot.get_updates(offset = update_id+1)
                        else:
                            bot.send_message_four(sender_id, 'Deposit Failed. Transaction not sent to the Deposit Address', [[{'text':'Back', 'callback_data':'Back'}]])
                            bot.get_updates(offset = update_id+1)
                    else:
                        bot.send_message_four(sender_id, 'Transaction Hash Already Used. Invalid Transaction Hash', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                except:
                    bot.send_message_four(sender_id, 'Invalid Transaction Hash', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)

    except Exception as e:
        print(e)
        print('got an error')
        bot.get_updates(offset = update_id+1)
        pass

starter()