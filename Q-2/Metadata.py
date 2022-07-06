#!/usr/bin/env python
import requests
import json
def load():
    awsurl = '<http://ipaddress/latest'

    awsmetadata = {'dynamic': {}, 'meta-data': {}, 'user-data': {}}
    for subsect in awsmetadata.keys():
        dataparse('{0}/{1}/'.format(awsurl, subsect), awsmetadata[subsect])
    return awsmetadata

def dataparse(url, d):
    r = requests.get(url)
    if r.status_code == 404:
        return
    for l in r.text.split('\n'):
        if not l: # "instance-identity/\n" case
            continue
        newurl = '{0}{1}'.format(url, l)
        # a key is detected with a final '/'
        if l.endswith('/'):
            newkey = l.split('/')[-2]
            d[newkey] = {}
            dataparse(newurl, d[newkey])
        else:
            r = requests.get(newurl)
            if r.status_code != 404:
                try:
                    d[l] = json.loads(r.text)
                except ValueError:
                    d[l] = r.text
            else:
                d[l] = None

if __name__ == '__main__':
    print(json.dumps(load()))
