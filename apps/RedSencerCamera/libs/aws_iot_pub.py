#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import ConfigParser


#aws設定ファイル＊呼び出しファイルからの相対パス
private_path = "../certs/private.pem.key"
rootCA_path = "../certs/root-CA.crt"
certificate_path = "../certs/certificate.pem.crt"

#設定ファイルの読み込み
inifile = ConfigParser.SafeConfigParser()
inifile.read('conf/config.ini')


#awsiot
endpoint = inifile.get('awsiot', 'endpoint')
client = inifile.get('awsiot', 'client')
port = inifile.get('awsiot', 'port')

def publish(path):
    print("path is:" + path)
    print('start')
    # For certificate based connection
    myMQTTClient = AWSIoTMQTTClient(client)

    # For Websocket connection
    # myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
    # Configurations
    # For TLS mutual authentication
    myMQTTClient.configureEndpoint(endpoint, 8883)
    # For Websocket
    # myShadowClient.configureEndpoint("YOUR.ENDPOINT", 443)

    myMQTTClient.configureCredentials(rootCA_path, private_path, certificate_path)
    # For Websocket, we only need to configure the root CA
    # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")

    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    print('connect')
    myMQTTClient.connect()
    print('cned')
    msg = "{\"url\":\"" + path  + "\"}"
    print(msg)
    myMQTTClient.publish("test/pub", msg, 0)
    #print('pass')
    #myMQTTClient.subscribe("myTopic", 1, customCallback)
    #myMQTTClient.unsubscribe("myTopic")
    myMQTTClient.disconnect()

