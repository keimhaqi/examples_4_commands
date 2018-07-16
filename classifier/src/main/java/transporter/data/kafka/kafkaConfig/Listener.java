package transporter.data.kafka.kafkaConfig;

import transporter.core.services.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.annotation.KafkaListener;

/**
 * Created by jiangzhenping on 17-10-10.
 */
@Configuration
public class Listener {
    @Autowired
    private KafkaUtils kafkaUtils;
    @Autowired
    private Service service;

    private Logger logger = LoggerFactory.getLogger(Listener.class);

    @KafkaListener(topics = "${kafka.producer.topic}")
    public void test(String message){
        System.out.println(message);
        service.transport4HotProduct(message);
        kafkaUtils.sendToBackend(message, "demo2");
    }
}