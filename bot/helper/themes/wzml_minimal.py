#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '⏤͟͞𝙍𝙞𝙯𝙯'
    ST_BN1_URL = 'https://t.me/aboutRizzx'
    ST_BN2_NAME = 'Owner'
    ST_BN2_URL = 'https://t.me/RD_C4'
    ST_MSG = '''<blockquote><b>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.Type {help_command} to get a list of available commands</b></blockquote>'''
    ST_BOTPM = '''<blockquote><i>Now, This bot will send all your files and links here. Start Using ...</blockquote></i>'''
    ST_UNAUTH = '''<blockquote><i>You Are not authorized user!</i></blockquote>'''
    OWN_TOKEN_GENERATE = '''<blockquote><b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i></blockquote>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<blockquote><b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i></blockquote>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "🚨 <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<blockquote>⌬ <b><i>BOT STATISTICS :</i></b>
┖ <b>Bot Uptime :</b> {bot_uptime}

┎ <b><i>RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>DISK :</i></b>
┃ {disk_bar} {disk}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}</blockquote>
    
    '''
    SYS_STATS = '''<blockquote>⌬ <b><i>OS SYSTEM :</i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>NETWORK STATS :</i></b>
┠ <b>Upload Data:</b> {up_data}
┠ <b>Download Data:</b> {dl_data}
┠ <b>Pkts Sent:</b> {pkt_sent}k
┠ <b>Pkts Received:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}</blockquote>
    '''
    REPO_STATS = '''<blockquote>⌬ <b><i>REPO STATISTICS :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code></blockquote>
    '''
    BOT_LIMITS = '''<blockquote>⌬ <b><i>BOT LIMITATIONS :</i></b>
┠ <b>Direct Limit :</b> {DL} GB
┠ <b>Torrent Limit :</b> {TL} GB
┠ <b>GDrive Limit :</b> {GL} GB
┠ <b>YT-DLP Limit :</b> {YL} GB
┠ <b>Playlist Limit :</b> {PL}
┠ <b>Mega Limit :</b> {ML} GB
┠ <b>Clone Limit :</b> {CL} GB
┖ <b>Leech Limit :</b> {LL} GB

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}</blockquote>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>🌀OH BHAI...Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<blockquote>🌋 <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}</blockquote>'''
    RESTARTED = '''<blockquote>🍁 <b><i>Bot Restarted!</i></b></blockquote>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Tunik🐾</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<blockquote><b><i>Task Started</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>By:</b> {Tag}\n\n</blockquote>"""
    LINKS_SOURCE = """<blockquote>➲ <b>Source:</b>
┖ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n</blockquote>"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>Task Started :</u></b>\n┃\n┖ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<blockquote><code><b><i>{Name}</i></b></code>\n</blockquote>'
    SIZE =                  '<blockquote>┠ <b>Size: </b>{Size}\n</blockquote>'
    ELAPSE =                '<blockquote>┠ <b>Elapsed: </b>{Time}\n</blockquote>'
    MODE =                  '<blockquote>┠ <b>Mode: </b>{Mode}\n</blockquote>'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<blockquote>┠ <b>Total Files: </b>{Files}\n</blockquote>'
    L_CORRUPTED_FILES =     '<blockquote>┠ <b>Corrupted Files: </b>{Corrupt}\n</blockquote>'
    L_CC =                  '<blockquote>┖ <b>By: </b>{Tag}\n\n</blockquote>'
    PM_BOT_MSG =            '<blockquote>➲ <b><i>File(s) have been Sent above</i></b></blockquote>'
    L_BOT_MSG =             '<blockquote>➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b></blockquote>'
    L_LL_MSG =              '<blockquote>➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n</blockquote>'
    
    # ----- MIRROR -------
    M_TYPE =                '<blockquote>┠ <b>Type: </b>{Mimetype}\n</blockquote>'
    M_SUBFOLD =             '<blockquote>┠ <b>SubFolders: </b>{Folder}\n</blockquote>'
    TOTAL_FILES =           '<blockquote>┠ <b>Files: </b>{Files}\n</blockquote>'
    RCPATH =                '<blockquote>┠ <b>Path: </b><code>{RCpath}</code>\n</blockquote>'
    M_CC =                  '<blockquote>┖ <b>By: </b>{Tag}\n\n</blockquote>'
    M_BOT_MSG =             '➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b></blockquote>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '📸 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<code><b><i>⏤͟͞𝙍𝙞𝙯𝙯❄️|{Name}</i></b></code>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '<blockquote>\n┃ {Bar}</blockquote>'
    PROCESSED =         '<blockquote>\n┠ <b>Processed:</b> {Processed}</blockquote>'
    STATUS =            '<blockquote>\n┠ <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> {Eta}</blockquote>'
    SPEED =             '<blockquote>\n┠ <b>Speed:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}</blockquote>'
    ENGINE =            '<blockquote>\n┠ <b>Engine:</b> {Engine}</blockquote>'
    STA_MODE =          '<blockquote>\n┠ <b>Mode:</b> {Mode}</blockquote>'
    SEEDERS =           '<blockquote>\n┠ <b>Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}</blockquote>'

    ####--------SEEDING----------
    SEED_SIZE =      '<blockquote>\n┠ <b>Size: </b>{Size}</blockquote>'
    SEED_SPEED =     '<blockquote>\n┠ <b>Speed: </b> {Speed} | '
    UPLOADED =                                     '<b>Uploaded: </b> {Upload}</blockquote>'
    RATIO =          '<blockquote>\n┠ <b>Ratio: </b> {Ratio} | '
    TIME =                                         '<b>Time: </b> {Time}</blockquote>'
    SEED_ENGINE =    '<blockquote>\n┠ <b>Engine:</b> {Engine}</blockquote>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '<blockquote>\n┠ <b>Size: </b>{Size}</blockquote>'
    NON_ENGINE =     '<blockquote>\n┠ <b>Engine:</b> {Engine}</blockquote>'

    ####--------OVERALL MSG FOOTER----------
    USER =              '<blockquote>\n┠ <b>User:</b> <code>{User}</code> | '
    ID =                                                        '<b>ID:</b> <code>{Id}</code></blockquote>'
    BTSEL =          '<blockquote>\n┠ <b>Select:</b> {Btsel}</blockquote>'
    CANCEL =         '<blockquote>\n┖ {Cancel}\n\n</blockquote>'

    ####------FOOTER--------
    FOOTER = '<blockquote>⌬ <b><i>Bot Stats</i></b>\n</blockquote>'
    TASKS =  '<blockquote>┠ <b>Tasks:</b> {Tasks}\n</blockquote>'
    BOT_TASKS = '<blockquote>┠ <b>Tasks:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n</blockquote>'
    Cpu = '<blockquote>┠ <b>CPU:</b> {cpu}% | '
    FREE =                      '<b>F:</b> {free} [{free_p}%]</blockquote>'
    Ram = '<blockquote>\n┠ <b>RAM:</b> {ram}% | '
    uptime =                     '<b>UPTIME:</b> {uptime}</blockquote>'
    DL = '<blockquote>\n┖ <b>DL:</b> {DL}/s | '
    UL =                        '<b>UL:</b> {UL}/s</blockquote>'

    ###--------BUTTONS-------
    PREVIOUS = '⬅️'
    REFRESH = ' 🍑\n{Page}'
    NEXT = '➡️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<blockquote><b>Counting:</b> <code>{LINK}</code></blockquote>'
    COUNT_NAME = '<blockquote><b><i>{COUNT_NAME}</i></b>\n┃\n</blockquote>'
    COUNT_SIZE = '<blockquote>┠ <b>Size: </b>{COUNT_SIZE}\n</blockquote>'
    COUNT_TYPE = '<blockquote>┠ <b>Type: </b>{COUNT_TYPE}\n</blockquote>'
    COUNT_SUB =  '<blockquote>┠ <b>SubFolders: </b>{COUNT_SUB}\n</blockquote>'
    COUNT_FILE = '<blockquote>┠ <b>Files: </b>{COUNT_FILE}\n</blockquote>'
    COUNT_CC =   '<blockquote>┖ <b>By: </b>{COUNT_CC}\n</blockquote>'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<blockquote><b>Searching for <i>{NAME}</i></b></blockquote>'
    LIST_FOUND = '<blockquote><b>Found {NO} result for <i>{NAME}</i></b></blockquote>'
    LIST_NOT_FOUND = '<blockquote>No result found for <i>{NAME}</i></blockquote>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<blockquote><i>No Active Downloads!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}</blockquote>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<blockquote>🔮 <b><u>User Settings :</u></b>
        
┎<b> Name :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg</blockquote>'''

    UNIVERSAL = '''<blockquote>🗿 <b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code></blockquote>'''

    MIRROR = '''<blockquote>☠ <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day</blockquote>'''

    LEECH = '''<blockquote>❄️ <b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code></blockquote>'''
