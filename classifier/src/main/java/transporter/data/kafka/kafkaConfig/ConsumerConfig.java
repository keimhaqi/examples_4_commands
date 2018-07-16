package transporter.data.kafka.kafkaConfig;

import org.apache.kafka.clients.consumer.ConsumerRebalanceListener;
import org.apache.kafka.common.TopicPartition;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.annotation.EnableKafka;
import org.springframework.kafka.config.ConcurrentKafkaListenerContainerFactory;
import org.springframework.kafka.config.KafkaListenerContainerFactory;
import org.springframework.kafka.core.ConsumerFactory;
import org.springframework.kafka.core.DefaultKafkaConsumerFactory;
import org.springframework.kafka.listener.AbstractMessageListenerContainer;
import org.springframework.kafka.listener.ConcurrentMessageListenerContainer;

import java.util.Collection;
import java.util.Map;

//import org.springframework.kafka.listener.SeekToCurrentErrorHandler;

/**
 * Created by jiangzhenping on 17-10-10.
 */
@Configuration
@EnableKafka
public class ConsumerConfig {
    private static Logger logger = LoggerFactory.getLogger(ConsumerConfig.class);
    /**
     * The Partition num.
     */
    @Value("${kafka.partition.num}")
    int partitionNum;

    /**
     * Kafka listener container factory.
     **
     **@return the kafka listener container factory
     */
    @Bean
    public KafkaListenerContainerFactory<ConcurrentMessageListenerContainer<String, String>> kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, String> factory =
                new ConcurrentKafkaListenerContainerFactory<String, String>();
        factory.setConsumerFactory(consumerFactory());
        factory.setConcurrency(partitionNum);
        factory.getContainerProperties().setAckMode(AbstractMessageListenerContainer.AckMode.RECORD);
        factory.getContainerProperties().setPollTimeout(3000);
        factory.getContainerProperties().setConsumerRebalanceListener(new ConsumerRebalanceListener() {
            @Override
            public void onPartitionsRevoked(Collection<TopicPartition> partitions) {
                logger.info(partitions.toString());
            }

            @Override
            public void onPartitionsAssigned(Collection<TopicPartition> partitions) {
                logger.info(partitions.toString());
            }
        });
        return factory;
    }

    /**
     * Consumer factory consumer factory.
     * *
     * * @return the consumer factory
     */
    @Bean
    public ConsumerFactory<String, String> consumerFactory() {
        return new DefaultKafkaConsumerFactory<String, String>(consumerConfigs());
    }

    /**
     * Consumer configs map.
     * *
     * *
     * @return the map
     */
    @Bean
    public Map<String, Object> consumerConfigs() {
        return KafkaUtils.getProps(Config.KafkaConsumer);
    }

    /**
     * Listener listener.
     * *
     * * @return the listener
     */
    @Bean
    public Listener listener() {
        return new Listener();
    }
}
