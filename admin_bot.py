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
        print(send)
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
        print(send.json())
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

token = database.special('API 2',cur)
offset = 0

logged_in = [468930122]
interest = {}

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
            if sender_id not in logged_in:
                bot.send_message(sender_id, 'Enter your password')
                bot.get_updates(offset = update_id+1)
            else:
                if callback_data == 'Nothing':
                    bot.get_updates(offset = update_id+1)

                elif callback_data == 'Total Deposit':
                    all_dep = database.all_depo(cur)
                    if all_dep == 'Nothing':
                        bot.edit_message_two(sender_id, message_id, 'No Deposit done yet', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                    else:
                        full_text = ''
                        for i in all_dep:
                            if len(full_text) > 3800:
                                bot.send_message(sender_id, full_text)
                                full_text = ''
                            full_text += f'Amount: {i[0]}, Transaction Hash: {i[1]}\n\n'
                        bot.edit_message_two(sender_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)

                elif callback_data == 'Back':
                    total_user = database.total_user(cur)
                    total_depo = database.total_depo(cur)
                    total_depo = format(total_depo, ',.8f')
                    if sender_id in interest:
                        del interest[sender_id]
                    bot.edit_message_two(sender_id, message_id, 'Select one of the option from below', [[{'text':f'Total User: {total_user}', 'callback_data':'Nothing'}],
                                                                                        [{'text':f'Total Deposit: {total_depo} BTC', 'callback_data':'Total Deposit'}],
                                                                                        [{'text':'Pending Withdrawal', 'callback_data':'Pending Withdrawal'}],
                                                                                        [{'text':'Set Interest of Today','callback_data':'Enter Interest'}]])
                    bot.get_updates(offset = update_id+1)

                elif callback_data == 'Pending Withdrawal':
                    pending_id = database.pending(cur)
                    if pending_id == 'Nothing':
                        bot.edit_message_two(sender_id, message_id, 'No withdrawal is pending', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                    else:
                        pending_amount = len(pending_id)
                        full_text = f'Pending Withdrawal {pending_amount}\n\nPending Message ID: '
                        for i in pending_id:
                            if len(full_text) > 3800:
                                bot.send_message(sender_id, full_text)
                            full_text += f'{i[0]},'
                        full_text += '\n\nTo Get Full Details of a Withdrawal, send the following Command\n\n$data (Message ID)\n\nExample$data 5\n$data 38\n\nTo mark a withdrawal as Complete, send the command below\n\n$withdraw (Message ID) (transaction hash)'
                        bot.edit_message_two(sender_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)

                elif callback_data == 'Enter Interest':
                    bot.edit_message_two(sender_id, message_id, 'Enter interest rate in Digit', [[{'text':'Back', 'callback_data':'Back'}]])
                    interest[sender_id] = 0
                    bot.get_updates(offset = update_id+1)      
                
                elif callback_data == 'Inte Posi':
                    all_user = database.all_user(cur)
                    if all_user == 'Nothing':
                        bot.edit_message_two(sender_id, message_id, 'No ID available to sent interest', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)  
                    else:
                        for i in all_user:
                            bala = float(i[2])
                            inte = bala * interest[sender_id] / 100
                            bala = bala + inte
                            database.update_bala(i[0], bala, cur)
                            if i[1] == 0:
                                pass
                            else:
                                ref_bala = float(database.find_bala(i[1], cur))
                                ref_bala += inte * 5 / 100
                                database.update_bala(i[1], ref_bala, cur)
                        bot.edit_message_two(sender_id, message_id, 'Positive Interest Sent', [[{'text':'Back', 'callback_data':'Back'}]])
                        database.inte_update(f'+{interest[sender_id]}', cur)
                        del interest[sender_id]
                        bot.get_updates(offset = update_id+1) 
                
                elif callback_data == 'Inte Nega':
                    all_user = database.all_user(cur)
                    if all_user == 'Nothing':
                        bot.edit_message_two(sender_id, message_id, 'No ID available to sent interest', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)  
                    else:
                        for i in all_user:
                            bala = float(i[2])
                            inte = bala * interest[sender_id] / 100
                            bala = bala - inte
                            database.update_bala(i[0], bala, cur)
                            if i[1] == 0:
                                pass
                            else:
                                ref_bala = float(database.find_bala(i[1], cur))
                                ref_bala -= inte * 5 / 100
                                database.update_bala(i[1], ref_bala, cur)
                        bot.edit_message_two(sender_id, message_id, 'Negative Interest Sent', [[{'text':'Back', 'callback_data':'Back'}]])
                        database.inte_update(f'-{interest[sender_id]}', cur)
                        del interest[sender_id]
                        bot.get_updates(offset = update_id+1)

        else:
            text = current_updates['message']['text']
            print(text)

            if text == '/start' and sender_id not in logged_in:
                if sender_id in interest:
                    del interest[sender_id]
                bot.send_message(sender_id, 'Enter your password')
                bot.get_updates(offset = update_id+1)
            
            elif text == '/start' and sender_id in logged_in:
                if sender_id in interest:
                    del interest[sender_id]
                total_user = database.total_user(cur)
                total_depo = database.total_depo(cur)
                total_depo = format(total_depo, ',.8f')
                bot.send_message_four(sender_id, 'Select one of the option from below', [[{'text':f'Total User: {total_user}', 'callback_data':'Nothing'}],
                                                                                        [{'text':f'Total Deposit: {total_depo} BTC', 'callback_data':'Total Deposit'}],
                                                                                        [{'text':'Pending Withdrawal', 'callback_data':'Pending Withdrawal'}],
                                                                                        [{'text':'Set Interest of Today','callback_data':'Enter Interest'}]])
                bot.get_updates(offset = update_id+1)
            
            elif sender_id not in logged_in and text != database.special('Pass', cur):
                bot.send_message(sender_id, 'Invalid Password')
                bot.get_updates(offset = update_id+1)

            elif text == database.special('Pass', cur) and sender_id not in logged_in:
                bot.send_message(sender_id, 'Access Granted')
                bot.delete_message(sender_id, message_id)
                logged_in.append(sender_id)
                total_user = database.total_user(cur)
                total_depo = database.total_depo(cur)
                total_depo = format(total_depo, ',.8f')
                bot.send_message_four(sender_id, 'Select one of the option from below', [[{'text':f'Total User: {total_user}', 'callback_data':'Nothing'}],
                                                                                        [{'text':f'Total Deposit: {total_depo} BTC', 'callback_data':'Total Deposit'}],
                                                                                        [{'text':'Pending Withdrawal', 'callback_data':'Pending Withdrawal'}],
                                                                                        [{'text':'Set Interest of Today','callback_data':'Enter Interest'}]])
                bot.get_updates(offset = update_id+1)

            elif text.startswith('$data') and sender_id in logged_in:
                data = text.split(' ')[1]
                history = database.find_history_two(int(data), cur)
                full_text = ''
                for i in history:
                    da_ti = datetime.fromtimestamp(float(i[4]))
                    if i[0] == 'Deposit':
                        full_text += f'Type: {i[0]}\nTransaction Hash: {i[1]}\nAmount: {i[3]} BTC\nTime: {da_ti}'
                        bot.send_message_four(sender_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                    elif i[0] == 'Withdraw':
                        full_text += f'Type: {i[0]}\nTransaction Hash: {i[1]}\nAmount: {i[3]} BTC\nTime: {da_ti}'
                        bot.send_message(sender_id, full_text)
                        bot.send_message_four(sender_id, f'{i[2]}', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)

            elif text.startswith('$withdraw') and sender_id in logged_in:
                data = text.split(' ')
                database.update_trans(data[1], data[2], cur)
                bot.send_message_four(sender_id, 'Transaction Updated', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif sender_id in interest and sender_id in logged_in:
                
                try:
                    inte = float(text)
                    interest[sender_id] = inte
                    print(interest)
                    bot.send_message_four(sender_id, f'Interest Rate {inte}. Interest Positive or Negative?', [[{'text':'Positive', 'callback_data':'Inte Posi'}, {'text':'Negative', 'callback_data':'Inte Nega'}],
                                                                                                [{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                except:
                    bot.send_message_four(sender_id, 'Not a Digit. Try again', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)

    except Exception as e:
        print(e)
        print('got an error')
        bot.get_updates(offset = update_id+1)
        pass

starter()