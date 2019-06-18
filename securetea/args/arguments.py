# -*- coding: utf-8 -*-
u"""Arguments module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 31 2018
    Version: 1.1
    Module: SecureTea

"""
import argparse


def get_args():
    """Docstring.

    Returns:
        Args: total arguments
    """
    parser = argparse.ArgumentParser(description='Arguments of SecureTea')

    parser.add_argument(
        '--conf',
        type=str,
        required=False,
        help='Path of config file. default:- "~/.securetea/securetea.conf" '
    )

    parser.add_argument(
        '--debug',
        default=False,
        action="store_true",
        help='Degug true or false'
    )

    parser.add_argument(
        '--twitter',
        required=False,
        action='store_true',
        help='Setup twitter credentials'
    )

    parser.add_argument(
        '--twilio_sms',
        required=False,
        action='store_true',
        help='Setup twilio SMS credentials'
    )

    parser.add_argument(
        '--telegram',
        required=False,
        action='store_true',
        help='Setup telegram SMS credentials'
    )

    parser.add_argument(
        '--gmail',
        action='store_true',
        required=False,
        help='Setup Gmail credentials'
    )

    parser.add_argument(
        '--slack',
        required=False,
        action='store_true',
        help='Setup Slack credentials'
    )

    parser.add_argument(
        '--aws_ses',
        required=False,
        action='store_true',
        help='Setup AWS SES credentials'
    )

    parser.add_argument(
        '--twitter_api_key',
        '-tak',
        type=str,
        required=False,
        help='Twitter api key'
    )

    parser.add_argument(
        '--twitter_api_secret_key',
        '-tas',
        type=str,
        required=False,
        help='Twitter api secret'
    )

    parser.add_argument(
        '--twitter_access_token',
        '-tat',
        type=str,
        required=False,
        help='Twitter access token'
    )

    parser.add_argument(
        '--twitter_access_token_secret',
        '-tats',
        type=str,
        required=False,
        help='Twitter access token secret'
    )

    parser.add_argument(
        '--telegram_bot_token',
        '-tbt',
        type=str,
        required=False,
        help='Telegram Bot Token'
    )

    parser.add_argument(
        '--telegram_user_id',
        '-tui',
        type=str,
        required=False,
        help='Telegram user id'
    )

    parser.add_argument(
        '--twilio_sid',
        '-tws',
        type=str,
        required=False,
        help='Twilio SID'
    )

    parser.add_argument(
        '--twilio_token',
        '-twt',
        type=str,
        required=False,
        help='Twilio authorization token'
    )

    parser.add_argument(
        '--twilio_from',
        '-twf',
        type=str,
        required=False,
        help='Twilio (From) phone number'
    )

    parser.add_argument(
        '--twilio_to',
        '-twto',
        type=str,
        required=False,
        help='Twilio (To) phone number'
    )

    parser.add_argument(
        '--slack_token',
        '-st',
        type=str,
        required=False,
        help='Slack token'
    )

    parser.add_argument(
        '--slack_user_id',
        '-suid',
        type=str,
        required=False,
        help='Slack user id'
    )

    parser.add_argument(
        '--sender_email',
        type=str,
        required=False,
        help='Gmail sender e-mail id'
    )

    parser.add_argument(
        '--to_email',
        type=str,
        required=False,
        help='Destination of e-mail'
    )

    parser.add_argument(
        '--password',
        type=str,
        required=False,
        help='Password for Gmail sender account'
    )

    parser.add_argument(
        '--aws_email',
        '-awse',
        type=str,
        required=False,
        help='AWS email id'
    )

    parser.add_argument(
        '--aws_secret_key',
        '-awss',
        type=str,
        required=False,
        help='AWS secret key'
    )

    parser.add_argument(
        '--aws_access_key',
        '-awsa',
        type=str,
        required=False,
        help='AWS access key'
    )

    parser.add_argument(
        '--firewall',
        '-f',
        required=False,
        action='store_true',
        help='Start firewall'
    )

    parser.add_argument(
        '--interface',
        required=False,
        help='Name of the interface'
    )

    parser.add_argument(
        '--inbound_IP_action',
        type=str,
        required=False,
        help='Inbound IP rule action'
    )

    parser.add_argument(
        '--inbound_IP_list',
        type=str,
        required=False,
        help='List of inbound IPs to look for'
    )

    parser.add_argument(
        '--outbound_IP_action',
        type=str,
        required=False,
        help='Outbound IP rule action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--outbound_IP_list',
        type=str,
        required=False,
        help='List of outbound IPs to look for'
    )

    parser.add_argument(
        '--protocol_action',
        type=str,
        required=False,
        help='Protocol action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--protocol_list',
        type=str,
        required=False,
        help='List of protocols to look for'
    )

    parser.add_argument(
        '--scan_action',
        type=str,
        required=False,
        help='Scan load action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--scan_list',
        type=str,
        required=False,
        help='List of extensions to scan for'
    )

    parser.add_argument(
        '--dest_port_action',
        type=str,
        required=False,
        help='Destination port action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--dest_port_list',
        type=str,
        required=False,
        help='List of destination ports to look for'
    )

    parser.add_argument(
        '--source_port_action',
        type=str,
        required=False,
        help='Source port action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--source_port_list',
        type=str,
        required=False,
        help='List of source ports to look for'
    )

    parser.add_argument(
        '--HTTP_request_action',
        type=str,
        required=False,
        help='HTTP request action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--HTTP_response_action',
        type=str,
        required=False,
        help='HTTP response action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--dns_action',
        type=str,
        required=False,
        help='DNS action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--dns_list',
        type=str,
        required=False,
        help='List of DNS to look for'
    )

    parser.add_argument(
        '--time_lb',
        type=str,
        required=False,
        help='Time lower bound'
    )

    parser.add_argument(
        '--time_ub',
        type=str,
        required=False,
        help='Time upper bound'
    )

    parser.add_argument(
        '--insecure_headers',
        '-ih',
        action="store_true",
        required=False,
        help="Test URL for insecure headers"
    )

    parser.add_argument(
        '--url',
        '-u',
        type=str,
        required=False,
        help="URL on which operations are to be performed"
    )

    parser.add_argument(
        '--ids',
        action="store_true",
        required=False,
        help="Start Intrusion Detection System (IDS)"
    )

    parser.add_argument(
        '--threshold',
        '-th',
        type=int,
        required=False,
        help="Intrusion Detection System (IDS) threshold"
    )

    parser.add_argument(
        '--system_log',
        '-sys_log',
        action="store_true",
        required=False,
        help="Start system log monitoring process"
    )

    parser.add_argument(
        '--server-log',
        action="store_true",
        required=False,
        help="Start server log monitoring process"
    )

    parser.add_argument(
        '--log-file',
        type=str,
        required=False,
        help="Path of the log file"
    )

    parser.add_argument(
        '--log-type',
        type=str,
        required=False,
        help="Type of the log file (Apache/Nginx)"
    )

    parser.add_argument(
        '--window',
        type=int,
        required=False,
        help="Days old log to process"
    )

    parser.add_argument(
        '--ip-list',
        type=str,
        required=False,
        help="List of IPs to grab from log file"
    )

    parser.add_argument(
        '--status-code',
        type=str,
        required=False,
        help="List of status code to grab from log file"
    )

    args = parser.parse_args()
    return args
