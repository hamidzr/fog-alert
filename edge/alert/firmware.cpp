#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include <PubSubClient.h>

// settings
// WiFi
const char* ssid = "newHope";
const char* password = "vandyville";

// OTA updates
const char* nodeName = "alert";
const char* otaPassword = "otahph";

// pubsub
const char* mqttServer = "broker.hivemq.com";
const char* alertTopic = "hph/threat";

// led settings
const auto LED_PIN = D4;


// pubsub globals
WiFiClient espClient;
PubSubClient client(espClient);


void ledOff() {
  digitalWrite(LED_PIN, HIGH); // active low on esp
}

void ledOn() {
  digitalWrite(LED_PIN, LOW); // turn the LED_PIN on.
}

// called to response to a threat
void alert() {
  ledOn();
  delay(500);
  ledOff();
}

void mqttOnMessage(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // TODO if topic and payload ..
  alert();

}

void mqttReconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // ... and resubscribe
      Serial.print("subscribing to ");
      Serial.print(alertTopic);
      Serial.println();
      // ... and resubscribe
      client.subscribe(alertTopic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setupWifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  // alternative connection
  /* Serial.begin(115200); */
  /* Serial.println("Booting"); */
  /* WiFi.mode(WIFI_STA); */
  /* WiFi.begin(ssid, password); */
  /* while (WiFi.waitForConnectResult() != WL_CONNECTED) { */
  /*   Serial.println("Connection Failed! Rebooting..."); */
  /*   delay(5000); */
  /*   ESP.restart(); */
  /* } */

}

void setupOTA() {
  // Port defaults to 8266
  // ArduinoOTA.setPort(8266);

  ArduinoOTA.setHostname(nodeName);

  ArduinoOTA.setPassword(otaPassword);

  ArduinoOTA.onStart([]() {
    String type;
    if (ArduinoOTA.getCommand() == U_FLASH) {
      type = "sketch";
    } else { // U_SPIFFS
      type = "filesystem";
    }

    // NOTE: if updating SPIFFS this would be the place to unmount SPIFFS using SPIFFS.end()
    Serial.println("Start updating " + type);
  });
  ArduinoOTA.onEnd([]() {
    Serial.println("\nEnd");
  });
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
  });
  ArduinoOTA.onError([](ota_error_t error) {
    Serial.printf("Error[%u]: ", error);
    if (error == OTA_AUTH_ERROR) {
      Serial.println("Auth Failed");
    } else if (error == OTA_BEGIN_ERROR) {
      Serial.println("Begin Failed");
    } else if (error == OTA_CONNECT_ERROR) {
      Serial.println("Connect Failed");
    } else if (error == OTA_RECEIVE_ERROR) {
      Serial.println("Receive Failed");
    } else if (error == OTA_END_ERROR) {
      Serial.println("End Failed");
    }
  });
  ArduinoOTA.begin();
  Serial.println("Ready");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  pinMode(LED_PIN, OUTPUT); // set the led pin as output
  ledOff();
  Serial.begin(115200);
  setupWifi();
  setupOTA();
  client.setServer(mqttServer, 1883);
  client.setCallback(mqttOnMessage);
}

void loop() {
  ArduinoOTA.handle();
  if (!client.connected()) {
    mqttReconnect();
  }
  client.loop();
}
