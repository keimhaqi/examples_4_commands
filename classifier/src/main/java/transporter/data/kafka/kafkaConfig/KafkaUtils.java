package transporter.data.kafka.kafkaConfig;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.stereotype.Service;
import org.springframework.util.concurrent.ListenableFuture;
import org.springframework.util.concurrent.ListenableFutureCallback;

import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

/**
 * Kafka工具类
 */
@Service
public class KafkaUtils{

    /**
     * kafka消费者topic设置。
     */

    @Autowired
    private KafkaTemplate<String, String> urProducer;
    /**
     * The constant logger.
     */
    private final Logger logger = LoggerFactory
            .getLogger(KafkaUtils.class);


    /**
     * 获取配置文件.
     *
     * @param fileName the file name
     * @return the props
     */
    public static Map<String, Object> getProps(String fileName) {
        // 配置文件
        Properties props = null;
        InputStream inputStream = null;
        try {
            inputStream = Thread.currentThread().getContextClassLoader()
                    .getResourceAsStream(fileName);
            if (inputStream == null)
                throw new IllegalArgumentException("该目录下不存在文件: kafkaConsumerConfiguration.properties");
            props = new Properties();
            props.load(inputStream);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (inputStream != null) {
                    inputStream.close();
                }
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
        Map<String, Object> map = new HashMap<String, Object>();
        if (!props.isEmpty()) {
            for (Map.Entry<Object, Object> e : props.entrySet()) {
                map.put((String) e.getKey(), e.getValue());
            }
        }
        return map;
    }

    public void sendToBackend(String json, String topic) {
        // 向Kafka服务器发送消息
        ListenableFuture<SendResult<String, String>> future = urProducer.send(topic, json);
        // 发送消息的回调函数
        future.addCallback(new ListenableFutureCallback<SendResult<String, String>>() {
            @Override
            public void onSuccess(SendResult<String, String> result) {
                logger.info("Send To Backend {} Success:{}", topic, json);
            }

            @Override
            public void onFailure(Throwable ex) {
                logger.error("Error:" + ex.getMessage());
            }
        });
    }

}
