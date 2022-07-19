#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/17 16:13
# @Author  : nice
# @File    : arun_8600.py
# @Project : zmq-consumer


# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = arun_from_dict(json.loads(json_string))

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any, List, Dict, TypeVar, Type, Callable, cast

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AmonDataTypeValue(Enum):
    BYTE_ARRAY = "BYTE_ARRAY"
    CHAR_STRING = "CHAR_STRING"
    ENUM = "ENUM"
    IP_ADDRESS = "IP_ADDRESS"
    IP_V4_ADDRESS = "IP_V4_ADDRESS"
    IP_V6_ADDRESS = "IP_V6_ADDRESS"
    MAC_ADDRESS = "MAC_ADDRESS"
    SIGNED_INT = "SIGNED_INT"
    TIMESTAMP = "TIMESTAMP"
    UNSIGNED_INT = "UNSIGNED_INT"


@dataclass
class AmonColumn:
    name: Optional[str] = None
    type: Optional[AmonDataTypeValue] = None
    size: Optional[int] = None
    enum: Optional[str] = None
    bitfield: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AmonColumn':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([AmonDataTypeValue, from_none], obj.get("type"))
        size = from_union([from_int, from_none], obj.get("size"))
        enum = from_union([from_str, from_none], obj.get("enum"))
        bitfield = from_union([from_str, from_none], obj.get("bitfield"))
        return AmonColumn(name, type, size, enum, bitfield)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["type"] = from_union([lambda x: to_enum(AmonDataTypeValue, x), from_none], self.type)
        result["size"] = from_union([from_int, from_none], self.size)
        result["enum"] = from_union([from_str, from_none], self.enum)
        result["bitfield"] = from_union([from_str, from_none], self.bitfield)
        return result


@dataclass
class AmonMessage:
    name: Optional[str] = None
    columns: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AmonMessage':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        columns = from_union([lambda x: from_list(from_str, x), from_none], obj.get("columns"))
        return AmonMessage(name, columns)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["columns"] = from_union([lambda x: from_list(from_str, x), from_none], self.columns)
        return result


@dataclass
class Compatible:
    compatible_with: Optional[List[str]] = None
    compatible_except: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Compatible':
        assert isinstance(obj, dict)
        compatible_with = from_union([lambda x: from_list(from_str, x), from_none], obj.get("with"))
        compatible_except = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("except"))
        return Compatible(compatible_with, compatible_except)

    def to_dict(self) -> dict:
        result: dict = {}
        result["with"] = from_union([lambda x: from_list(from_str, x), from_none], self.compatible_with)
        result["except"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.compatible_except)
        return result


