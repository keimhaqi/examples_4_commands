package transporter.data.kafka.kafkaConfig;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.annotation.EnableKafka;
import org.springframework.kafka.core.DefaultKafkaProducerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.core.ProducerFactory;

import java.util.Map;

@Configuration
@EnableKafka
public class ProducerConfig {

    /**
     * 后端Producer配置
     *
     * @return the map
     */
    public Map<String, Object> backendProducerConfigs() {
        return KafkaUtils.getProps(Config.SearchKafkaProducer);
    }

    /**
     * 后端Producer工厂
     *
     * @return the producer factory
     */
    @Bean
    public ProducerFactory<String, String> backendProducerFactory() {
        return new DefaultKafkaProducerFactory<>(backendProducerConfigs());
    }

    /**
     * 后端Producer实例
     *
     * @return the kafka template
     */
    @Bean
    public KafkaTemplate<String, String> backendTemplate() {
        return new KafkaTemplate<>(backendProducerFactory());
    }

    @Bean
    public KafkaUtils kafkaUtils(){
        return new KafkaUtils();
    }
}
