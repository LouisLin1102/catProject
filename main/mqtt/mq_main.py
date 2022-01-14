from os import urandom
import time
import mqtt.mq as mq
import datetime
import argparse
import json
import os



class SendMessageFunction:
    def __init__(self,args,date,start_time,end_time,duration):
        self.args = args
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.sub_topic = "events"
        self.sub_folder = 'mqtt'
        
    def push_message(self):
        minimum_backoff_time = 1
        MAXIMUM_BACKOFF_TIME = 32
        should_backoff = False
        mqtt_topic = "/devices/{}/{}/{}".format(self.args.device_id, self.sub_topic,self.sub_folder)
        jwt_iat = datetime.datetime.now(tz=datetime.timezone.utc)
        jwt_exp_mins = self.args.jwt_expires_minutes
        client = mq.get_client(
            self.args.project_id,
            self.args.cloud_region,
            self.args.registry_id,
            self.args.device_id,
            self.args.private_key_file,
            self.args.algorithm,
            self.args.ca_certs,
            self.args.mqtt_bridge_hostname,
            self.args.mqtt_bridge_port,
        )
        # Publish num_messages messages to the MQTT bridge once per second.
        for i in range(1, self.args.num_messages + 1):
            # Process network events.
            client.loop()

            # Wait if backoff is required.
            if should_backoff:
                # If backoff time is too large, give up.
                if minimum_backoff_time > MAXIMUM_BACKOFF_TIME:
                    print("Exceeded maximum backoff time. Giving up.")
                    break

                # Otherwise, wait and connect again.
                delay = minimum_backoff_time + urandom.randint(0, 1000) / 1000.0
                print("Waiting for {} before reconnecting.".format(delay))
                time.sleep(delay)
                minimum_backoff_time *= 2
                client.connect(self.args.mqtt_bridge_hostname, self.args.mqtt_bridge_port)

            # payload = "{}/{}-payload-{}".format(args.registry_id, args.device_id, i)
            start_time = datetime.datetime.strftime( self.start_time,'%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.strftime( self.end_time,'%Y-%m-%d %H:%M:%S')
            data = { 'date' : self.date ,'start_time':start_time,'end_time':end_time,'duration':self.duration}
            payload = json.dumps(data)
            
            print("Publishing message {}/{}: '{}'".format(i, self.args.num_messages, payload))
            seconds_since_issue = (datetime.datetime.now(tz=datetime.timezone.utc) - jwt_iat).seconds
            if seconds_since_issue > 60 * jwt_exp_mins:
                print("Refreshing token after {}s".format(seconds_since_issue))
                jwt_iat = datetime.datetime.now(tz=datetime.timezone.utc)
                client.loop()
                client.disconnect()
                client = mq.get_client(
                    self.args.project_id,
                    self.args.cloud_region,
                    self.args.registry_id,
                    self.args.device_id,
                    self.args.private_key_file,
                    self.args.algorithm,
                    self.args.ca_certs,
                    self.args.mqtt_bridge_hostname,
                    self.args.mqtt_bridge_port,
                )
            # Publish "payload" to the MQTT topic. qos=1 means at least once
            # delivery. Cloud IoT Core also supports qos=0 for at most once
            # delivery.
            client.publish(mqtt_topic, payload, qos=1)

            # Send events every second. State should not be updated as often
            # for i in range(0, 60):
            #     time.sleep(1)
            #     client.loop()
        
    


# Publish to the events or state topic based on the flag.
# sub_topic = "events" if args.message_type == "event" else "state"
# sub_folder = 'mqtt'
# mqtt_topic = "/devices/{}/{}/{}".format(args.device_id, sub_topic,sub_folder)

