import json


def amon2dict(amon: str) -> dict:
    amon_dict = json.loads(amon)
    msg_dict = {}

    msg_dict['name'] = amon_dict.get('name')
    msg_dict['type'] = amon_dict.get('type')
    # msg_dict['major']=amon_dict.get('major')
    # msg_dict['minor']=amon_dict.get('minor')
    msg_dict['timestamp'] = amon_dict.get('timestamp')
    msg_dict['sequence'] = amon_dict.get('sequence')
    msg_dict['source'] = amon_dict.get('source')
    msg_dict['rows'] = amon_dict.get('rows')
    msg_dict['data'] = []

    row_num = 0
    while row_num < amon_dict.get('rows'):
        index = 0
        temp_val = {}
        for column_name in amon_dict.get('columns'):
            temp_val[column_name] = amon_dict.get('data')[row_num][index]
            index += 1
        msg_dict['data'].append(temp_val)
        row_num += 1

    return msg_dict


# type = 0  AMON_RADIO_STATS_MESSAGE
def amon_radio_stats_msg(amon: dict):
    pass


# type = 1  AMON_VAP_STATS_MESSAGE
def amon_vap_stats_msg(amon: dict):
    pass


# type = 2  AMON_STATION_STATS_MESSAGE
def amon_station_stats_msg(amon: dict):
    pass


# type = 3  AMON_AP_NEIGHBORS_MESSAGE
def amon_ap_neighbors_msg(amon: dict):
    pass


# type = 4  AMON_UNASSOCIATED_STA_MESSAGE
def amon_unassociated_sta_msg(amon: dict):
    pass


# type = 10  AMON_USER_INFO_MESSAGE
def amon_user_info_msg(amon: dict):
    pass


# type = 11 AMON_AP_INFO_MESSAGE
def amon_ap_info_msg(amon: dict):
    pass


# type = 12 AMON_RADIO_INFO_MESSAGE
def amon_radio_info_msg(amon: dict):
    pass


# type = 13 AMON_VAP_INFO_MESSAGE
def amon_vap_info_msg(amon: dict):
    pass


# type = 14 AMON_MON_AP_INFO_MESSAGE
def amon_mon_ap_info_msg(amon: dict):
    pass


# type = 15 AMON_MON_AP_STATS_MESSAGE
def amon_mon_ap_stats_msg(amon: dict):
    pass


# type = 16 AMON_MON_STA_INFO_MESSAGE
def amon_mon_sta_info_msg(amon: dict):
    pass


# type = 17 AMON_MON_STA_STATS_MESSAGE
def amon_mon_sta_stats_msg(amon: dict):
    pass


# type = 18 AMON_AP_SYSTEM_STATS_MESSAGE
def amon_ap_system_stats_msg(amon: dict):
    pass


# type = 19 AMON_STATION_RSSI_INFO_MESSAGE
def amon_station_rssi_info_msg(amon: dict):
    pass


# type = 20 AMON_STATION_STEER_INFO_MESSAGE
def amon_station_steer_info_msg(amon: dict):
    pass


# type = 29 AMON_DHCP_STATION_INFO_MESSAGE
def amon_dhcp_station_info_msg(amon: dict):
    pass


# type = 30 AMON_MACAUTH_MESSAGE
def amon_macauth_msg(amon: dict):
    pass


# type = 31 AMON_AUTH_SERVER_TIMEOUT_MESSAGE
def amon_auth_server_timeout_msg(amon: dict):
    pass


# type = 32 AMON_DOT1X_MESSAGE
def amon_dot1x_msg(amon: dict):
    pass


# type =33   AMON_WPA_KEY_HANDSHAKE_MESSAGE
def amon_wpa_key_handshake_msg(amon: dict):
    pass


# type = 34 AMON_CP_MESSAGE
def amon_cp_msg(amon: dict):
    pass


# type = 35 AMON_PASSIVE_AP_STATION_STATS_MESSAGE
def amon_passive_ap_station_stats_msg(amon: dict):
    pass


# type = 36 AMON_PASSIVE_CTRL_STATION_STATS_MESSAGE
def amon_passive_ctrl_station_stats_msg(amon: dict):
    pass


# type = 37 AMON_PASSIVE_AP_AGGR_STATS_MESSAGE
def amon_passive_ap_aggr_stats_msg(amon: dict):
    pass


# type = 55 AMON_MON_AP_DEL_MESSAGE
def amon_mon_ap_del_msg(amon: dict):
    pass


# type = 56 AMON_MON_STA_DEL_MESSAGE
def amon_mon_sta_del_msg(amon: dict):
    pass


# type = 57 AMON_MON_AP_SNAPSHOT_MESSAGE
def amon_mon_ap_snapshot_msg(amon: dict):
    pass


# type = 58 AMON_MON_STA_SNAPSHOT_MESSAGE
def amon_mon_sta_snapshot_msg(amon: dict):
    pass


# type = 67 AMON_HWMON_TEMP_DETAIL_MESSAGE
def amon_hwmon_temp_detail_msg(amon: dict):
    pass


# type = 68 AMON_HWMON_FAN_DETAIL_MESSAGE
def amon_hwmon_fan_detail_msg(amon: dict):
    pass


# type = 71 AMON_HWMON_SYS_INFO_MESSAGE
def amon_hwmon_sys_info_msg(amon: dict):
    pass


# type = 81 AMON_BSSID_TUNNEL_STATS_MESSAGE
def amon_bssid_tunnel_stats_msg(amon: dict):
    pass


# type = 82 AMON_USER_FINGERPRINT_INFO_MESSAGE
def amon_user_fingerprint_info_msg(amon: dict):
    pass


# type = 89 AMON_RADIO_STATS_EXT_MESSAGE
def amon_radio_stats_ext_msg(amon: dict):
    pass


# type = 90 AMON_VAP_STATS_EXT_MESSAGE
def amon_vap_stats_ext_msg(amon: dict):
    pass


# type = 91 AMON_STATION_STATS_EXT_MESSAGE
def amon_station_stats_ext_msg(amon: dict):
    pass


# type = 108 AMON_AP_ETH_STATS_MESSAGE
def amon_ap_eth_stats_msg(amon: dict):
    pass
