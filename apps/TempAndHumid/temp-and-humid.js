var awsIot = require('aws-iot-device-sdk');
var exec = require('child_process').exec;

/*
 * 温度湿度センサーから値を読み取って、
 * aws iotにjson形式でデータを送信する。
 *
 * 前提：aws-iot-devise-sdk npmでインストールする必要あり。
 */

// Define paramerters to publish a message
//AWS iot の設定情報
var device = awsIot.device({
  region: 'ap-northeast-1',
  clientId: 'raspi',
  privateKey: '../certs/private.pem.key',
  clientCert: '../certs/certificate.pem.crt',
  caCert: '../certs/root-CA.crt',
});

//設定内容 
//温度湿度のセンサー入力Pin
DHT_pin=4
//AWSIoTへの転送間隔(ミリ秒)
//wait_time=3600000 //1hour
wait_time=100000 //10sec 
//取得場所
place = 'my-house';
//デバイスID
deviceid = "rspi"

// Connect to Message Broker
device.on('connect', function() {
    console.log('Connected to Message Broker.');

    // Loop every 10 sec
    setInterval(function pub_info() {

        exec("python libs/get_temp_and_humid.py " + DHT_pin , function (error, stdout, stderr) {
          if (error !== null) {
            console.log('exec error: ' + error);
            return
          }
          datas = stdout.split(",")
          // Compose records
          var record = {
              "deviceid": deviceid,
              "place": place,
              "timestamp": datas[0],
              "温度": datas[1],
              "湿度": datas[2]
          };

          // Serialize record to JSON format and publish a message
          var message = JSON.stringify(record);
          console.log("Publish: " + message);
          device.publish('test/pub', message);
        });

        return pub_info;
    }(), wait_time);//1hour
//    }, 10000);//10sec
});

