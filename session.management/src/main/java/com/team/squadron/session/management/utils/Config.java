package com.team.squadron.session.management.utils;

import org.springframework.stereotype.Component;

import java.io.InputStream;
import java.util.Properties;

@Component
public class Config {
    private Properties properties;
    private String KafkaListenerTopics;
    private String KafkaServer;
    private String KafkaCommit;
    private String KafkaDeserializer;

    public Config() throws Exception {
        properties = new Properties();
        InputStream inputStream = getClass().getClassLoader().getResourceAsStream("config.properties");
        if (inputStream == null) {
            throw new Exception("Unable to find properties resource");
        }
        properties.load(inputStream);
        KafkaListenerTopics = getProperty("kafka.listening_topics");
        KafkaServer = getProperty("kafka.bootstrap.servers");
        KafkaCommit = getProperty("kafka.enable.auto.commit");
        KafkaDeserializer = getProperty("kafka.deserializer");
    }

    public String getKafkaCommit() {
        return KafkaCommit;
    }

    public String getKafkaDeserializer() {
        return KafkaDeserializer;
    }

    public String getKafkaServer() {
        return KafkaServer;
    }

    private String getProperty(String key) {
        return System.getProperty(key, properties.getProperty(key));
    }

    public String getKafkaListenerTopics() {
        return KafkaListenerTopics;
    }
}
