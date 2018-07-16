package transporter.data.kafka.kafkaConfig;
import org.springframework.context.annotation.Configuration;

@Configuration
public class Config {
    // kafka消费者配置文件名称
    public static final String KafkaConsumer = "kafkaConsumerConfiguration.properties";
    public static final String SearchKafkaProducer = "kafkaProducerConfiguration.properties";
}
