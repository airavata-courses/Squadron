package com.team.squadron.session.management.connection;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.team.squadron.session.management.models.UserLog;
import com.team.squadron.session.management.repositories.UserLogRepository;
import com.team.squadron.session.management.utils.Config;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;

@Component
public class SessionConsumers{

    Config config;
    UserLogRepository repository;

    @Autowired
    public SessionConsumers(Config config, UserLogRepository repository){
        this.config = config;
        this.repository = repository;
    }

    public void startConsumingLogs(){
        Properties props = new Properties();
        props.setProperty("bootstrap.servers", config.getKafkaServer());
        props.setProperty("group.id",config.getKafkaListenerTopics());
        props.setProperty("enable.auto.commit", config.getKafkaCommit());
        props.setProperty("key.deserializer", config.getKafkaDeserializer());
        props.setProperty("value.deserializer", config.getKafkaDeserializer());

        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Arrays.asList(config.getKafkaListenerTopics()));

        List<UserLog> buffer = new ArrayList<>();
        int minBatchSize = 2;
        while (true) {
            ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
            for (ConsumerRecord<String, String> record : records) {
                UserLog userlog = null;
                try {
                    userlog = new ObjectMapper().readValue(record.value(), UserLog.class);
                } catch (JsonProcessingException e) {
                    e.printStackTrace();
                }
                buffer.add(userlog);
            }
            if (buffer.size() >= minBatchSize) {
                repository.saveAll(buffer);
                consumer.commitSync();
                buffer.clear();
            }
        }
    }
}