@dataclass
class MvStatusReason:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'MvStatusReason':
        assert isinstance(obj, dict)
        return MvStatusReason()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Arun:
    compatible: Optional[Compatible] = None
    amon_messages: Optional[Dict[str, AmonMessage]] = None
    amon_msg_category: Optional[Dict[str, str]] = None
    amon_columns: Optional[Dict[str, AmonColumn]] = None
    amon_data_types: Optional[Dict[str, AmonDataTypeValue]] = None
    ap_phy_type: Optional[Dict[str, str]] = None
    move_reason_type: Optional[Dict[str, str]] = None
    move_status: Optional[Dict[str, str]] = None
    binary_move_status: Optional[Dict[str, str]] = None
    move_status_reason: Optional[Dict[str, str]] = None
    network_type: Optional[Dict[str, str]] = None
    rra_state: Optional[Dict[str, str]] = None
    security: Optional[Dict[str, str]] = None
    steer_capability: Optional[Dict[str, str]] = None
    wifi_ap_phy: Optional[Dict[str, str]] = None
    wifi_ht_type: Optional[Dict[str, str]] = None
    anonymous: Optional[Dict[str, str]] = None
    auth_user_event_type: Optional[Dict[str, str]] = None
    mon_client_phy_type_t: Optional[Dict[str, str]] = None
    rap_type: Optional[MvStatusReason] = None
    rsta_type: Optional[MvStatusReason] = None
    mv_status_reason: Optional[MvStatusReason] = None
    wms_encr_protocol: Optional[Dict[str, str]] = None
    wms_probe_type: Optional[Dict[str, str]] = None
    sta_deauth_reason_code: Optional[Dict[str, str]] = None
    sta_deauth_aruba_reason: Optional[Dict[str, str]] = None
    sta_ft_auth_status_code: Optional[Dict[str, str]] = None
    sta_ft_r1_data_rx_status_code: Optional[Dict[str, str]] = None
    wpa_key_handshake_trigger_reason: Optional[Dict[str, str]] = None
    wpa_key_handshake_result: Optional[Dict[str, str]] = None
    wpa_key_handshake_reason: Optional[Dict[str, str]] = None
    cp_reason: Optional[Dict[str, str]] = None
    cluster_membership_status: Optional[Dict[str, str]] = None
    cluster_connection_type: Optional[Dict[str, str]] = None
    cluster_connection_status: Optional[Dict[str, str]] = None
    cluster_disconnect_reason: Optional[Dict[str, str]] = None
    cluster_incompatible_reason: Optional[Dict[str, str]] = None
    cluster_amon_operation: Optional[Dict[str, str]] = None
    health_score: Optional[Dict[str, str]] = None
    eth_mode: Optional[Dict[str, str]] = None
    eth_type: Optional[Dict[str, str]] = None
    eth_admin: Optional[Dict[str, str]] = None
    eth_operstate: Optional[Dict[str, str]] = None
    eth_speed: Optional[Dict[str, str]] = None
    eth_duplex: Optional[Dict[str, str]] = None
    eth_pse: Optional[Dict[str, str]] = None
    eth_stp: Optional[Dict[str, str]] = None
    dot11_v_reason: Optional[Dict[str, str]] = None
    reboot_reason_code: Optional[Dict[str, str]] = None
    pmm_pwr_type: Optional[Dict[str, str]] = None
    ipm_power_reduction_steps: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Arun':
        assert isinstance(obj, dict)
        compatible = from_union([Compatible.from_dict, from_none], obj.get("compatible"))
        amon_messages = from_union([lambda x: from_dict(AmonMessage.from_dict, x), from_none], obj.get("amon_messages"))
        amon_msg_category = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("amon_msg_category"))
        amon_columns = from_union([lambda x: from_dict(AmonColumn.from_dict, x), from_none], obj.get("amon_columns"))
        amon_data_types = from_union([lambda x: from_dict(AmonDataTypeValue, x), from_none], obj.get("amon_data_types"))
        ap_phy_type = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("ap_phy_type"))
        move_reason_type = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("move_reason_type"))
        move_status = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("move_status"))
        binary_move_status = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("binary_move_status"))
        move_status_reason = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("move_status_reason"))
        network_type = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("network_type"))
        rra_state = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("rra_state"))
        security = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("security"))
        steer_capability = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("steer_capability"))
        wifi_ap_phy = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("wifi_ap_phy"))
        wifi_ht_type = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("wifi_ht_type"))
        anonymous = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("anonymous"))
        auth_user_event_type = from_union([lambda x: from_dict(from_str, x), from_none],
                                          obj.get("auth_user_event_type"))
        mon_client_phy_type_t = from_union([lambda x: from_dict(from_str, x), from_none],
                                           obj.get("mon_client_phy_type_t"))
        rap_type = from_union([MvStatusReason.from_dict, from_none], obj.get("rap_type"))
        rsta_type = from_union([MvStatusReason.from_dict, from_none], obj.get("rsta_type"))
        mv_status_reason = from_union([MvStatusReason.from_dict, from_none], obj.get("mv_status_reason"))
        wms_encr_protocol = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("wms_encr_protocol"))
        wms_probe_type = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("wms_probe_type"))
        sta_deauth_reason_code = from_union([lambda x: from_dict(from_str, x), from_none],
                                            obj.get("sta_deauth_reason_code"))
        sta_deauth_aruba_reason = from_union([lambda x: from_dict(from_str, x), from_none],
                                             obj.get("sta_deauth_aruba_reason"))
        sta_ft_auth_status_code = from_union([lambda x: from_dict(from_str, x), from_none],
                                             obj.get("sta_ft_auth_status_code"))
        sta_ft_r1_data_rx_status_code = from_union([lambda x: from_dict(from_str, x), from_none],
                                                   obj.get("sta_ft_r1data_rx_status_code"))
        wpa_key_handshake_trigger_reason = from_union([lambda x: from_dict(from_str, x), from_none],
                                                      obj.get("wpa_key_handshake_trigger_reason"))
        wpa_key_handshake_result = from_union([lambda x: from_dict(from_str, x), from_none],
                                              obj.get("wpa_key_handshake_result"))
        wpa_key_handshake_reason = from_union([lambda x: from_dict(from_str, x), from_none],
                                              obj.get("wpa_key_handshake_reason"))
        cp_reason = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("cp_reason"))
        cluster_membership_status = from_union([lambda x: from_dict(from_str, x), from_none],
                                               obj.get("cluster_membership_status"))
        cluster_connection_type = from_union([lambda x: from_dict(from_str, x), from_none],
                                             obj.get("cluster_connection_type"))
        cluster_connection_status = from_union([lambda x: from_dict(from_str, x), from_none],
                                               obj.get("cluster_connection_status"))
        cluster_disconnect_reason = from_union([lambda x: from_dict(from_str, x), from_none],
                                               obj.get("cluster_disconnect_reason"))
        cluster_incompatible_reason = from_union([lambda x: from_dict(from_str, x), from_none],
                                                 obj.get("cluster_incompatible_reason"))
        cluster_amon_operation = from_union([lambda x: from_dict(from_str, x), from_none],
                                            obj.get("cluster_amon_operation"))
        health_score = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("health_score"))
        eth_mode = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_mode"))
        eth_type = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_type"))
        eth_admin = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_admin"))
        eth_operstate = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_operstate"))
        eth_speed = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_speed"))
        eth_duplex = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_duplex"))
        eth_pse = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_pse"))
        eth_stp = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("eth_stp"))
        dot11_v_reason = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("dot11v_reason"))
        reboot_reason_code = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("reboot_reason_code"))
        pmm_pwr_type = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("pmm_pwr_type"))
        ipm_power_reduction_steps = from_union([lambda x: from_list(from_str, x), from_none],
                                               obj.get("ipm_power_reduction_steps"))
        return Arun(compatible, amon_messages, amon_msg_category, amon_columns, amon_data_types, ap_phy_type,
                    move_reason_type, move_status, binary_move_status, move_status_reason, network_type, rra_state,
                    security, steer_capability, wifi_ap_phy, wifi_ht_type, anonymous, auth_user_event_type,
                    mon_client_phy_type_t, rap_type, rsta_type, mv_status_reason, wms_encr_protocol, wms_probe_type,
                    sta_deauth_reason_code, sta_deauth_aruba_reason, sta_ft_auth_status_code,
                    sta_ft_r1_data_rx_status_code, wpa_key_handshake_trigger_reason, wpa_key_handshake_result,
                    wpa_key_handshake_reason, cp_reason, cluster_membership_status, cluster_connection_type,
                    cluster_connection_status, cluster_disconnect_reason, cluster_incompatible_reason,
                    cluster_amon_operation, health_score, eth_mode, eth_type, eth_admin, eth_operstate, eth_speed,
                    eth_duplex, eth_pse, eth_stp, dot11_v_reason, reboot_reason_code, pmm_pwr_type,
                    ipm_power_reduction_steps)

    def to_dict(self) -> dict:
        result: dict = {}
        result["compatible"] = from_union([lambda x: to_class(Compatible, x), from_none], self.compatible)
        result["amon_messages"] = from_union([lambda x: from_dict(lambda x: to_class(AmonMessage, x), x), from_none],
                                             self.amon_messages)
        result["amon_msg_category"] = from_union([lambda x: from_dict(from_str, x), from_none], self.amon_msg_category)
        result["amon_columns"] = from_union([lambda x: from_dict(lambda x: to_class(AmonColumn, x), x), from_none],
                                            self.amon_columns)
        result["amon_data_types"] = from_union(
            [lambda x: from_dict(lambda x: to_enum(AmonDataTypeValue, x), x), from_none], self.amon_data_types)
        result["ap_phy_type"] = from_union([lambda x: from_dict(from_str, x), from_none], self.ap_phy_type)
        result["move_reason_type"] = from_union([lambda x: from_dict(from_str, x), from_none], self.move_reason_type)
        result["move_status"] = from_union([lambda x: from_dict(from_str, x), from_none], self.move_status)
        result["binary_move_status"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                  self.binary_move_status)
        result["move_status_reason"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                  self.move_status_reason)
        result["network_type"] = from_union([lambda x: from_dict(from_str, x), from_none], self.network_type)
        result["rra_state"] = from_union([lambda x: from_dict(from_str, x), from_none], self.rra_state)
        result["security"] = from_union([lambda x: from_dict(from_str, x), from_none], self.security)
        result["steer_capability"] = from_union([lambda x: from_dict(from_str, x), from_none], self.steer_capability)
        result["wifi_ap_phy"] = from_union([lambda x: from_dict(from_str, x), from_none], self.wifi_ap_phy)
        result["wifi_ht_type"] = from_union([lambda x: from_dict(from_str, x), from_none], self.wifi_ht_type)
        result["anonymous"] = from_union([lambda x: from_dict(from_str, x), from_none], self.anonymous)
        result["auth_user_event_type"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                    self.auth_user_event_type)
        result["mon_client_phy_type_t"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                     self.mon_client_phy_type_t)
        result["rap_type"] = from_union([lambda x: to_class(MvStatusReason, x), from_none], self.rap_type)
        result["rsta_type"] = from_union([lambda x: to_class(MvStatusReason, x), from_none], self.rsta_type)
        result["mv_status_reason"] = from_union([lambda x: to_class(MvStatusReason, x), from_none],
                                                self.mv_status_reason)
        result["wms_encr_protocol"] = from_union([lambda x: from_dict(from_str, x), from_none], self.wms_encr_protocol)
        result["wms_probe_type"] = from_union([lambda x: from_dict(from_str, x), from_none], self.wms_probe_type)
        result["sta_deauth_reason_code"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                      self.sta_deauth_reason_code)
        result["sta_deauth_aruba_reason"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                       self.sta_deauth_aruba_reason)
        result["sta_ft_auth_status_code"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                       self.sta_ft_auth_status_code)
        result["sta_ft_r1data_rx_status_code"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                            self.sta_ft_r1_data_rx_status_code)
        result["wpa_key_handshake_trigger_reason"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                                self.wpa_key_handshake_trigger_reason)
        result["wpa_key_handshake_result"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                        self.wpa_key_handshake_result)
        result["wpa_key_handshake_reason"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                        self.wpa_key_handshake_reason)
        result["cp_reason"] = from_union([lambda x: from_dict(from_str, x), from_none], self.cp_reason)
        result["cluster_membership_status"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                         self.cluster_membership_status)
        result["cluster_connection_type"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                       self.cluster_connection_type)
        result["cluster_connection_status"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                         self.cluster_connection_status)
        result["cluster_disconnect_reason"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                         self.cluster_disconnect_reason)
        result["cluster_incompatible_reason"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                           self.cluster_incompatible_reason)
        result["cluster_amon_operation"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                      self.cluster_amon_operation)
        result["health_score"] = from_union([lambda x: from_dict(from_str, x), from_none], self.health_score)
        result["eth_mode"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_mode)
        result["eth_type"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_type)
        result["eth_admin"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_admin)
        result["eth_operstate"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_operstate)
        result["eth_speed"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_speed)
        result["eth_duplex"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_duplex)
        result["eth_pse"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_pse)
        result["eth_stp"] = from_union([lambda x: from_dict(from_str, x), from_none], self.eth_stp)
        result["dot11v_reason"] = from_union([lambda x: from_dict(from_str, x), from_none], self.dot11_v_reason)
        result["reboot_reason_code"] = from_union([lambda x: from_dict(from_str, x), from_none],
                                                  self.reboot_reason_code)
        result["pmm_pwr_type"] = from_union([lambda x: from_dict(from_str, x), from_none], self.pmm_pwr_type)
        result["ipm_power_reduction_steps"] = from_union([lambda x: from_list(from_str, x), from_none],
                                                         self.ipm_power_reduction_steps)
        return result


def arun_from_dict(s: Any) -> Arun:
    return Arun.from_dict(s)


def arun_to_dict(x: Arun) -> Any:
    return to_class(Arun, x)
