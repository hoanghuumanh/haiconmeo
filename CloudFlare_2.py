
import sys
import CloudFlare

def main():
    zone_name = "haiconmeo.tk"
    cf = CloudFlare.CloudFlare()
    zone_info = cf.zones.post(data={'jump_start':False, 'name': zone_name})
    zone_id = zone_info['id']

    dns_records = [
        {'name':'foo', 'type':'AAAA', 'content':'2001:d8b::1'},
        {'name':'foo', 'type':'A', 'content':'192.168.0.1'},
        {'name':'duh', 'type':'A', 'content':'10.0.0.1', 'ttl':120},
        {'name':'bar', 'type':'CNAME', 'content':'foo'},
        {'name':'shakespeare', 'type':'TXT', 'content':"What's in a name? That which we call a rose by any other name ..."}
    ]

    for dns_record in dns_records:
        r = cf.zones.dns_records.post(zone_id, data=dns_record)
    exit(0)


main()