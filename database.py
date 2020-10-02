def add_user(tele_id, cur):
    sql = f"INSERT INTO users(Telegram_ID) VALUES('{tele_id}')"
    cur.execute(sql)

def find_user(user_id, cur):
    cur.execute(f"SELECT Telegram_ID FROM users WHERE Telegram_ID = '{user_id}'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows[0][0]

def with_add(user_id, cur):
    cur.execute(f"SELECT Withdrawal_Address FROM users WHERE Telegram_ID = '{user_id}'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows[0][0]

def find_bala(user_id, cur):
    cur.execute(f"SELECT Balance FROM users WHERE Telegram_ID = '{user_id}'")
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return rows[0][0]

def update_bala(user_id, bala, cur):
    sql = f"UPDATE users SET Balance = '{bala}' WHERE Telegram_ID = '{user_id}'"
    cur.execute(sql)

def update_with(user_id, add, cur):
    sql = f"UPDATE users SET Withdrawal_Address = '{add}' WHERE Telegram_ID = '{user_id}'"
    cur.execute(sql)

def find_ref(user_id, cur):
    cur.execute(f"SELECT Referral_ID FROM users WHERE Telegram_ID = '{user_id}'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows[0][0]

def update_ref(user_id, ref, cur):
    sql = f"UPDATE users SET Referral_ID = '{ref}' WHERE Telegram_ID = '{user_id}'"
    cur.execute(sql)

def special(code ,cur):
    cur.execute(f"SELECT Detail FROM special WHERE code = '{code}'")
    rows = cur.fetchall()
    return rows[0][0]

def find_history(sender_id, ty_trans, cur):
    cur.execute(f"SELECT Transaction_ID, Wallet, Amount, Time FROM history WHERE Telegram_ID = '{sender_id}' and Type = '{ty_trans}'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows

def get_depo(cur):
    cur.execute(f"SELECT Detail FROM special WHERE code = 'Depo'")
    rows = cur.fetchall()
    return rows[0][0]

def get_trans(trans, cur):
    cur.execute(f"SELECT Transaction_ID FROM history WHERE Transaction_ID = '{trans}'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows

def depo_trans(tele_id, trans, amount, time, cur):
    sql = f"INSERT INTO history(Telegram_ID, Type, Transaction_ID, Wallet, Amount, Time) VALUES('{tele_id}', 'Deposit', '{trans}', 'Nothing', '{amount}', '{time}')"
    cur.execute(sql)

def get_profit(cur):
    cur.execute(f"SELECT Detail FROM special WHERE code = 'Profit'")
    rows = cur.fetchall()
    return rows[0][0]

def with_trans(tele_id, wallet, amount, time, cur):
    sql = f"INSERT INTO history(Telegram_ID, Type, Transaction_ID, Wallet, Amount, Time) VALUES('{tele_id}', 'Withdraw', 'Pending', '{wallet}', '{amount}', '{time}')"
    cur.execute(sql)

def get_term(number, cur):
    cur.execute(f"SELECT Detail FROM special WHERE code = 'term {number}'")
    rows = cur.fetchall()
    return rows[0][0]

def total_user(cur):
    cur.execute(f"SELECT COUNT(*) FROM users")
    rows = cur.fetchall()
    return rows[0][0]

def total_depo(cur):
    cur.execute(f"SELECT sum(Amount) FROM history WHERE Type = 'Deposit'")
    rows = cur.fetchall()
    return rows[0][0]

def all_depo(cur):
    cur.execute(f"SELECT Amount, Transaction_ID FROM history WHERE Type = 'Deposit'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows

def pending(cur):
    cur.execute(f"SELECT ID_Num FROM history WHERE Type = 'Withdraw'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows

def find_history_two(id_num, cur):
    cur.execute(f"SELECT, Type, Transaction_ID, Wallet, Amount, Time FROM history WHERE ID_Num = '{id_num}'")
    rows = cur.fetchall()
    if rows == []:
        return 'Nothing'
    else:
        return rows