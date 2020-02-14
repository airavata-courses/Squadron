package com.team.squadron.session.management;

import com.team.squadron.session.management.connection.SessionConsumers;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Component;

@SpringBootApplication
public class KafkaConsumer implements CommandLineRunner {

    private SessionConsumers sessionConsumers;

    @Autowired
    public KafkaConsumer(SessionConsumers sessionConsumers) {
        this.sessionConsumers = sessionConsumers;
    }

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(KafkaConsumer.class);
        app.setWebApplicationType(WebApplicationType.NONE);
        app.run();
    }

    @Override
    public void run(String... args) throws Exception {
        sessionConsumers.startConsumingLogs();
    }
}
