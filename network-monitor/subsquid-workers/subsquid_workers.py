import requests
from datetime import datetime
import prettytable
from prettytable import PrettyTable
from hurry.filesize import size, si
import argparse

PINGS_URL = "https://scheduler.testnet.subsquid.io/workers/pings"
CHUNKS_URL = "https://scheduler.testnet.subsquid.io/chunks"
API = "https://app.subsquid.io/network/api/metrics/testnet/workers"

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--workers',
        dest='workers',
        help='Subsquid workers separated by space',
        nargs='+',
        required=True)
    return parser.parse_args()

def workerUptime(workers: list):
    uptime = requests.get(API)
    uptime_list = uptime.json()["payload"]
    s = sorted(uptime_list, key=lambda d: float(d['uptime']), reverse=True)
    print('\nWORKERS UPTIME (MY WORKERS)')
    t = PrettyTable(['#', 'node', 'uptime', 'online', 'local'])
    for  n, node in enumerate(s):
        if node['p2pAddress'] in workers:
            t.add_row([str(n+1), node['p2pAddress'][:4] + '***' + node['p2pAddress'][-4:], node['uptime'], 'up' if node['online'] else "-","*" if node['p2pAddress'] in workers else ""])
    t.align="r"
    print(t)
    print('\nWORKERS UPTIME (ALL WORKERS)')
    up = 0
    t = PrettyTable(['#', 'node', 'uptime', 'online', 'local'])
    for n, node in enumerate(s):
        t.add_row([str(n+1), node['p2pAddress'][:4] + '***' + node['p2pAddress'][-4:], node['uptime'], 'up' if node['online'] else "-","*" if node['p2pAddress'] in workers else ""])
        if node['online']:
            up += 1
    t.align="r"
    print(t)
    print('Total: {}'.format(str(len(s))))
    print('Total up: {}\n'.format(str(up)))

def workerStatus(workers: list):
    pings = requests.get(PINGS_URL)
    pings.raise_for_status()
    status = {}
    for ping in pings.json():
        if ping['peer_id'] in workers:
            status[ping['peer_id']] = {
                'worker': ping['peer_id'],
                'last_ping': datetime.fromtimestamp(ping['last_ping'] / 1000.0).isoformat(),
                'version': ping['version'],
                'stored_bytes': ping['stored_bytes'],
                'assigned_chunks_count': 0,
                'assigned_chunks_size': 0,
                'downloaded_chunks_count': 0,
                'downloaded_chunks_size': 0,
            }
    print('Fetching chunks...')
    chunks = requests.get(CHUNKS_URL)
    for ds_chunks in chunks.json().values():
        for chunk in ds_chunks:
            for worker in workers:
                if worker in chunk['assigned_to']:
                    status[worker]['assigned_chunks_count'] += 1
                    status[worker]['assigned_chunks_size'] += chunk['size_bytes']
                if worker in chunk['downloaded_by']:
                    status[worker]['downloaded_chunks_count'] += 1
                    status[worker]['downloaded_chunks_size'] += chunk['size_bytes']

    t = PrettyTable(['worker', 'version', 'last ping', 'stored', 'a chunks count', 'd chunks count', 'a chunks size', 'd chunks size'])
    for key, value in status.items():
        t.add_row([key[:4] + '***' + key[-4:],
            value['version'],
            value['last_ping'],
            size(value['stored_bytes'], system=si),
            value['assigned_chunks_count'],
            value['downloaded_chunks_count'],
            size(value['assigned_chunks_size'], system=si),
            size(value['downloaded_chunks_size'], system=si),
            ])
    t.align="r"
    print('\nWORKERS STATUS')
    print(t)
    print('Total workers: {}'.format(len(pings.json())))

def main():
    args = parseArguments()
    workers = args.workers
    print("#================================================")
    print("# Subsquid workers dashboard, by GRASSETS-TECH   ")
    print("#================================================")
    workerStatus(workers)
    workerUptime(workers)

if __name__ == '__main__':
    main()
